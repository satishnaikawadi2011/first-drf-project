from rest_framework import serializers
from .models import User


# TODO: From Scratch
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100,allow_blank=False)
#     email =  serializers.EmailField(allow_blank=False)
#     password =  serializers.CharField(max_length=50,allow_blank=False)

#     def create(self,validated_data):
#         print("In Create")
#         print(validated_data)
#         return User.objects.create(**validated_data)

#     def validate_email(self,email):
#         if User.objects.filter(email=email).count() != 0:
#             raise serializers.ValidationError('Email is already in use !')
#         return email

#     def validate_username(self,username):
#         if User.objects.filter(username=username).count() != 0:
#             raise serializers.ValidationError('username is already in use !')
#         return username



# TODO: With ModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email']

    def validate_email(self,email):
        if User.objects.filter(email=email).count() != 0:
            raise serializers.ValidationError('Email is already in use !')
        return email

    def validate_username(self,username):
        if User.objects.filter(username=username).count() != 0:
            raise serializers.ValidationError('username is already in use !')
        return username