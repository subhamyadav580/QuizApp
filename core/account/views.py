from django.shortcuts import render
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import permissions, serializers, status
from rest_framework.authtoken.models import Token

class UserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            allData = {}
            token = Token.objects.get(user=account).key
            allData = {
                'Message' : 'User Registerd successfully',
                'username' : account.username,
                'is_teacher' : account.is_teacher,
                'is_student' : account.is_student,
                'Token' : token
            }
            return Response(allData, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)