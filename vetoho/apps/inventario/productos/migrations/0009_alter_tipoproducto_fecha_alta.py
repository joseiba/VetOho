# Generated by Django 3.2.9 on 2022-09-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_alter_tipoproducto_fecha_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='fecha_alta',
            field=models.CharField(default='28/09/2022 11:32:45 hs', editable=False, max_length=200),
        ),
    ]
