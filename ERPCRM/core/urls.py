from django.urls import path
from . import views

app_name = "apps"

urlpatterns = [
    path("", views.index, name="index"),
    path("cowsapp/", views.CowApp, name='cow')
]
