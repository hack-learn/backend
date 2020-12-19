from django.conf import settings
from rest_framework import serializers
from teach_learn.exams.models import Exam_Result
from teach_learn.users.serializers import UserModelSerializer
from teach_learn.exams.serializers.exams import ExamModelSerializer

class ExamResultModelSerializer(serializers.ModelSerializer):

    user = UserModelSerializer()
    exam = ExamModelSerializer()
    
    class Meta:
        """class Meta"""
        model = Exam_Result
        fields = '__all__'
        # (
        #     'user',
        #     'exam',
        #     'score',
        # )
