from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView
from . import views
from .views import CustomRegisterView

#para las imagenes
from django.conf import settings
from django.conf.urls.static import static

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
    #login y logout
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #registro
    path('register/', CustomRegisterView.as_view(), name='register'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)