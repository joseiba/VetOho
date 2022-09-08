# Generated by Django 3.2.9 on 2022-09-07 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especie', models.CharField(help_text='Ingrese el nombre de la Especie', max_length=200)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Especie',
                'verbose_name_plural': 'Especies',
                'permissions': (('add_especie', 'Agregar Especie'), ('change_especie', 'Editar Especie'), ('delete_especie', 'Eliminar Especie'), ('view_especie', 'Listar Especies')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_raza', models.CharField(help_text='Ingrese el nombre de la Raza', max_length=200)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('id_especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.especie')),
            ],
            options={
                'verbose_name': 'Raza',
                'verbose_name_plural': 'Razas',
                'permissions': (('add_raza', 'Agregar Raza'), ('change_raza', 'Editar Raza'), ('delete_raza', 'Eliminar Raza'), ('view_raza', 'Listar Razas')),
                'default_permissions': (),
            },
        ),
    ]
