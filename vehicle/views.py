from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView

from .models import Car, Moto, Mileage
from .serializers import CarSerializer, MotoSerializer, MileageSerializer, MotoMileageSerializer, MotoCreateSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MotoListAPIView(ListAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoUpdateAPIView(UpdateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoCreateAPIView(CreateAPIView):
    serializer_class = MotoCreateSerializer


class MotoRetrieveAPIView(RetrieveAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoDestroyAPIView(DestroyAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MileageCreateAPIView(CreateAPIView):
    serializer_class = MileageSerializer


class MileageListAPIView(ListAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("car", "moto")
    ordering_fields = ("year",)


class MileageMotoListAPIView(ListAPIView):
    queryset = Mileage.objects.filter(moto__isnull=False)
    serializer_class = MotoMileageSerializer
