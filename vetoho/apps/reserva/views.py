import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import JsonResponse


from datetime import time, datetime, date

from apps.reserva.models import Reserva
from apps.reserva.forms import ReservaForm
from apps.configuracion.empleado.models import Empleado
from apps.configuracion.servicio.models import Servicio
from apps.configuracion.servicio.forms import ServicioForm

hora_entrada = "08:00"
hora_salida_lun_vie = "18:00"
hora_salida_sab = "15:00"
today = date.today()
# Create your views here.
@login_required()
@permission_required('reserva.add_reserva')
def add_reserva(request):
    form = ReservaForm
    servicios = Servicio.objects.exclude(is_active="N").order_by('-last_modified')
    if request.method == 'POST':
        form = ReservaForm(request.POST) 
        if form.is_valid():           
            form.save()            
            messages.success(request, 'Se ha agregado correctamente!')
            try:
                emp = Empleado.objects.get(id=request.POST.get('id_empleado'))
                emp.emp_disponible_reserva = 'N'
                emp.save()
                # masc = Mascota.objects.get(id=request.POST.get('id_mascota'))
                # masc.masc_reservado = 'N'
                # masc.fecha_reservada = request.POST.get('fecha_reserva')
                # masc.hora_reserva = request.POST.get('hora_reserva')
                # masc.save()
            except Exception as e:
                pass
            return redirect('/reserva/listReserva/')
    context = {'form' : form}
    return render(request, 'reserva/add_reserva_modal.html', context)

@login_required()
@permission_required('reserva.view_reserva')
def list_reserva(request):
    data = []
    # reserva = Reserva.objects.all()
    # fechaDate = date(today.year, today.month, today.day)
    # for r in reserva:
    #     if r.fecha_reserva is not None:
    #         if fechaDate > r.fecha_reserva:
    #             if r.estado_re == 'PEN':
    #                 r.estado_re = 'FIN'
    #                 r.disponible_emp = "S"
    #                 r.color_estado = "green"
    #                 try:
    #                     masc = Mascota.objects.get(id=r.id_mascota.id)
    #                     masc.masc_reservado = "S"
    #                     masc.fecha_reservada = ""
    #                     masc.hora_reserva = ""
    #                     masc.save()
    #                 except:
    #                     pass
    #                 r.save()                                                     
    # paginator = Paginator(reserva, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # context = {'page_obj' : page_obj}
    return render(request, "reserva/list_reserva.html")


def get_min_service(request):
    servicio = request.GET.get('servicio')
    emp = Empleado.objects.filter(id_servicio=servicio)
    listEmpleado = [{'id': empleado.id, 'nombre': empleado.nombre_emp + " " + empleado.apellido_emp} for empleado in emp]

    listJsonEmpleado= json.dumps(listEmpleado)
    isFalse = True
    try:
        minService = Servicio.objects.get(id=servicio)
    except:
        isFalse = False
    if isFalse:
        response = { 'tiempo': minService.min_serv, 'mensaje': "Ok", 'empleado': listJsonEmpleado}
        return JsonResponse(response)
    response = { 'tiempo': minService.min_serv, 'mensaje': "", 'empleado': listJsonEmpleado}       
    return JsonResponse(response)