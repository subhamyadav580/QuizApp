from django.db.models import fields
from rest_framework import serializers
from quizApp.models import Subject, User

class UserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'is_teacher', 'is_student']

    def save(self, **kwargs):
        account = User(email = self.validated_data['email'], username = self.validated_data['username'], 
                        is_teacher=self.validated_data['is_teacher'], is_student = self.validated_data['is_student'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password!= password2:
            return serializers.ValidationError({'password' : 'Password not matched'})
        account.set_password(password)
        account.save()
        return account


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject

        fields = ['name']

    def save(self):
        print(self.validated_data)
        subject = Subject(name=self.validated_data['name'])
        account = self.validated_data['User']
        if account.is_teacher:
            subject.save()
            return subject
        else:
            return serializers.ValidationError({'User Error' : 'Not allowded to add subjects'})
        


