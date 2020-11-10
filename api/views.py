from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers,status
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import j_to_p,p_to_j,is_user_exists,convert_errors
import io


# Create your views here.

# TODO: Without API VIEW
# def user_detail(request,id):
#     user = User.objects.get(pk=id)
#     serializer = UserSerializer(user)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')


# def user_list(request):
#     user = User.objects.all()
#     serializer = UserSerializer(user,many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

# @csrf_exempt
# def update_user(request,id):
#     if request.method == 'PATCH':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         user = User.objects.get(pk=id)
#         serializer = UserSerializer(user,data=python_data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'msg':'data updated patially!'})
#         errors = convert_errors(serializer.errors)
#         json_data = p_to_j(errors)
#         return HttpResponse(json_data,content_type='application/json',status=400)
        



# @csrf_exempt
# def create_user(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream )
#         serializer = UserSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Created !'}
#             json_data = p_to_j(res)
#             return HttpResponse(json_data,content_type='application/json')
        
#         errors = convert_errors(serializer.errors)
#         json_data = p_to_j({'errors':errors})
#         return HttpResponse(json_data,content_type='application/json',status=400)
            
# @csrf_exempt
# def delete_user(request,id):
#     if request.method == 'DELETE':
#         if is_user_exists(id):
#             user = User.objects.get(pk=id)
#             user.delete()
#             return JsonResponse({'msg':'Data deleted successfully !'})
#         return JsonResponse({'errors':{'general':'User does not exists !'}},status=404)


# TODO: With API VIEW

@api_view(['POST'])
def create_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created !'}
            return Response(res)
        errors = convert_errors(serializer.errors)
        return Response({'errors':errors})

@api_view(['GET'])
def user_detail(request,id):
    if is_user_exists(id):     
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response({'errors':{'general':'User does not exists !'}})


@api_view(['GET'])
def user_list(request):
    user = User.objects.all()
    serializer = UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_user(request,id):
    if is_user_exists(id):
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated patially!'})
        errors = convert_errors(serializer.errors)
        return Response({'errors':errors})
    return Response({'errors':{'general':'User not found !'}})


@api_view(['DELETE'])
def delete_user(request,id):
        if is_user_exists(id):
            user = User.objects.get(pk=id)
            user.delete()
            return Response({'msg':'Data deleted successfully !'})
        return Response({'errors':{'general':'User does not exists !'}},status=404)