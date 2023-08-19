# Generated by Django 4.2 on 2023-08-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_repuesto', models.CharField(max_length=30, verbose_name='nombre del repuesto')),
                ('tipo', models.CharField(max_length=20, verbose_name='tipo de repuesto')),
                ('marca_respuesto', models.CharField(max_length=20, verbose_name='marca')),
            ],
        ),
    ]
