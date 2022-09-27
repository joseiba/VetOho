from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from apps.reserva.models import Reserva


# Create your views here.
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