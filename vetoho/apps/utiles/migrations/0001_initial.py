from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timbrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_timbrado', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_inicio_timbrado', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_fin_timbrado', models.CharField(blank=True, max_length=500, null=True)),
                ('vencido', models.CharField(blank=True, default='N', max_length=2, null=True)),
            ],
        ),
    ]
