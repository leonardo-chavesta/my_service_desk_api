# Generated by Django 4.1.2 on 2022-10-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'db_table': 'perfil',
            },
        ),
        migrations.CreateModel(
            name='PrioridadIncidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Prioridad',
                'verbose_name_plural': 'Prioridades',
                'db_table': 'prioridad',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='TecnicoAsignado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('incidenciaAsigandas', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnicos',
                'db_table': 'tecnico',
            },
        ),
    ]
