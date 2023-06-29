from rest_framework import serializers

from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "fio",
            "mail",
            "date_birth",
            "grade",
            "address",
            "floor",
            "photo",
        )

    def create(self, validated_data):
        return super().create(validated_data)


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "fio",
            "mail",
            "date_birth",
            "grade",
            "address",
            "floor",
            "photo",
        )
