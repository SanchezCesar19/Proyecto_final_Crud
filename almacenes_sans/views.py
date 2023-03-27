from django.db.models import Q
from django.shortcuts import render, redirect
from almacenes_sans.models import producto,proveedor
from django.contrib import messages
# Create your views here.
def home(request):
    proveedores = proveedor.objects.all()
    messages.success(request, '¡Provedores listados!')
    productos = producto.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, "gestionproducto.html", {"proveedores":proveedores,
                                                    "productos": productos
                                                    })
def registroproveedor(request):
    proveid= request.POST['txtid']
    provenom= request.POST['txtNombre']
    provedire= request.POST['txtdire']
    provetelef= request.POST['txtele']

    proovedores = proveedor.objects.create(id=proveid,
                                           nombre=provenom,
                                           direccion=provedire,
                                           telefono=provetelef)
    messages.success(request, '¡Provedor Registrado!')
    return redirect('gestion_producto')

def registroproducto(request):
    producid= request.POST['txtidpro']
    producnombre= request.POST['txtNombrepro']
    producdescri= request.POST['txtdescrippro']
    producprecio= request.POST['txtpreciopro']
    produccatego= request.POST['txtcategopro']
    producfabric= request.POST['txtfabripro']
    proveeid = request.POST['txtidproovee']
    productos = producto.objects.create(id=producid,
                                          nombre=producnombre,
                                          descripcion=producdescri,
                                          precio=producprecio,
                                          categoria=produccatego,
                                          fabricante=producfabric,
                                        proveedor_id=proveeid)
    messages.success(request, '¡Producto Registrado!')
    return redirect('gestion_producto')


def eliminarproveedor(request,id):
    proves = proveedor.objects.get(id=id)
    proves.delete()
    messages.success(request, '¡Provedor Eliminado!')
    return redirect('gestion_producto')

def eliminarproducto(request,id):
    proves = producto.objects.get(id=id)
    proves.delete()
    messages.success(request, '¡Producto Eliminado!')
    return redirect('gestion_producto')

def editarproveedor(request,id):
    proves = proveedor.objects.get(id=id)
    return render(request,"edicionproveedor.html",{"editprove":proves})

def guardaredicioproveedor(request):
    proveid = request.POST['txtid']
    provenom= request.POST['txtNombre']
    provedire= request.POST['txtdire']
    provetelef= request.POST['txtele']

    proves = proveedor.objects.get(id=proveid)
    proves.nombre = provenom
    proves.direccion = provedire
    proves.telefono = provetelef
    proves.save()
    messages.success(request, '¡Provedor Actualizados!')

    return redirect('gestion_producto')

def editarproducto(request,id):
    producs = producto.objects.get(id=id)
    return render(request,"edicionproducto.html",{"editproduc":producs})

def guardaredicioproducto(request):
    produid = request.POST['txtidpro']
    produnom= request.POST['txtNombrepro']
    produdesc= request.POST['txtdescrippro']
    produprecio= request.POST['txtpreciopro']
    producatego= request.POST['txtcategopro']
    produfari= request.POST['txtfabripro']

    produc = producto.objects.get(id=produid)
    produc.nombre = produnom
    produc.direccion = produdesc
    produc.precio = produprecio
    produc.categoria = producatego
    produc.fabricante = produfari
    produc.save()
    messages.success(request, '¡Producto Actualizado!')

    return redirect('gestion_producto')
