# Generated by Django 4.1.2 on 2022-10-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_clientes_prioridad_alter_clientes_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='descripcionPerfil',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]