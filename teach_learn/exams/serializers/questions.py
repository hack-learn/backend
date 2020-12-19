from django.conf import settings
from rest_framework import serializers
from teach_learn.exams.models import Question
from teach_learn.exams.serializers.answers import AnswerModelSerializer


class QuestionModelSerializer(serializers.ModelSerializer):

    answers = AnswerModelSerializer(many=True)

    class Meta:
        """class Meta"""
        model = Question
        fields = '__all__'
