from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo_vacuna', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='FichaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_create', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ficha Medica',
                'verbose_name_plural': 'Fichas Medicas',
            },
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxima_vacuna', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_aplicacion', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_proxima_aplicacion', models.CharField(blank=True, max_length=500, null=True)),
                ('id_ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.fichamedica')),
                ('id_vacuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_vacuna.tipovacuna')),
            ],
            options={
                'verbose_name': 'Ficha Medica',
                'verbose_name_plural': 'Fichas Medicas',
            },
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(help_text='Ingrese nombre de la mascota', max_length=200)),
                ('tatuaje', models.CharField(blank=True, default='-', help_text='Ingrese el tatuaje', max_length=200, null=True)),
                ('sexo', models.CharField(choices=[('MAC', 'Macho'), ('HEB', 'Hembra')], default='-', help_text='Seleccione el sexo', max_length=15)),
                ('edad', models.CharField(blank=True, default='-', max_length=200, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='Ingrese una foto', null=True, upload_to='mascotas/fotos')),
                ('peso', models.CharField(help_text='Ingrese el peso de la mascota', max_length=200)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('masc_reservado', models.CharField(blank=True, default='S', max_length=200, null=True)),
                ('fecha_reservada', models.CharField(blank=True, max_length=200, null=True)),
                ('hora_reserva', models.CharField(blank=True, max_length=200, null=True)),
                ('color_pelaje', models.CharField(blank=True, default='-', help_text='Ingrese el color de la mascota', max_length=200, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('id_raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.raza')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'permissions': (('add_mascota', 'Agregar Mascota'), ('change_mascota', 'Editar Mascota'), ('delete_mascota', 'Eliminar Mascota'), ('view_mascota', 'Listar Mascotas')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='HistoricoFichaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxima_vacunacion', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('diagnostico', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('tratamiento', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('proximo_tratamiento', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('medicamento', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('fecha_aplicacion', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_proxima_aplicacion', models.CharField(blank=True, max_length=500, null=True)),
                ('antiparasitario', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('proximo_antiparasitario', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('peso', models.CharField(blank=True, default='-', max_length=200, null=True)),
                ('fecha_alta', models.CharField(blank=True, max_length=500, null=True)),
                ('historico_cargado_reporte', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('id_ficha_medica', models.IntegerField(blank=True, null=True)),
                ('id_mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.mascota')),
                ('vacuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_vacuna.tipovacuna')),
            ],
            options={
                'verbose_name': 'Historico Ficha Medicas',
                'verbose_name_plural': 'Historicos Fichas Medicas',
            },
        ),
        migrations.AddField(
            model_name='fichamedica',
            name='id_mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.mascota'),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('tratamiento', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('proximo_tratamiento', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('medicamento', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('id_ficha_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.fichamedica')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Antiparasitario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antiparasitario', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('proximo_antiparasitario', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('id_ficha_medica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.fichamedica')),
            ],
            options={
                'verbose_name': 'Antiparasitario',
                'verbose_name_plural': 'Antiparasitarios',
            },
        ),
    ]
