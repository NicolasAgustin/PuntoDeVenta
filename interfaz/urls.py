from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("client/<str:name>", views.client, name="client"),
    path("clients", views.clients, name="clients"),
    path("login", views.login, name="login"),
    path("home", views.home, name="home"),
]
