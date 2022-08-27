from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
import json
from django.http import JsonResponse

from apps.inventario.productos.forms import TipoProductoForm
from apps.inventario.productos.models import TipoProducto

date = datetime.now()

#Metodo para agregar tipo producto
def add_tipo_producto(request):
    form = TipoProductoForm
    if request.method == 'POST':
        form = TipoProductoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Tipo de producto agregado correctamente!')
            return redirect('/tipoProducto/list')
    context = {'form' : form}
    return render(request, 'inventario/productos/add_tipo_producto.html', context)


# Metodo para editar tipo producto
def edit_tipo_producto(request, id):
    tipo_producto = TipoProducto.objects.get(id=id)
    form = TipoProductoForm(instance=tipo_producto)
    if request.method == 'POST':
        form = TipoProductoForm(request.POST, instance=tipo_producto)
        if not form.has_changed():
            messages.info(request, "No ha hecho ningun cambio")
            return redirect('/tipoProducto/list/')
        if form.is_valid():
            tipo_producto = form.save(commit=False)
            tipo_producto.save()
            messages.add_message(request, messages.SUCCESS, 'Tipo de producto editado correctamente!')
            return redirect('/tipoProducto/list/')

    context = {'form': form, 'tipo_producto':tipo_producto}
    return render(request, 'inventario/productos/add_tipo_producto.html', context)

# Metodo para dar de baja tipo producto
def baja_tipo_producto(request, id):
    try:
        tipo_producto = TipoProducto.objects.get(id=id)
    except TipoProducto.DoesNotExist:
        data = {
            'error':True, 
            'message':"No se encontro el registro."
        }
        return JsonResponse(data, safe=False)
    #try:
    #producto = Producto.objects.get(tipo_producto=id)
    #except:
    producto = None
    if producto is None:
        if tipo_producto.fecha_baja == "-":
            tipo_producto.is_active = "N"
            tipo_producto.fecha_baja = date.strftime("%d/%m/%Y %H:%M:%S hs")
            tipo_producto.save()
            data = {
                'error':False, 
                'message':"Registro eliminado correctamente."
            }
            return JsonResponse(data, safe=False)
        else:
            data = {
                'error':False, 
                'message':"El tipo de producto ya fue dado de baja!"
            }
            return JsonResponse(data, safe=False)
    else:
        data = {
            'error':True, 
            'message':"Este tipo de producto está asociado a productos en stock!"
        }
        return JsonResponse(data, safe=False)


# Metodo para dar de alta tipo producto
def alta_tipo_producto(request, id):
    tipo_producto = TipoProducto.objects.get(id=id)
    if request.method == 'POST':
        if tipo_producto.fecha_baja != "-":
            tipo_producto.is_active = "Y"
            tipo_producto.fecha_baja = '-'
            tipo_producto.save()
            return redirect('/tipoProducto/list/')
        else:
            messages.success(request, 'El tipo de producto ya fue dado de alta!')
            return redirect('/tipoProducto/list/')
    context = {'tipo_producto':tipo_producto}
    return render(request, 'inventario/productos/alta_tipo_producto.html', context)
    

#Metodo para listar todos los tipos de productos
def list_tipo_producto(request):
    return render(request, "inventario/productos/list_tipo_producto.html")


def get_list_tipo_producto(request):
    query = request.GET.get('busqueda')

    if query:
        tipos_productos = TipoProducto.objects.filter(Q(nombre_tipo__icontains=query))
    else:
        tipos_productos = TipoProducto.objects.all()

    total = tipos_productos.count()

    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1
        per_page = length

        tipos_productos = tipos_productos[start:start + length]

    data = [{'id': tp.id, 'nombre_tipo': tp.nombre_tipo, 'fecha_alta': tp.fecha_alta, 'fecha_baja': tp.fecha_baja } for tp in tipos_productos]        

    response = {
        'data': data,
        'recordsTotal': total,
        'recordsFiltered': total,
    }
    return JsonResponse(response) 

#Metodo para la busqueda de tipo de producto
def search_tipo_producto(request):
    query = request.GET.get('q')
    
    paginator = Paginator(tipos_productos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = { 'page_obj': page_obj}
    return render(request, "inventario/productos/list_tipo_producto.html", context)

#Metodo para la busqueda de tipo de producto
def vence_si_no(request):
    tipo_producto = request.GET.get('tipo')
    tipo_producto_vence = TipoProducto.objects.get(id=tipo_producto)

    if tipo_producto_vence.vence == 'S':
        response = {
            'mensaje' : 'S'
        }

        return JsonResponse(response)
    
    response = {
        'mensaje' : 'N'
    }

    return JsonResponse(response)