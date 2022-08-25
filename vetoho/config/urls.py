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
from django.urls import path, include
from cgitb import handler
from django.conf.urls.static import static
from config import settings

#urls users
from apps.user.views import home
#urls error page
from apps.handler.views import handler_404, handler_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="index"),
    path('tipoProducto/', include(('apps.inventario.productos.urls','tipoproducto'), namespace='tipoproducto')),
    path('deposito/', include(('apps.inventario.depositos.urls','deposito'), namespace='deposito'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404=handler_404
handler500=handler_500