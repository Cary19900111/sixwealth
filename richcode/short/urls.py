from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("basic", views.basic, name="basic"),
    path("daily", views.daily, name="daily"),
    path("deepv", views.deepv_add_two_high, name="deep_v"),
]
