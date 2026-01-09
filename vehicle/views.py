from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Car, Moto, Mileage
from .serializers import CarSerializer, MotoSerializer, MileageSerializer, MotoMileageSerializer, MotoCreateSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .permissions import IsOwnerOrStaffPermission


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class MotoListAPIView(ListAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoUpdateAPIView(UpdateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    permission_classes = [IsOwnerOrStaffPermission]


class MotoCreateAPIView(CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
