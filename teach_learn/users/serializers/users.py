from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator

from rest_framework import serializers
from teach_learn.users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        """class Meta"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'linkedin',
            'github',
            'country',
            'city',
            'specialty',
            'english_level',
            'occupation',
        )
