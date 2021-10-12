from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from quizApp.models import Subject, User
from quizApp.serializers import UserSerializers, SubjectSerializers,QuizSerializers
from rest_framework.authtoken.models import Token


@api_view(['POST',])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registerd'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        
        return Response(data)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def AddSubject(request):
    if request.method == 'POST':
        serializer = SubjectSerializers(data=request.data, context = {'request' : request})
        data = {}
        if serializer.is_valid():
            subject = serializer.save()
            data['Response'] = 'successfully added'
            data['name'] = subject.name
        else:
            data = serializer.errors
        return Response(data)



@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def CreateQuiz(request):
    if request.method == 'POST':
        account = request.user
        if account.is_teacher:
            serializer = QuizSerializers(data=request.data)
            data = {}
            if serializer.is_valid():
                quiz = serializer.save()
                data['Response'] = 'successfully added'
                data['Quiz Name'] = quiz.name
                data['Subject Name'] = quiz.subject
            else:
                data = serializer.errors
            return Response(data)
        else:
            return Response({'User Error' : 'Method Not Allowded'})


