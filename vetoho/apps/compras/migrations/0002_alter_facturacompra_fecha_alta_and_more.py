# Generated by Django 4.1.7 on 2023-05-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacompra',
            name='fecha_alta',
            field=models.CharField(default='15/05/2023', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_alta',
            field=models.CharField(default='15/05/2023 19:23:19 hs', editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='pedidocabecera',
            name='fecha_alta',
            field=models.CharField(default='15/05/2023', editable=False, max_length=200),
        ),
    ]
