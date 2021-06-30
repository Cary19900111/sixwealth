from django.urls import path

from . import views

urlpatterns = [
    path("", views.test, name="test"),
    path("basic", views.basic, name="basic"),
    path("daily", views.daily, name="daily"),
]
