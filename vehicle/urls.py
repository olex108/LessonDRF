from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import (CarViewSet, MotoListAPIView, MotoCreateAPIView, MotoUpdateAPIView, MotoDestroyAPIView,
                           MotoRetrieveAPIView)

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path("moto/", MotoListAPIView.as_view(), name="moto_list"),
    path("moto/<int:pk>/", MotoRetrieveAPIView.as_view(), name="moto_details"),
    path("moto/create/", MotoCreateAPIView.as_view(), name="moto_create"),
    path("moto/<int:pk>/update/", MotoUpdateAPIView.as_view(), name="moto_update"),
    path("moto/<int:pk>/delete/", MotoDestroyAPIView.as_view(), name="moto_delete"),
] + router.urls