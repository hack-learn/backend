from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from teach_learn.exams.serializers import QuestionModelSerializer

from teach_learn.exams.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """Question view set
    """
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer
