# Generated by Django 4.0.4 on 2022-09-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='fecha_alta',
            field=models.CharField(default='04/09/2022 17:35:19 hs', editable=False, max_length=200),
        ),
    ]
