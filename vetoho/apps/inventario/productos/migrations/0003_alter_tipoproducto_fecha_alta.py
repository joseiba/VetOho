# Generated by Django 4.1.7 on 2023-04-17 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_tipoproducto_fecha_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='fecha_alta',
            field=models.CharField(default='17/04/2023 19:53:01 hs', editable=False, max_length=200),
        ),
    ]
