from django import forms
from .models import Producto, Cliente, Pedido, Proveedor
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100, label='Buscar')
    
class CustomUserChangeForm(UserChangeForm):
    password = None  # Excluir el campo de contraseña

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']