from rest_framework import routers

from .api import (
    DeviceViewSet,
    LuDeviceTypeViewSet,
    LuStatusDeviceViewSet,
    ReadingViewSet,
)

router = routers.DefaultRouter()
router.register("api/lu-device-type", LuDeviceTypeViewSet, "LuDeviceType")
router.register("api/lu-status-device", LuStatusDeviceViewSet, "LuStatusDevice")
router.register("api/device", DeviceViewSet, "Device")
router.register("api/reading", ReadingViewSet, "Reading")


urlpatterns = router.urls
