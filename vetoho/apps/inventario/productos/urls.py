from django.urls import path
from .views import *

urlpatterns = [
    #Urls tipo producto
    path('add/',add_tipo_producto , name="add_tipo_producto"),
    path('list/', list_tipo_producto, name="list_tipo_producto"),
    path('edit/<int:id>/', edit_tipo_producto, name="edit_tipo_producto"),
    path('baja/<int:id>/', baja_tipo_producto, name="baja_tipo_producto"),
    path('alta/<int:id>/', alta_tipo_producto, name="alta_tipo_producto"),
    path('vence_si_no/', vence_si_no, name="vence_si_no"),
    path('get_list_tipo_producto/', get_list_tipo_producto, name="get_list_tipo_producto"),
]