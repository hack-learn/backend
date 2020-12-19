from django.db import models
from django.contrib.auth.models import AbstractUser
from teach_learn.utils.models import BaseModel
from django.core.validators import RegexValidator


class User(BaseModel, AbstractUser):
    """User Model"""

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed. '
    )

    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)

    linkedin = models.URLField(max_length=500)

    github = models.URLField(max_length=500)

    country = models.CharField(max_length=50)

    city = models.CharField(max_length=50)

    specialty = models.CharField(max_length=80)

    english_level = models.CharField(max_length=80)

    occupation = models.CharField(max_length=80)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_student =  models.BooleanField(
        'student',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries, '
            'Student are the main type of user'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

