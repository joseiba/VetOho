# Generated by Django 4.1.7 on 2023-06-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_alter_historicoproductoprecio_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicoproductoprecio',
            name='fecha_alta',
            field=models.CharField(default='09/06/2023', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fecha_alta',
            field=models.CharField(default='09/06/2023 21:22:25 hs', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_compra',
            field=models.CharField(default='09/06/2023', editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='fecha_alta',
            field=models.CharField(default='09/06/2023 21:22:25 hs', editable=False, max_length=200),
        ),
    ]
