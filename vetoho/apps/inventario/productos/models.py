from django.db import models
from datetime import datetime

# Create your models here.
date = datetime.now()
class TipoProducto(models.Model):
    """
    Clase que define la estructura de un tipo de producto
    """
    opciones = (
        ('S', 'Si'),
        ('N', 'No'),
    )

    nombre_tipo = models.CharField(max_length = 200, help_text = "Ingrese nombre del tipo de producto")
    fecha_alta = models.CharField(max_length = 200, default = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S hs"), editable = False)
    fecha_baja = models.CharField(max_length = 200, default = '-', null = True, blank = True)
    vence = models.CharField(max_length=2, choices=opciones, default="S", blank=True, null=True, help_text='El producto vence?')
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    is_active = models.CharField(max_length=2, default="S", blank=True, null=True)

    class Mwta:
        verbose_name = "Tipo Producto"
        verbose_name_plural = "Tipo Productos"
        default_permissions =  ()
        permissions = (
            ('add_tipoproducto', 'Agregar Tipo Producto'),
            ('change_tipoproducto', 'Editar Tipo Producto'),
            ('delete_tipoproducto', 'Eliminar Tipo Producto'),
            ('view_tipoproducto', 'Listar Tipo Productos'))

    def __str__(self):
        """Formato del tipo producto"""
        return '{0}'.format(self.nombre_tipo)

    def get_absolute_url(self):
        """Retorna el URL para acceder a una instancia de un tipo de producto en particular."""
        return reverse('tipoProducto-detail', args=[str(self.id)])