# Generated by Django 4.1.7 on 2023-06-08 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_alter_inventario_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='fecha_alta',
            field=models.CharField(default='07/06/2023 23:00:10 hs', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='fecha_alta',
            field=models.CharField(default='07/06/2023 23:00:10 hs', editable=False, max_length=200),
        ),
    ]
