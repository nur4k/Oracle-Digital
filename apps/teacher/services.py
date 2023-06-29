import jwt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response


def email_link(token):
    relativeLink = reverse("email-verify")
    url = "http://" + settings.DOMAIN + relativeLink + "?token=" + str(token)
    return url


def create_token(**kwargs):
    data = {**kwargs}
    try:
        token = jwt.encode(data, settings.SECRET_KEY, algorithm="HS256")
        return token
    except jwt.ExpiredSignatureError:
        return Response({"error": "DecodeError"}, status=status.HTTP_400_BAD_REQUEST)
