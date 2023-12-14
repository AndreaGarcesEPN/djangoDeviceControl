# En urls.py de la aplicación device_control
from django.urls import path
from .views import AllDevices

urlpatterns = [
    path("", AllDevices.as_view(), name="index"),
    # Otras rutas aquí...
]
