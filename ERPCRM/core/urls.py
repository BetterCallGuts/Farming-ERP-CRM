from django.urls import path
from . import views

app_name = "apps"

urlpatterns = [
    path("", views.index, name="index"),

    path("<str:app>/<str:page>/<int:stat>/", views.CowApp, name='app'),
]
