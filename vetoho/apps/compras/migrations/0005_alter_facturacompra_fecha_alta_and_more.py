# Generated by Django 4.1.7 on 2023-06-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_alter_facturacompra_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompra',
            name='fecha_alta',
            field=models.CharField(default='07/06/2023', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_alta',
            field=models.CharField(default='07/06/2023 21:14:43 hs', editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='pedidocabecera',
            name='fecha_alta',
            field=models.CharField(default='07/06/2023', editable=False, max_length=200),
        ),
    ]
