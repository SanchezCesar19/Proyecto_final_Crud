from django.urls import path
from loginapp import views

urlpatterns = [
    path('', views.home),
    path('iniciaste_sesion/',views.loginsesiondef, name='iniciaste_sesion'),
    path('creaste_usuario/',views.regissesiondef, name='registro_sesion')
]