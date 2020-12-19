from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from teach_learn.exams.serializers import CategoryModelSerializer

from teach_learn.exams.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """Category view set
    """
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
