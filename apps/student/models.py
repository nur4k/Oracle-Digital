from django.db import models


class Student(models.Model):
    floor_choices = (("MALE", ("Мужчина")), ("FEMALE", ("Женщина")))

    fio = models.CharField(verbose_name="ФИО", max_length=155)
    mail = models.EmailField(verbose_name="Email", max_length=155, unique=True)
    date_birth = models.DateField(verbose_name="Дата Рождения")
    grade = models.CharField(verbose_name="Класс", max_length=50)
    address = models.CharField(verbose_name="Адрес", max_length=50)
    floor = models.CharField(verbose_name="Пол", choices=floor_choices, max_length=6)
    photo = models.ImageField(
        verbose_name="Фото", upload_to="media/students", blank=True, null=True
    )

    def __str__(self) -> str:
        return self.fio
