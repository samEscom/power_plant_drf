from rest_framework import serializers

from .models import LuDeviceType


class LuDeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuDeviceType
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)
