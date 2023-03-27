from django.urls import path
from almacenes_sans import views

urlpatterns = [
    path('', views.home,name='gestionproducto'),
    path('registrar_proovedor/', views.registroproveedor,name='registro_proovedor'),
    path('registrar_producto/', views.registroproducto,name='registro_producto'),
    path('eliminar_proveedor/<int:id>/', views.eliminarproveedor, name='eliminar_proveedor'),
    path('eliminar_producto/<int:id>/', views.eliminarproducto, name='eliminar_producto'),
    #edicion proveedor
    path('editar_proveedor/<int:id>/', views.editarproveedor, name='editar_proveedor'),
    path('proveedor_editado/', views.guardaredicioproveedor, name='proveedor_editado'),
    #edicion producto
    path('editar_producto/<int:id>/', views.editarproducto, name='editar_producto'),
    path('producto_editado/', views.guardaredicioproducto, name='producto_editado'),
]