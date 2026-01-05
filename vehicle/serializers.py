from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Car, Moto, Mileage


class MileageSerializer(ModelSerializer):
    class Meta:
        model = Mileage
        fields = "__all__"


class CarSerializer(ModelSerializer):
    last_mileage = serializers.IntegerField(source="mileage_set.all.first.mileage")

    class Meta:
        model = Car
        fields = "__all__"


class MotoSerializer(ModelSerializer):
    last_mileage = serializers.SerializerMethodField()

    def get_last_mileage(self, obj):
        if obj.mileage_set.all().first():
            return obj.mileage_set.all().first().mileage
        return 0

    class Meta:
        model = Moto
        fields = "__all__"
