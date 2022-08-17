from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
import math

from apps.cliente.forms import CiudadForm, ClienteForm
from apps.cliente.models import Ciudad

#Ciudades 
@login_required()
#@permission_required('configuracion.add_confiempresa')
def add_ciudad(request):
    form = CiudadForm
    if request.method == 'POST':
        form = CiudadForm(request.POST or None)
        if form.is_valid():
            messages.success(request, 'Se ha agregado correctamente!')
            form.save()
            return redirect('/configuracion/listCiudades/')
    context = {'form' : form}
    return render(request, 'configuracion/ciudad/add_ciudad_modal.html', context)


@login_required()
#@permission_required('configuracion.change_confiempresa')
def edit_ciudad(request, id):
    ciudad = Ciudad.objects.get(id=id)
    form = CiudadForm(instance=ciudad)
    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)
        if not form.has_changed():
            messages.info(request, "No has hecho ningun cambio!")
            return redirect('/configuracion/listCiudades/')
        if form.is_valid():
            ciudad = form.save(commit=False)
            ciudad.save()
            messages.success(request, 'Se ha editado correctamente!')
            return redirect('/configuracion/listCiudades/')
    context = {'form' : form, 'ciudad': ciudad}
    return render(request, 'configuracion/ciudad/edit_ciudad_modal.html', context)

#@login_required()
#@permission_required('configuracion.view_confiempresa')
def list_ciudades(request):
    return render(request, 'configuracion/ciudad/list_ciudad.html')

#@login_required()
def get_list_ciudades(request):
    query = request.GET.get('busqueda')
    print("viene aca")
    if query != "":
        ciudad = Ciudad.objects.filter(Q(nombre_ciudad__icontains=query))
    else:
        ciudad = Ciudad.objects.all()

    total = ciudad.count()


    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1
        per_page = length

        ciudad = ciudad[start:start + length]

    data = [{'id': c.id, 'nombre': c.nombre_ciudad} for c in ciudad]        

    response = {
        'data': data,
        'recordsTotal': total,
        'recordsFiltered': total,
    }
    return JsonResponse(response)