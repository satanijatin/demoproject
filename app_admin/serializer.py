
from rest_framework import serializers

from django.contrib.auth.hashers import make_password, check_password


from .models import *

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Admin
        fields='__all__'

    def create(self,validated_data):
        user=Admin.objects.create(
            name=validated_data['name'],
             email=validated_data['email'],
            password=make_password(validated_data['password']),
              language=validated_data['language'],
               gender=validated_data['gender'],
            )
        
        user.save()
        return user
    

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields='__all__'


class BookSerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=True)
    class Meta:
        model=Book
        fields='__all__'

  
   

class BookSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model=Book
        fields='__all__'

  