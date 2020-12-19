from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from teach_learn.users.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name',
                    'last_name', 'is_staff', 'is_student')
    list_filter = ('is_student', 'is_staff', 'created', 'modified')

admin.site.register(User, CustomUserAdmin)
