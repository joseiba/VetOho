# Generated by Django 4.0.4 on 2022-09-05 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_emp', models.CharField(max_length=200)),
                ('apellido_emp', models.CharField(max_length=200)),
                ('ci_empe', models.CharField(max_length=200)),
                ('disponible', models.BooleanField(blank=True, default=True, null=True)),
                ('emp_disponible_reserva', models.CharField(blank=True, default='S', max_length=200, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=200, null=True)),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.servicio')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'permissions': (('add_empleado', 'Agregar Empleado'), ('change_empleado', 'Editar Empleado'), ('delete_empleado', 'Eliminar Empleado'), ('view_empleado', 'Listar Empleados')),
                'default_permissions': (),
            },
        ),
    ]