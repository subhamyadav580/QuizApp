from django.db.models import fields
from rest_framework import serializers

from core.account.models import Account

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'username', 'password'
        ]