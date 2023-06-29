from rest_framework import serializers

from apps.teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "password",
            "grade",
            "lesson_name",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        teacher = Teacher(**validated_data)
        teacher.set_password(password)
        teacher.save()
        return teacher


class VerifyEmailSerializer(serializers.Serializer):
    ...
