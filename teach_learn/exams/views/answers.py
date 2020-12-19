from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from teach_learn.exams.serializers import AnswerModelSerializer

from teach_learn.exams.models import Answer

class AnswerViewSet(viewsets.ModelViewSet):
    """Answer view set
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer
