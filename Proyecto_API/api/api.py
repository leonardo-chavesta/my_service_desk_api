import django
from .models import Usuario , Perfil, Clientes, TecnicoAsignado, PrioridadIncidencia, Productos
from rest_framework import  viewsets, permissions
from rest_framework.response import Response
from .serializers import UsuarioSerializer , PerfilSerializer, PrioridadIncidenciaSerializer, TecnicoSerializer, ProductoSerializer, ClientesSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PerfilSerializer

class PrioridadViewSet(viewsets.ModelViewSet):
    queryset = PrioridadIncidencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PrioridadIncidenciaSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = TecnicoAsignado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientesSerializer
  

