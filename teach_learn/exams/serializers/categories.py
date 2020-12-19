from django.conf import settings
from rest_framework import serializers
from teach_learn.exams.models import Category


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        """class Meta"""
        model = Category
        fields = '__all__'
        
        # (
        #     'title'
        # )
