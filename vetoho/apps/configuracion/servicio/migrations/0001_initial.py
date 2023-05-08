
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(help_text='Ingrese nombre del servicio', max_length=200)),
                ('precio_servicio', models.CharField(help_text='Ingrese el precio del servicio', max_length=200)),
                ('min_serv', models.CharField(max_length=200)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'permissions': (('add_servicio', 'Agregar Servicio'), ('change_servicio', 'Editar Servicio'), ('delete_servicio', 'Eliminar Servicio'), ('view_servicio', 'Listar Servicios')),
                'default_permissions': (),
            },
        ),
    ]
