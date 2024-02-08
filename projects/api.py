from rest_framework import permissions, viewsets

from .models import LuDeviceType
from .serializers import LuDeviceTypeSerializer


class LuDeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = LuDeviceType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LuDeviceTypeSerializer
