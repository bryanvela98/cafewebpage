from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente, Pedido, Proveedor
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

def inicio(request):
    return render(request, 'base.html')

def form_productos(request):
    productos = Producto.objects.all()
    if request.method =='POST':
        formproducto=ProductoForm(request.POST) #aca llega la info al HTML
        
        print(formproducto)
        
        if formproducto.is_valid():
            formproducto.save()  # Guarda los datos del formulario en la base de datos
            return redirect('productos')
    else:
        formproducto=ProductoForm()
        
    return render(request, 'productos.html', {'formproducto': formproducto, 'productos':productos})
        
    

def form_clientes(request):
    clientes = Cliente.objects.all()
    if request.method =='POST':
        formcliente=ClienteForm(request.POST) #aca llega la info al HTML
        
        print(formcliente)
        
        if formcliente.is_valid():
            formcliente.save()  # Guarda los datos del formulario en la base de datos
            return redirect('clientes')
    else:
        formcliente=ClienteForm()
    
    return render(request, 'clientes.html', {'formcliente': formcliente,'clientes':clientes})    
    
def form_pedidos(request):
    pedidos = Pedido.objects.all()
    if request.method =='POST':
        formpedido=PedidoForm(request.POST) #aca llega la info al HTML
        
        print(formpedido)
        
        if formpedido.is_valid():
            formpedido.save()  # Guarda los datos del formulario en la base de datos
            return redirect('pedidos')
    else:
        formpedido=PedidoForm()
    
    return render(request, 'pedidos.html', {'formpedido': formpedido,'pedidos':pedidos})
    

def form_proveedores(request):
    proveedores = Proveedor.objects.all()
    if request.method =='POST':
        formproveedor=ProveedorForm(request.POST) #aca llega la info al HTML
        
        print(formproveedor)
        
        if formproveedor.is_valid():
            formproveedor.save()  # Guarda los datos del formulario en la base de datos
            return redirect('proveedores')
    else:
        formproveedor=ProveedorForm()
        
    return render(request, 'proveedores.html', {'formproveedor': formproveedor,'proveedores':proveedores})
    

def resultados_busqueda(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']  # Asegúrate de usar 'termino_busqueda' en lugar de 'nombre'
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'busqueda.html', {'form': form})

def eliminar_producto(request, producto_id):
    # Obtener el objeto Producto por ID o mostrar una página 404 si no existe
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        # Confirmar la eliminación del producto
        producto.delete()
        return redirect('productos')  # Puedes redirigir a la página de visualización de productos o a donde desees

    # Si no es una solicitud POST, renderizar la plantilla de confirmación de eliminación
    return render(request, 'eliminar_producto.html', {'producto': producto})

def eliminar_cliente(request, cliente_id):
    # Obtener el objeto Producto por ID o mostrar una página 404 si no existe
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        # Confirmar la eliminación del producto
        cliente.delete()
        return redirect('clientes')  # Puedes redirigir a la página de visualización de productos o a donde desees

    # Si no es una solicitud POST, renderizar la plantilla de confirmación de eliminación
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})

def eliminar_pedido(request, pedido_id):
    # Obtener el objeto Producto por ID o mostrar una página 404 si no existe
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    if request.method == 'POST':
        # Confirmar la eliminación del producto
        pedido.delete()
        return redirect('pedidos')  # Puedes redirigir a la página de visualización de productos o a donde desees

    # Si no es una solicitud POST, renderizar la plantilla de confirmación de eliminación
    return render(request, 'eliminar_pedido.html', {'pedido': pedido})

def eliminar_proveedor(request, proveedor_id):
    # Obtener el objeto Producto por ID o mostrar una página 404 si no existe
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

    if request.method == 'POST':
        # Confirmar la eliminación del producto
        proveedor.delete()
        return redirect('proveedores')  # Puedes redirigir a la página de visualización de productos o a donde desees

    # Si no es una solicitud POST, renderizar la plantilla de confirmación de eliminación
    return render(request, 'eliminar_pedido.html', {'proveedor': proveedor})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedidos')
    else:
        form = PedidoForm(instance=pedido)

    return render(request, 'editar_pedido.html', {'form': form, 'pedido': pedido})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, 'Inicio de sesión exitoso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales inválidas. Por favor, inténtelo de nuevo.')
        return super().form_invalid(form)

class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error en el registro. Por favor, inténtelo de nuevo.')
        return super().form_invalid(form)