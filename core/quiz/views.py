from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from quiz.models import Question, Quizzes
from quiz.serializers import QuizSerializer,RandomQuestionSerializer,QuestionSerializer, CreateQuizSerializer, CreateCategorySerializer
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from quiz.permissions import AuthorAllStaffAllButEditOrReadOnly


class CreateCategory(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    def post(self, request, format=None, **kwargs):
        serializer = CreateCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class CreateQuiz(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    def post(self, request, format=None, **kwargs):
        serializer = CreateQuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RandomQuestion(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


