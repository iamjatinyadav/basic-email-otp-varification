from django.urls import path
from .views import *


urlpatterns = [
    path("register/", RegisterApi.as_view()),
    path("verify/", VerifyOTP.as_view()),
]