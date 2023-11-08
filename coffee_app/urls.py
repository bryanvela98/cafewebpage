from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='productos'),
    path('clientes/', views.lista_clientes, name='clientes'),
    path('pedidos/', views.lista_pedidos, name='pedidos'),
    path('proveedores/', views.lista_proveedores, name='proveedores'),
    path('busqueda/', views.resultados_busqueda, name='resultados_busqueda'),
]