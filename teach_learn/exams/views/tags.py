from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from teach_learn.exams.serializers import TagModelSerializer

from teach_learn.exams.models import Tag

class TagsViewSet(viewsets.ModelViewSet):
    """
    Tags view set
    """
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
