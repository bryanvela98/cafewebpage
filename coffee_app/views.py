from django.shortcuts import render
from .models import Producto, Cliente, Pedido, Proveedor
from .forms import *

def inicio(request):
    return render(request, 'base.html')

def form_productos(request):
    productos = Producto.objects.all()
    if request.method =='POST':
        formproducto=ProductoForm(request.POST) #aca llega la info al HTML
        
        print(formproducto)
        
        if formproducto.is_valid():
            formproducto.save()  # Guarda los datos del formulario en la base de datos
            return render(request, 'base.html')
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
            return render(request, 'base.html')
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
            return render(request, 'base.html')
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
            return render(request, 'base.html')
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
