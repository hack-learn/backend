"""Exam Admin Configuration."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.answers import Answer
from .models.categories import Category
from .models.exams_results import Exam_Result
from .models.exams import Exam
from .models.questions import Question
from .models.tags import Tag

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Answer admin configs.
    """

    # List of element can display on admin
    list_display = (
        'question',
        'descrition',
        'is_correct',
    )

    # Some filters and configurations
    date_hierarchy = 'created'
    list_filter = ['question']
    search_fields = ['question__title']
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin configs.
    """

    # List of element can display on admin
    list_display = (
        'title',
    )

    # Some filters and configurations
    date_hierarchy = 'created'


@admin.register(Exam_Result)
class ExamResultAdmin(admin.ModelAdmin):
    """Category admin configs.
    """

    # List of element can display on admin
    list_display = (
        'user',
        'exam',
        'score',
    )

    # Some filters and configurations
    date_hierarchy = 'created'
    
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    """Category admin configs.
    """

    # List of element can display on admin
    list_display = (
        'title',
        'description',
        'category',
    )

    # Some filters and configurations
    date_hierarchy = 'created'
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Category admin configs.
    """

    # List of element can display on admin
    list_display = (
        'title',
        'description',
        'component',
        'difficulty',
        'tag',
    )

    # Some filters and configurations
    date_hierarchy = 'created'
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Category admin configs.
    """

    # List of element can display on admin
    list_display = (
        'title',
        'description',
        'category',
    )

    # Some filters and configurations
    date_hierarchy = 'created'
    


# class CustomUserAdmin(UserAdmin):
#     """Configuration for Kumpel model.

#     User admin configs.
#     """

#     list_display = (
#         'email',
#         'username',
#         'first_name',
#         'phone_number',
#         'last_name',
#         'is_staff',
#         'is_verified',
#     )

#     list_filter = ('is_verified', 'is_staff', 'created', 'modified')

#     # Some filters and configurations
#     date_hierarchy = 'created'
#     search_fields = ['user']
#     list_per_page = 10


# class GenreAdmin(admin.ModelAdmin):
#     """Configuration for kumpel model.

#     Genre admin configs.
#     """

#     list_display = ('name',)
#     list_filter = ('name', 'created', 'modified')
#     date_hierarchy = 'created'
#     list_per_page = 10


# class HobbyAdmin(admin.ModelAdmin):
#     """Configuration for kumpel model.

#     Hobby admin configs.
#     """

#     list_display = ('name', 'description')
#     date_hierarchy = 'created'
#     list_per_page = 10


# class InterestAdmin(admin.ModelAdmin):
#     """Configuration for kumpel model.

#     Interest admin configs.
#     """

#     list_display = ('name', 'description')
#     date_hierarchy = 'created'
#     list_per_page = 10


# # Register models and configurations
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Genre, GenreAdmin)
# admin.site.register(Hobby, HobbyAdmin)
# admin.site.register(Interest, InterestAdmin)
