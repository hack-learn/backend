from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from teach_learn.users.serializers.users import UserModelSerializer


from teach_learn.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """User view set
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer