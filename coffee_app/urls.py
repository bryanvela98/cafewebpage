from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.form_productos, name='productos'),
    path('clientes/', views.form_clientes, name='clientes'),
    path('pedidos/', views.form_pedidos, name='pedidos'),
    path('proveedores/', views.form_proveedores, name='proveedores'),
    path('busqueda/', views.resultados_busqueda, name='resultados_busqueda'),
    path('eliminar/producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar/cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('eliminar/pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('eliminar/proveedor/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('editar_pedido/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('editar_proveedor/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
]