from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from teach_learn.exams.serializers.exams import ExamModelSerializer


from teach_learn.exams.models import Exam


class ExamViewSet(viewsets.ModelViewSet):
    """User view set
    """
    queryset = Exam.objects.all()
    serializer_class = ExamModelSerializer
