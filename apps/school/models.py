from django.db import models


class School(models.Model):
    name = models.CharField(verbose_name="Название", max_length=155)
    grades = models.CharField(verbose_name="Классы", max_length=155)

    def __str__(self) -> str:
        return f"{self.name} -- {self.grades}"
