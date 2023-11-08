from django import forms
from .models import Producto, Cliente, Pedido, Proveedor

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