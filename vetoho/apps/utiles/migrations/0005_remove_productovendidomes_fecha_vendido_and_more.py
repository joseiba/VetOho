# Generated by Django 4.1.7 on 2023-06-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utiles', '0004_productovendidomes_fecha_vendido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productovendidomes',
            name='fecha_vendido',
        ),
        migrations.AddField(
            model_name='productovendidomes',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]