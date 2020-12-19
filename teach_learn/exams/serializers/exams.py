from django.conf import settings
from rest_framework import serializers
from teach_learn.exams.models import Exam
from teach_learn.exams.serializers.categories import CategoryModelSerializer
from teach_learn.exams.serializers.questions import QuestionModelSerializer


class ExamModelSerializer(serializers.ModelSerializer):

    category = CategoryModelSerializer(read_only=True)

    questions = QuestionModelSerializer(many=True)
    
    # questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        """class Meta"""
        model = Exam
        fields = '__all__'
        # (
        #     'title',
        #     'description',
        #     'category',
        # )
