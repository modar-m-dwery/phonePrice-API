from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.get_all_devices),
    path('devices/<int:id>/', views.get_device),
    path('devices/add/', views.add_device),
    path('predict/', views.PredictPrice.as_view(), name='predict-price'),
]
