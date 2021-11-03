from django.db import models
from django.db.models import fields
from rest_framework import serializers
from quiz.models import Answer, Category, Question, Quizzes

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]




class RandomQuestionSerializer(serializers.ModelSerializer):


    # answer = serializers.StringRelatedField(many=True)
    answer = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = [
            'title',
            'answer'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = [
            'title',
            'answer',
            'quiz',
        ]


class CreateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
            'category'
        ]

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]