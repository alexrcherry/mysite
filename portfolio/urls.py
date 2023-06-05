from django.urls import path, re_path
from . import views

app_name = "portfolio"
urlpatterns = [
    path("", views.main, name="main"),
    path("portfolio/", views.IndexView, name="index"),
]