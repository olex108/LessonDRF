from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView

from .models import Car, Moto
from .serializers import CarSerializer, MotoSerializer


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
    serializer_class = MotoSerializer


class MotoRetrieveAPIView(RetrieveAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoDestroyAPIView(DestroyAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
