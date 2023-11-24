from django.contrib import admin
from coffee_app import models

# Register your models here.

admin.site.register(models.Producto)

admin.site.register(models.Pedido)

admin.site.register(models.Cliente)

admin.site.register(models.Proveedor)

admin.site.register(models.Avatar)