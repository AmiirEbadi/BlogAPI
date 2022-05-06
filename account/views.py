import imp
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from serializer.serializers import (
    UserSerializer
)
from permission.permissions import (
    IsOwnerOrAdminOrReadonly
)
from rest_framework.permissions import (
    AllowAny,
)

class UserListAPI(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]


class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsOwnerOrAdminOrReadonly]