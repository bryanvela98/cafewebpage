from django.db import models

from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        
        return f"{self.nombre} - Descripción: {self.descripcion} - Precio: {self.precio}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        
        return f"Nombre: {self.nombre} - E-mail: {self.email} - Telefono: {self.telefono}"

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    producto = models.ManyToManyField(Producto)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField()
    
    def __str__(self) -> str:
        
        return f"Cliente: {self.cliente} - Producto: {self.producto} - Cantidad: {self.cantidad} - Fecha Pedido: {self.fecha_pedido}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    productos = models.ManyToManyField(Producto)
    
    def __str__(self) -> str:
        
        return f"Nombre: {self.nombre} - Direccion: {self.direccion} - Telefono: {self.telefono} - Productos: {self.productos}"
    
    
class Avatar(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.imagen}"