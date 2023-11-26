# Generated by Django 4.2 on 2023-11-25 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0002_alter_producto_options_alter_producto_precio'),
        ('usuarios', '0005_delete_arl_remove_usuario_rol_usuario_direccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaVenta', models.DateField(max_length=12, verbose_name='Fecha Venta')),
                ('totalVenta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('productos', models.ManyToManyField(through='ventas.DetalleVenta', to='productos.producto')),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta'),
        ),
    ]
