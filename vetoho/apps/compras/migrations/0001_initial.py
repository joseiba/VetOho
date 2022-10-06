# Generated by Django 3.1.5 on 2022-09-30 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_factura', models.CharField(max_length=500, null=True)),
                ('nro_timbrado', models.CharField(max_length=500, null=True)),
                ('fecha_alta', models.CharField(default='29/09/2022', max_length=500, null=True)),
                ('fecha_emision_factura', models.CharField(max_length=500, null=True)),
                ('fecha_emision', models.CharField(max_length=500, null=True)),
                ('fecha_vencimiento', models.CharField(max_length=500, null=True)),
                ('tipo_factura', models.BooleanField(default=True)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado'), ('FINALIZADO', 'Finalizado')], default=('PENDIENTE', 'Pendiente'), max_length=500)),
                ('total_iva', models.IntegerField(default=0)),
                ('total', models.FloatField(default=0)),
                ('factura_cargada_producto', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('factura_cargada_pedido', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('pedidod_to_factura', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('facturado', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('factura_caja', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
            ],
            options={
                'verbose_name': 'Factura Compra',
                'verbose_name_plural': 'Facturas Compras',
                'permissions': (('add_facturacompra', 'Agregar Factura Compra'), ('change_facturacompra', 'Editar Factura Compra'), ('delete_facturacompra', 'Eliminar Factura Compra'), ('view_facturacompra', 'Listar Factura Compra')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Plural',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_pedido', models.CharField(blank=True, default='-', max_length=500, null=True)),
                ('fecha_alta', models.CharField(default='29/09/2022 21:38:28 hs', editable=False, max_length=200)),
                ('pedido_cargado', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'permissions': (('add_pedido', 'Agregar Pedido'), ('change_pedido', 'Editar Pedido'), ('delete_pedido', 'Eliminar Pedido'), ('view_pedido', 'Listar Pedido')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PedidoCabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alta', models.CharField(default='29/09/2022', editable=False, max_length=200)),
                ('pedido_cargado', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
            ],
            options={
                'verbose_name': 'Pedido Cabecera',
                'verbose_name_plural': 'Pedido Cabeceras',
                'permissions': (('add_pedidocabecera', 'Agregar Pedido'), ('change_pedidocabecera', 'Editar Pedido'), ('delete_pedidocabecera', 'Eliminar Pedido'), ('view_pedidocabecera', 'Listar Pedido')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(help_text='Ingrese nombre del proveedor', max_length=500)),
                ('direccion', models.CharField(help_text='Ingrese la direccion', max_length=500)),
                ('ruc_proveedor', models.CharField(default='-', help_text='Ingrese el ruc del proveedor', max_length=500)),
                ('telefono', models.CharField(help_text='Ingrese el telefono del proveedor', max_length=500)),
                ('email', models.EmailField(blank=True, default='-', help_text='Ingrese email del proveedor', max_length=500, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.CharField(blank=True, default='S', max_length=2, null=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'permissions': (('add_proveedor', 'Agregar Proveedor'), ('change_proveedor', 'Editar Proveedor'), ('delete_proveedor', 'Eliminar Proveedor'), ('view_proveedor', 'Listar Proveedores')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=800)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('id_pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.pedido')),
                ('id_pedido_cabecera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.pedidocabecera')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
            ],
            options={
                'verbose_name': 'Pedido Detalle',
                'verbose_name_plural': 'Pedido Detalle',
                'permissions': (('add_pedidodetalle', 'Agregar Pedido'), ('change_pedidodetalle', 'Editar Pedido'), ('delete_pedidodetalle', 'Eliminar Pedido'), ('view_pedidodetalle', 'Listar Pedido')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='FacturaDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_compra', models.CharField(blank=True, max_length=800, null=True)),
                ('detalle_cargado_reporte', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('detalle_cargado_mes', models.CharField(blank=True, default='N', max_length=2, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=800)),
                ('id_factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.facturacompra')),
                ('id_pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.pedido')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
            ],
            options={
                'ordering': ['id'],
                'permissions': (('add_facturadet', 'Agregar Factura Compra'), ('change_facturadet', 'Editar Factura Compra'), ('delete_facturadet', 'Eliminar Factura Compra'), ('view_facturadet', 'Listar Factura Compra')),
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='facturacompra',
            name='id_pedido_cabecera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.pedidocabecera'),
        ),
        migrations.AddField(
            model_name='facturacompra',
            name='id_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor'),
        ),
    ]