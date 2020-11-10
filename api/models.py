from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(null=False,max_length=100,unique=True)
    email = models.EmailField(null=False,unique=True)
    password = models.CharField(max_length=50,null=False)