from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('depositos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(help_text='Ingrese nombre del producto', max_length=500)),
                ('descripcion', models.CharField(help_text='Ingrese descripcion del producto', max_length=500)),
                ('fecha_vencimiento', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_baja', models.CharField(blank=True, default='-', max_length=200, null=True)),
                ('fecha_movimiento', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_compra', models.CharField(default='27/04/2023', editable=False, max_length=200)),
                ('precio_compra', models.CharField(blank=True, default='0', help_text='Ingrese precio de compra', max_length=500, null=True)),
                ('precio_venta', models.CharField(help_text='Ingrese precio de venta', max_length=500)),
                ('stock_minimo', models.IntegerField(help_text='Ingrese stock minimo')),
                ('lote', models.CharField(blank=True, max_length=200, null=True)),
                ('stock', models.IntegerField(help_text='Ingrese stock minimo')),
                ('iva', models.CharField(choices=[('1', '5%'), ('2', '10%')], help_text='Debe seleccionar el iva', max_length=5)),
                ('stock_total', models.IntegerField(blank=True, null=True)),
                ('stock_movido', models.IntegerField(blank=True, default=0, null=True)),
                ('servicio_o_producto', models.CharField(blank=True, default='P', max_length=2, null=True)),
                ('producto_vencido', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('id_servicio', models.IntegerField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
                ('id_deposito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='depositos.deposito')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(help_text='Ingrese nombre del tipo de producto', max_length=200)),
                ('fecha_alta', models.CharField(default='27/04/2023 20:08:29 hs', editable=False, max_length=200)),
                ('fecha_baja', models.CharField(blank=True, default='-', max_length=200, null=True)),
                ('vence', models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], default='S', help_text='El producto vence?', max_length=2, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
            ],
            options={
                'verbose_name': 'Tipo Producto',
                'verbose_name_plural': 'Tipo Productos',
                'permissions': (('add_tipoproducto', 'Agregar Tipo Producto'), ('change_tipoproducto', 'Editar Tipo Producto'), ('delete_tipoproducto', 'Eliminar Tipo Producto'), ('view_tipoproducto', 'Listar Tipo Productos')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(help_text='Ingrese nombre del producto', max_length=500)),
                ('descripcion', models.CharField(help_text='Ingrese descripcion del producto', max_length=500)),
                ('fecha_vencimiento', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_baja', models.CharField(blank=True, default='-', max_length=200, null=True)),
                ('precio_compra', models.CharField(blank=True, default='0', help_text='Ingrese precio de compra', max_length=500, null=True)),
                ('precio_venta', models.CharField(help_text='Ingrese precio de venta', max_length=500)),
                ('stock_minimo', models.IntegerField(help_text='Ingrese stock minimo')),
                ('lote', models.CharField(blank=True, max_length=200, null=True)),
                ('stock', models.IntegerField(help_text='Ingrese stock minimo')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
                ('tipo_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.tipoproducto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'permissions': (('add_producto', 'Agregar Producto'), ('change_producto', 'Editar Producto'), ('delete_producto', 'Eliminar Producto'), ('view_producto', 'Listar Productos')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProductoStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_stock', models.IntegerField(help_text='Ingrese stock')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
                ('id_deposito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depositos.deposito')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.tipoproducto'),
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_viejo', models.IntegerField(blank=True, default=0, null=True)),
                ('stock_fisico', models.IntegerField(blank=True, default=0, null=True)),
                ('diferencia', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_alta', models.CharField(default='27/04/2023 20:08:29 hs', max_length=500, null=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoProductoPrecio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alta', models.CharField(default='27/04/2023', max_length=500, null=True)),
                ('precio_compra', models.CharField(blank=True, max_length=500, null=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]
