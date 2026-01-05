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