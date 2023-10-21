from rest_framework import serializers
from django.contrib.auth.models import User
from .models import rut

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','groups')

class rutSerializer(serializers.ModelSerializer):
    class Meta:
        model = rut
        fields = '__all__'