# Generated by Django 4.1.7 on 2023-06-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0009_alter_caja_fecha_alta_alter_caja_fecha_hora_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='fecha_alta',
            field=models.CharField(default='09/06/2023', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='fecha_hora_alta',
            field=models.CharField(default='09/06/2023 21:22:25 hs', max_length=500, null=True),
        ),
    ]
