# Generated by Django 4.2 on 2023-11-25 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='productos',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='usuarios',
            new_name='usuario',
        ),
    ]
