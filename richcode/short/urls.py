from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("basic", views.basic, name="basic"),
    path("daily", views.daily, name="daily"),
    path("month", views.month, name="month"),
    path("deepv", views.deepv_add_two_high, name="deep_v"),
    path("bottomlessvol", views.volumn_donw, name="volumn_donw"),
    path("pricedown50", views.high_price_down_50, name="high_price_down_50"),
    path("fillmonthdata", view=views.fill_omit_month_data, name="fill_omit_month_data"),
]
