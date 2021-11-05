from django.shortcuts import render
from rest_framework.views import APIView

class UserRegistration(APIView):
    def post(self, request, format=None, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)