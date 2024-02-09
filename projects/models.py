from datetime import datetime

from django.db import models

# Create your models here.


class LuDeviceType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class LuStatusDevice(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    current_power = models.FloatField()
    device_type_id = models.ForeignKey(LuDeviceType, on_delete=models.CASCADE)
    status_device_id = models.ForeignKey(LuStatusDevice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False, null=False)
    updated_at = models.DateTimeField(default=None, blank=True, null=True)


class Reading(models.Model):
    id = models.IntegerField(primary_key=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    device_type_id = models.ForeignKey(LuDeviceType, on_delete=models.CASCADE)
    current_power = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now, blank=False, null=False)
