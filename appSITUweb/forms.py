from django import forms
from .models import Pasajero

class PasajeroFormulario(forms.ModelForm):
	def clean_cedula(self):
		cedula = self.cleaned_data.get("cedula", "").strip()
		if not cedula.isdigit():
			raise forms.ValidationError("La cédula debe contener solo números.")
		if len(cedula) != 10:
			raise forms.ValidationError("La cédula debe tener exactamente 10 dígitos.")
		queryset = Pasajero.objects.filter(cedula=cedula)
		if self.instance.pk:
			queryset = queryset.exclude(pk=self.instance.pk)
		if queryset.exists():
			raise forms.ValidationError("Ya existe un pasajero con esta cédula.")
		return cedula

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre", "").strip()
		if len(nombre) < 2:
			raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
		return nombre

	def clean_apellido(self):
		apellido = self.cleaned_data.get("apellido", "").strip()
		if len(apellido) < 2:
			raise forms.ValidationError("El apellido debe tener al menos 2 caracteres.")
		return apellido

	class Meta:
		model = Pasajero
		fields=["cedula","nombre","apellido", "email","imagen"] 
		labels = {
			"cedula": "Cédula",
			"nombre": "Nombre",
			"apellido": "Apellido",
			"email": "Correo electrónico",
			"imagen": "Imagen",
		}
		widgets = {
			"cedula": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese la cédula"}),
			"nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el nombre"}),
			"apellido": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el apellido"}),
			"email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ingrese el correo electrónico"}),
			"imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
		}
		#fields = '__all__'


from .models import Tarjeta, Bus, Viaje, SimularAccesoPago


class TarjetaFormulario(forms.ModelForm):
	class Meta:
		model = Tarjeta
		fields = ["codigo", "monto", "idPasajero"]
		labels = {"codigo": "Código", "monto": "Monto", "idPasajero": "Pasajero"}
		widgets = {
			"codigo": forms.TextInput(attrs={"class": "form-control"}),
			"monto": forms.TextInput(attrs={"class": "form-control"}),
			"idPasajero": forms.Select(attrs={"class": "form-control"}),
		}


class BusFormulario(forms.ModelForm):
	class Meta:
		model = Bus
		fields = ["placa", "cooperativa", "numero"]
		labels = {"placa": "Placa", "cooperativa": "Cooperativa", "numero": "Número"}
		widgets = {
			"placa": forms.TextInput(attrs={"class": "form-control"}),
			"cooperativa": forms.TextInput(attrs={"class": "form-control"}),
			"numero": forms.NumberInput(attrs={"class": "form-control"}),
		}


class ViajeFormulario(forms.ModelForm):
	class Meta:
		model = Viaje
		fields = ["pasajero", "bus", "costo", "cantidad", "efectivo", "tipo"]
		widgets = {
			"pasajero": forms.Select(attrs={"class": "form-control"}),
			"bus": forms.Select(attrs={"class": "form-control"}),
			"costo": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
			"cantidad": forms.NumberInput(attrs={"class": "form-control"}),
			"efectivo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
			"tipo": forms.Select(attrs={"class": "form-control"}),
		}


class SimularAccesoPagoFormulario(forms.ModelForm):
	class Meta:
		model = SimularAccesoPago
		fields = ["numero", "viaje", "tarjeta"]
		widgets = {
			"numero": forms.TextInput(attrs={"class": "form-control"}),
			"viaje": forms.Select(attrs={"class": "form-control"}),
			"tarjeta": forms.Select(attrs={"class": "form-control"}),
		}