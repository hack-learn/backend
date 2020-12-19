from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated
# from cride.users.permissions import IsAccountOwner

# from cride.users.serializers.profiles import ProfileModelSerializer
# from cride.circles.serializers import CircleModelSerializer
from teach_learn.users.serializers import UserModelSerializer


from teach_learn.users.models import User
# from cride.circles.models import Circle


class UserViewSet(viewsets.ModelViewSet):
    """User view set
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer