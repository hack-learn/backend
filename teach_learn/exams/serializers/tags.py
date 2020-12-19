from django.conf import settings
from rest_framework import serializers
from teach_learn.exams.models import Tag
from teach_learn.exams.serializers.categories import CategoryModelSerializer

class TagModelSerializer(serializers.ModelSerializer):

    category = CategoryModelSerializer()

    class Meta:
        """class Meta"""
        model = Tag
        fields = '__all__'
        # (
        #     'title',
        #     'description',
        #     'category',
        # )
