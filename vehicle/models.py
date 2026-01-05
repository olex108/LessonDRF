from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "авто"
        verbose_name_plural = "авто"
        ordering = ['title']


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "мотоцикл"
        verbose_name_plural = "мотоциклы"
        ordering = ['title']


class Mileage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Авто", null=True, blank=True)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, verbose_name="Мотоцикл", null=True, blank=True)
    mileage = models.PositiveIntegerField(verbose_name="Пробег")
    year = models.PositiveSmallIntegerField(verbose_name="Год регистрации")

    def __str__(self):
        return f"{self.car}{self.moto} - {self.mileage} - {self.year}"

    class Meta:
        verbose_name = "пробег"
        verbose_name_plural = "пробег"
        ordering = ['-year']