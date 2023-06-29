from django.db import models

from apps.student.models import Student
from apps.teacher.models import Teacher


class Grade(models.Model):
    name = models.CharField(verbose_name="Название", max_length=155)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name="Учитель",
        related_name="teacher_grade",
    )
    students = models.ManyToManyField(Student, related_name="student_grade")

    def __str__(self) -> str:
        return self.name
