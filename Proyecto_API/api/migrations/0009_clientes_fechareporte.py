# Generated by Django 4.1.2 on 2022-10-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_perfil_descripcionperfil_remove_perfil_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='fechaReporte',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
