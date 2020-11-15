from rest_framework import serializers
from django.contrib.auth.models import User

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
            raise serializers.ValidationError({'password': 'Passwords Must Match!'})
        
        
        new_user.set_password(password)
        new_user.save(password)

        return new_user

class Login_Serializer(serializers.ModelSerializer):
    
    def post(self, request):
        pass
