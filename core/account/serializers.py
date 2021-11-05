from django.db.models import fields
from rest_framework import serializers, validators

from account.models import Account

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[validators.UniqueValidator(queryset=Account.objects.all())])
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = [
            'username', 'password', 'password2', 'is_teacher', 'is_student'
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        account = Account(
            username = self.validated_data['username'],
            password=self.validated_data['password'],
            is_teacher=self.validated_data['is_teacher'],
            is_student=self.validated_data['is_student'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Password not matched'})
        account.set_password(password)
        account.save()
        return account