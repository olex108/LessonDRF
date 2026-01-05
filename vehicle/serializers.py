from rest_framework.serializers import ModelSerializer
from .models import Car, Moto


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class MotoSerializer(ModelSerializer):
    class Meta:
        model = Moto
        fields = "__all__"