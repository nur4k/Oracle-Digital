from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.teacher.manager import UserManager
from apps.teacher.services import create_token, email_link
from apps.teacher.tasks import send_mail_to_email


class Teacher(AbstractUser):
    username = models.CharField(verbose_name=("Имя пользователя"), max_length=150)
    email = models.EmailField(verbose_name=("Адресс электронной почты"))
    first_name = models.CharField(verbose_name="Имя", max_length=155)
    last_name = models.CharField(verbose_name="Фамилия", max_length=155)
    is_staff = models.BooleanField(verbose_name="Персонал", default=True)
    is_superuser = models.BooleanField(verbose_name="Админ", default=False)

    phone_number = models.CharField(
        verbose_name="Номер телефона", max_length=10, unique=True
    )
    grade = models.CharField(verbose_name="Класс", max_length=50)
    lesson_name = models.CharField(verbose_name="Название предмета", max_length=50)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.phone_number


@receiver(post_save, sender=Teacher)
def my_model_post_save(sender, instance, created, **kwargs):
    if created:
        # Do something when a new instance of Teacher is created
        token = create_token(user_id=instance.id)

        url = email_link(token)

        send_mail_to_email.delay(instance.email, url)
