from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    productos = models.ManyToManyField(Producto)