from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from teach_learn.exams.serializers import ExamResultModelSerializer

from teach_learn.exams.models import Exam_Result


class ExamResultViewSet(viewsets.ModelViewSet):
    """Exam Results view set
    """
    queryset = Exam_Result.objects.all()
    serializer_class = ExamResultModelSerializer
