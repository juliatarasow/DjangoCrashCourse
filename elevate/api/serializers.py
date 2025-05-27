from rest_framework import serializers
from . models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta: # here we specify the Attributes/Props
        model = Product
        fields = ['id', 'name', 'description', 'price']
        # fields = '__all__' 

class RegistrationSerializer(serializers.ModelSerializer):
    """
    User registration serializer with password confirmation.
   
    Handles user creation with password matching validation.
    Requires password confirmation field and hashes password securely.
    """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True) # write_only=True -> can not be read! (GET)-> only: PUT/POST
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = { # extra key word arguments -> extra configuration for existing fields
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )

        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Sorry, the passwords did not match'})

        user.set_password(password) # password is hashed automatically
        user.save()
        return user
