from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabeceraventa',
            name='fecha_alta',
            field=models.CharField(default='25/03/2023', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cabeceraventa',
            name='fecha_emision',
            field=models.CharField(default='25/03/2023 11:53:07 hs', max_length=500, null=True),
        ),
    ]
