# Generated by Django 3.2.9 on 2022-09-28 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_alter_tipoproducto_fecha_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='fecha_alta',
            field=models.CharField(default='27/09/2022 23:50:42 hs', editable=False, max_length=200),
        ),
    ]
