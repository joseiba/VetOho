from django import forms

from apps.inventario.productos.models import TipoProducto

class TipoProductoForm(forms.ModelForm):
    """[summary]
    Args:
        forms ([TipoProductoForm]): [Formulario de tipo de producto]
    """    
    class Meta:
        model = TipoProducto
        exclude = ['is_active']
        labels = {
            'nombre_tipo' : 'Nombre',
            'vence' : 'Vence'
        }
        widgets = {
            'nombre_tipo' : forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off','name': 'nombre_tipo', 'placeholder': 'Nombre Tipo Producto', 'required': 'required', 'onkeyup':'aceptarLetras(this)'}),
            'vence' : forms.Select(attrs={'class':'form-control', 'id': 'vence','required':'required' ,'name':'vence'}),
			'fecha_alta' : forms.TextInput(attrs={'class':'form-control','type':'datetime',
            'name': 'fecha_alta', 'placeholder': 'Fecha de Alta', 'readonly': 'readonly'}),
		    'fecha_baja' : forms.TextInput(attrs={'class':'form-control','type':'datetime', 'name': 'fecha_baja', 
            'placeholder': 'Fecha de Baja', 'readonly': 'readonly'}),
		}