from datetime import datetime

from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import Device, LuDeviceType, LuStatusDevice, Reading
from .serializers import (
    DeviceSerializer,
    LuDeviceTypeSerializer,
    LuStatusDeviceSerializer,
    ReadingSerializer,
)


class LuDeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = LuDeviceType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LuDeviceTypeSerializer


class LuStatusDeviceViewSet(viewsets.ModelViewSet):
    queryset = LuStatusDevice.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LuStatusDeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DeviceSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReadingSerializer

    def create(self, request, *args, **kwargs):
        data = ReadingSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        device_id = request.data.get("device_id")
        current_power = request.data.get("current_power")

        try:
            device = Device.objects.get(id=device_id)
            data.save()

            device.current_power = current_power
            device.updated_at = datetime.now()
            device.save(update_fields=["current_power", "updated_at"])

            return Response(data=data.data, status=status.HTTP_201_CREATED)

        except Device.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND, data={"error": "device_id not found"}
            )

        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )
