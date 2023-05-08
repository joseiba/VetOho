from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(help_text='Ingrese nombre de la ciudad', max_length=200)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'permissions': (('add_ciudad', 'Agregar Ciudad'), ('change_ciudad', 'Editar Ciudad'), ('delete_ciudad', 'Eliminar Ciudad'), ('view_ciudad', 'Listar Ciudades')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(help_text='Ingrese nombre del cliente', max_length=200)),
                ('apellido_cliente', models.CharField(help_text='Ingrese apellido del cliente', max_length=200)),
                ('direccion', models.CharField(help_text='Ingrese apellido del cliente', max_length=200)),
                ('cedula', models.CharField(help_text='Ingrese cedula del cliente', max_length=200)),
                ('ruc', models.CharField(blank=True, help_text='Ingrese ruc del cliente', max_length=200, null=True)),
                ('telefono', models.CharField(help_text='Ingrese telefono del cliente', max_length=200)),
                ('email', models.EmailField(blank=True, help_text='Ingrese email del cliente', max_length=200, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
                ('id_ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.ciudad')),
            ],
            options={
                'ordering': ['last_modified'],
                'permissions': (('add_cliente', 'Agregar Cliente'), ('change_cliente', 'Editar Cliente'), ('delete_cliente', 'Eliminar Cliente'), ('view_cliente', 'Listar Clientes')),
                'default_permissions': (),
            },
        ),
    ]
