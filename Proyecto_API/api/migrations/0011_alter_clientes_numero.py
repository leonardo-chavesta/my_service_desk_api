# Generated by Django 4.1.2 on 2022-10-27 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_clientes_correo_clientes_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='numero',
            field=models.TextField(max_length=50, null=True),
        ),
    ]