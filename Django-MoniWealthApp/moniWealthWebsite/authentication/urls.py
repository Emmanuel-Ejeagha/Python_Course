from .views import RegistrationVeiw
from django.urls import path


urlpatterns = [
    path('register', RegistrationVeiw.as_view(), name='register')
]