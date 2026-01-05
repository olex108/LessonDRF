from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Car, Moto, Mileage


class MileageSerializer(ModelSerializer):
    class Meta:
        model = Mileage
        fields = "__all__"


class CarSerializer(ModelSerializer):
    last_mileage = serializers.IntegerField(source="mileage_set.all.first.mileage")
    mileage = MileageSerializer(source="mileage_set", many=True)

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


class MotoMileageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Mileage
        fields = ["mileage", "year", "moto"]


class MotoCreateSerializer(ModelSerializer):
    mileage = MileageSerializer(many=True)

    class Meta:
        model = Moto
        fields = "__all__"

    def create(self, validated_data):
        mileage = validated_data.pop("mileage")

        moto_item = Moto.objects.create(**validated_data)

        for item in mileage:
            Mileage.objects.create(**item, moto=moto_item)

        return moto_item
