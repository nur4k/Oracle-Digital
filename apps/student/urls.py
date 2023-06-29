from django.urls import path

from apps.student.views import (
    StudentCreateView,
    StudentDeleteView,
    StudentUpdateView,
    StudentView,
)

urlpatterns = [
    path("get/", StudentView.as_view()),
    path("post/<int:pk>/", StudentCreateView.as_view()),
    path("update/<int:pk>/", StudentUpdateView.as_view()),
    path("delete/<int:pk>/", StudentDeleteView.as_view()),
]
