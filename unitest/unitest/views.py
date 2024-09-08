from .serializers import UserSerializer
from rest_framework import mixins, generics

#mixin - reusable optional actions
#Actions - list, retrieve, update, create

class UserCreateView(mixins.CreateModelMixin):
    