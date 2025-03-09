from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
    
    def is_valid(self):
        user = authenticate(
            username=self.initial_data["username"],
            password=self.initial_data["password"]
        )
        # print(self.initial_data["username"])
        # print(self.initial_data["password"])
        
        if user: 
            return user
        raise serializers.ValidationError(
            {"status": "Incorrect nickname or password"}
        )
        