from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import User

def p_to_j(data):
    json_data = JSONRenderer().render(data)
    return json_data

def j_to_p(data):
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        return python_data

def is_user_exists(id):
    users = User.objects.filter(pk=id)
    if users.count() == 0:
        return False
    return True

def convert_errors(errors):
    transformed_errors = {}
    for key in errors.keys():
        transformed_errors[key] = errors[key][0]
    return transformed_errors
