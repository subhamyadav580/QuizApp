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
    

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        account = Account.objects.create(
            username = self.validated_data['username'],
            password=self.validated_data['password'],
            is_teacher=self.validated_data['is_teacher'],
            is_student=self.validated_data['is_student'])
        
        account.set_password(validated_data['password'])
        account.save()

        return account