import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.teacher.models import Teacher
from apps.teacher.serializers import TeacherSerializer, VerifyEmailSerializer


class TeacherView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class VerifyEmail(GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def get(self, request):
        token = request.query_params.get("token", None)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            user = Teacher.objects.get(id=payload["user_id"])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response(
                {"email": "Successfully activated"}, status=status.HTTP_200_OK
            )
        except jwt.ExpiredSignatureError:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
