from rest_framework.views import APIView, Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .serializer import RegistrationSerializer, LoginSerializer



class Registration(APIView):
    def post(self, request: Request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "User has been successfully created"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)
     
class Login(APIView):
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        user = serializer.is_valid()
        if user:
            login(request, user)
            return Response(
                {"status": "login completed successfully"},
                status=status.HTTP_202_ACCEPTED
            )
        return Response(serializer.errors)
    

# {"username": "test", "password": "test"}
# {"username": "test", "password": "test"}