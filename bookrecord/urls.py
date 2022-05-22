from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountRegistration.as_view(), name='registation')
]
