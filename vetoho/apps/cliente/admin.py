from django.contrib import admin

from vetoho.apps.cliente.models import Cliente, Ciudad

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Cliente)
