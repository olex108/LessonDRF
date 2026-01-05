from rest_framework import viewsets

from .models import Car, Moto
from .serializers import CarSerializer, MotoSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
