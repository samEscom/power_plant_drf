from rest_framework import routers

from .api import LuDeviceTypeViewSet

router = routers.DefaultRouter()
router.register("api/lu-device-type", LuDeviceTypeViewSet, "LuDeviceTYpe")

urlpatterns = router.urls
