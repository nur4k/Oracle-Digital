from django.urls import path

from apps.teacher.views import TeacherView, VerifyEmail

urlpatterns = [
    path("register", TeacherView.as_view()),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify"),
]
