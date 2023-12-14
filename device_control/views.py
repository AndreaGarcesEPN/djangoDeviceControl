# En views.py
from django.views.generic import ListView
from .device_control import openapi
from .models import DeviceControlItem
from django.shortcuts import render
import json  # Agrega la importación de la biblioteca json

class AllDevices(ListView):
    model = DeviceControlItem
    template_name = "device_control/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Realiza la solicitud de estado aquí
        DEVICE_ID = "vdevo170000581142241"
        response = openapi.get(f'/v1.0/iot-03/devices/{DEVICE_ID}/status')

        # Asegúrate de que la respuesta sea un diccionario antes de intentar usar .json()
        if isinstance(response, dict):
            # Convierte el diccionario a cadena JSON para visualización
            context['device_status'] = json.dumps(response, indent=2)
        else:
            # Si no es un diccionario, maneja el caso según la estructura real de la respuesta
            context['device_status'] = "No se pudo obtener el estado del dispositivo"

        return context
