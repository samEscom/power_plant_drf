from rest_framework import serializers

from .models import Device, LuDeviceType, LuStatusDevice, Reading


class LuDeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuDeviceType
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class LuStatusDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuStatusDevice
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            "id",
            "name",
            "current_power",
            "device_type_id",
            "status_device_id",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = (
            "id",
            "device_id",
            "device_type_id",
            "current_power",
            "created_at",
        )
        read_only_fields = (
            "id",
            "created_at",
        )
