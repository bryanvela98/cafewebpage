from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.form_productos, name='productos'),
    path('clientes/', views.form_clientes, name='clientes'),
    path('pedidos/', views.form_pedidos, name='pedidos'),
    path('proveedores/', views.form_proveedores, name='proveedores'),
    path('busqueda/', views.resultados_busqueda, name='resultados_busqueda'),
]