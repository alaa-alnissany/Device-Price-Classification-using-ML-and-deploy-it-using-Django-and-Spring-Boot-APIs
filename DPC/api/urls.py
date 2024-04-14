from django.urls import path 
from . import views


urlpatterns = [
    path('devices', views.get_all_devices),
    path('devices/<int:device_id>/', views.get_device_details),
    path('adddevices', views.add_device),
    path('predict/<int:device_id>/', views.predict_device_price),
    ]