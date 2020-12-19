from django.conf import settings
from rest_framework import serializers
from teach_learn.exams.models import Answer
# from teach_learn.exams.serializers.questions import QuestionModelSerializer

class AnswerModelSerializer(serializers.ModelSerializer):

    # question = QuestionModelSerializer()

    class Meta:
        """class Meta"""
        model = Answer

        fields = '__all__'
        # ('__all__'
        #     # 'descrition',
        #     # 'question',
        #     # 'is_correct'
        # )
