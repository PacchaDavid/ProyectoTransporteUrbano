from django.shortcuts import render
from .forms import PasajeroFormulario
from .models import Pasajero
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import TarjetaFormulario, BusFormulario, ViajeFormulario, SimularAccesoPagoFormulario
from .models import Tarjeta, Bus, Viaje, SimularAccesoPago

# Create your views here.

def home_view(request):
    return render(request,"index.html",{})

def pasajeros(request):
    data = PasajeroFormulario()
    pasajeros = Pasajero.objects.all()
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El pasajero se registró correctamente.")
            return redirect(to="pasajeros")
        else:
            data = formulario

    return render(request,"pasajeros.html",{"pasajeros":pasajeros, 'form':data})

def pasajerosEdit(request, id):
    pasajeros = get_object_or_404(Pasajero, id = id)
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajeros, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El pasajero se actualizó correctamente.")
            return redirect(to="pasajeros")
    else:
        formulario = PasajeroFormulario(instance=pasajeros)

    return render(request,'pasajerosEdit.html',{'form': formulario, 'pasajero': pasajeros})

def pasajerosCrear(request):
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El pasajero se creó correctamente.")
            return redirect(to="pasajeros")
    else:
        formulario = PasajeroFormulario()

    return render(request, 'pasajerosCrear.html', {'form': formulario})

def pasajerosDelete(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    if request.method == 'POST':
        pasajero.delete()
        messages.success(request, "El pasajero se eliminó correctamente.")
        return redirect(to="pasajeros")

    return render(request, 'pasajerosDelete.html', {'pasajero': pasajero})


### Tarjeta views
def tarjetas(request):
    tarjetas = Tarjeta.objects.all()
    return render(request, 'tarjetas.html', {'tarjetas': tarjetas})

def tarjetasCrear(request):
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La tarjeta se creó correctamente.")
            return redirect('tarjetas')
    else:
        formulario = TarjetaFormulario()
    return render(request, 'tarjetasCrear.html', {'form': formulario})

def tarjetasEdit(request, id):
    tarjeta = get_object_or_404(Tarjeta, id=id)
    if request.method == 'POST':
        formulario = TarjetaFormulario(data=request.POST, instance=tarjeta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La tarjeta se actualizó correctamente.")
            return redirect('tarjetas')
    else:
        formulario = TarjetaFormulario(instance=tarjeta)
    return render(request, 'tarjetasEdit.html', {'form': formulario, 'tarjeta': tarjeta})

def tarjetasDelete(request, id):
    tarjeta = get_object_or_404(Tarjeta, id=id)
    if request.method == 'POST':
        tarjeta.delete()
        messages.success(request, "La tarjeta se eliminó correctamente.")
        return redirect('tarjetas')
    return render(request, 'tarjetasDelete.html', {'tarjeta': tarjeta})


### Bus views
def buses(request):
    buses = Bus.objects.all()
    return render(request, 'buses.html', {'buses': buses})

def busesCrear(request):
    if request.method == 'POST':
        formulario = BusFormulario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El bus se creó correctamente.")
            return redirect('buses')
    else:
        formulario = BusFormulario()
    return render(request, 'busesCrear.html', {'form': formulario})

def busesEdit(request, id):
    bus = get_object_or_404(Bus, id=id)
    if request.method == 'POST':
        formulario = BusFormulario(data=request.POST, instance=bus)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El bus se actualizó correctamente.")
            return redirect('buses')
    else:
        formulario = BusFormulario(instance=bus)
    return render(request, 'busesEdit.html', {'form': formulario, 'bus': bus})

def busesDelete(request, id):
    bus = get_object_or_404(Bus, id=id)
    if request.method == 'POST':
        bus.delete()
        messages.success(request, "El bus se eliminó correctamente.")
        return redirect('buses')
    return render(request, 'busesDelete.html', {'bus': bus})


### Viaje views
def viajes(request):
    viajes = Viaje.objects.select_related('pasajero', 'bus').all()
    return render(request, 'viajes.html', {'viajes': viajes})

def viajesCrear(request):
    if request.method == 'POST':
        formulario = ViajeFormulario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El viaje se creó correctamente.")
            return redirect('viajes')
    else:
        formulario = ViajeFormulario()
    return render(request, 'viajesCrear.html', {'form': formulario})

def viajesEdit(request, id):
    viaje = get_object_or_404(Viaje, id=id)
    if request.method == 'POST':
        formulario = ViajeFormulario(data=request.POST, instance=viaje)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El viaje se actualizó correctamente.")
            return redirect('viajes')
    else:
        formulario = ViajeFormulario(instance=viaje)
    return render(request, 'viajesEdit.html', {'form': formulario, 'viaje': viaje})

def viajesDelete(request, id):
    viaje = get_object_or_404(Viaje, id=id)
    if request.method == 'POST':
        viaje.delete()
        messages.success(request, "El viaje se eliminó correctamente.")
        return redirect('viajes')
    return render(request, 'viajesDelete.html', {'viaje': viaje})


### Historial de viajes por pasajero
def historial_pasajero(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    viajes = Viaje.objects.filter(pasajero=pasajero).select_related('bus')
    return render(request, 'historial_pasajero.html', {'pasajero': pasajero, 'viajes': viajes})


### Respaldo a Azure Cosmos DB
def backup_to_cosmos_view(request):
    from django.core.management import call_command
    from io import StringIO
    buf = StringIO()
    try:
        call_command('backup_to_cosmos', stdout=buf)
        messages.success(request, f'Respaldo completado:\n{buf.getvalue()}')
    except Exception as e:
        messages.error(request, f'Error en respaldo: {e}')
    return redirect('home')

### Simular pago
def simular_pago(request):
    if request.method == 'POST':
        formulario = SimularAccesoPagoFormulario(data=request.POST)
        if formulario.is_valid():
            pago = formulario.save()
            messages.success(request, "Pago simulado correctamente.")
            return redirect('simular_pago')
    else:
        formulario = SimularAccesoPagoFormulario()
    return render(request, 'simular_pago.html', {'form': formulario})