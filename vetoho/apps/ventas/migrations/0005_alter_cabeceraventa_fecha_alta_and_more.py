# Generated by Django 4.1.7 on 2023-06-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_alter_cabeceraventa_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabeceraventa',
            name='fecha_alta',
            field=models.CharField(default='07/06/2023', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cabeceraventa',
            name='fecha_emision',
            field=models.CharField(default='07/06/2023 21:14:43 hs', max_length=500, null=True),
        ),
    ]
