from django.contrib import admin
from quizApp.models import Answer, Question, Student, StudentAnswer, User,Subject,Quiz,TakenQuiz
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_student", "is_teacher")
    list_editable = ("is_student", "is_teacher")

admin.site.register(User, UserAdmin)

admin.site.register(Subject)

admin.site.register(Quiz)

admin.site.register(Question)

admin.site.register(Answer)

admin.site.register(Student)

admin.site.register(TakenQuiz)

admin.site.register(StudentAnswer)