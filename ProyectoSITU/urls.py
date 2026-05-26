"""ProyectoSITU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from appSITUweb.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('pasajeros/', pasajeros, name='pasajeros'),
    path('pasajerosEdit/<id>', pasajerosEdit, name='pasajerosEdit'),
    path('pasajerosCrear/', pasajerosCrear, name='pasajerosCrear'),
    path('pasajerosDelete/<id>', pasajerosDelete, name='pasajerosDelete'),
    # Tarjetas
    path('tarjetas/', tarjetas, name='tarjetas'),
    path('tarjetasCrear/', tarjetasCrear, name='tarjetasCrear'),
    path('tarjetasEdit/<id>', tarjetasEdit, name='tarjetasEdit'),
    path('tarjetasDelete/<id>', tarjetasDelete, name='tarjetasDelete'),
    # Buses
    path('buses/', buses, name='buses'),
    path('busesCrear/', busesCrear, name='busesCrear'),
    path('busesEdit/<id>', busesEdit, name='busesEdit'),
    path('busesDelete/<id>', busesDelete, name='busesDelete'),
    # Viajes
    path('viajes/', viajes, name='viajes'),
    path('viajesCrear/', viajesCrear, name='viajesCrear'),
    path('viajesEdit/<id>', viajesEdit, name='viajesEdit'),
    path('viajesDelete/<id>', viajesDelete, name='viajesDelete'),
    # Otros
    path('historial/pasajero/<id>', historial_pasajero, name='historial_pasajero'),
    path('simular_pago/', simular_pago, name='simular_pago'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
