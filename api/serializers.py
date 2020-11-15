from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib import auth

# Register serializer
class Register_Serializer(serializers.ModelSerializer):

    # Created a new field for ConfirmedPassword
    password2 = serializers.CharField(style={'input-type': 'password'}, write_only=True) 

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password','password2']
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def save(self, validated_data):
        new_user = User(
            username = self.validated_data['username'],     
            email = self.validated_data['email'],
            first_name= self.validated_data['first_name'],
            last_name= self.validated_data['last_name']     
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2 :
            raise serializers.ValidationError(
                {'password': 'Passwords Must Match!'}
            )
        
        
        new_user.set_password(password)
        new_user.save(password)

        return new_user

class Login_Serializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128,min_length=3)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=3)
    tokens = serializers.CharField(max_length=128, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','tokens']
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def validate(self, request):
        email = request.get('email', '')
        password = request.get('password', '')
        
        # Checks if user is authenticated 
        user = auth.authenticate(email=email, password=password)

       
        if user is None:
            raise serializers.ValidationError(
                {'Error' : 'Wrong information'}
            )

        return {
            'email' : user.email,
            'token' : user.tokens(),
        }
