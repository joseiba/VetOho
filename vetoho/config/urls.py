"""vetoho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from django.contrib import admin
from django.urls import path
from cgitb import handler
from django.conf.urls.static import static
from config import settings

#urls users
from apps.user.views import home
#urls error page
from apps.handler.views import handler_404, handler_500

#cliente
from apps.cliente.views import (add_ciudad, edit_ciudad, list_ciudades, get_list_ciudades, add_cliente,
edit_cliente, list_client_ajax, list_clientes, delete_cliente)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="index"),

    #cliente urls
    path('configuracion/listCiudades/', list_ciudades , name="list_ciudades"),
    path('configuracion/get_list_ciudades/', get_list_ciudades , name="get_list_ciudades"),
    path('configuracion/addCiudad/',  add_ciudad, name="add_ciudad"),
    path('configuracion/editCiudad/<int:id>/',edit_ciudad , name="edit_ciudad"),
    path('cliente/addCliente/',add_cliente , name="add_cliente"),
    path('cliente/listCliente/', list_clientes, name="list_cliente"),
    path('cliente/get_list_client/', list_client_ajax, name="list_client_ajax"),
    path('cliente/editCliente/<int:id>/', edit_cliente, name="edit_cliente"),
    path('<int:id>', delete_cliente, name="delete_cliente"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404=handler_404
handler500=handler_500