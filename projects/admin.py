from django.contrib import admin

from .models import Device, LuDeviceType, LuStatusDevice, Reading

admin.site.register(LuDeviceType)
admin.site.register(LuStatusDevice)
admin.site.register(Device)
admin.site.register(Reading)
