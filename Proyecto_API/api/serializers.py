from dataclasses import field
from pyexpat import model
from .models import Clientes, Productos, TecnicoAsignado, PrioridadIncidencia, Perfil, Usuario
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        exclude = ()

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TecnicoAsignado
        exclude =()

class PrioridadIncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrioridadIncidencia
        exclude =()

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Perfil
        exclude =()

class ClientesSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    tecnico = TecnicoSerializer(read_only=True)
    prioridad = PrioridadIncidenciaSerializer(read_only=True)

    producto_Id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Productos.objects.all(), source='producto')
    tecnico_Id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TecnicoAsignado.objects.all(), source='tecnico')
    prioridad_Id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=PrioridadIncidencia.objects.all(), source='prioridad')
    class Meta:
        model= Clientes
        fields =('id', 'nombre', 'reporte', 'fechaReporte','correo' , 'numero' ,'producto', 'tecnico', 'prioridad', 'producto_Id', 'prioridad_Id', 'tecnico_Id')
        read_only_fields = ()

class UsuarioSerializer(serializers.ModelSerializer):
    perfil=PerfilSerializer(read_only=True)
    perfil_Id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Perfil.objects.all(), source='perfil')
    class Meta:
        model= Usuario
        fields =('id', 'correo', 'clave', 'perfil' , 'perfil_Id', 'nombre')
        read_only_fields = ()


    
