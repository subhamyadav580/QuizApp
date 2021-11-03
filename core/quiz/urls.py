from django.urls import path

from .views import CreateCategory, CreateQuiz, Quiz, QuizQuestion, RandomQuestion

app_name = "quiz"


urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions'),
    path('createQuiz', CreateQuiz.as_view(), name='createQuiz'),
    path('createCategory', CreateCategory.as_view(), name='createcategory')
]
