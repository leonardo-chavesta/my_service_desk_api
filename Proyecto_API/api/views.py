
from django.views import View
from .models import Productos, Clientes, Usuario
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClientesSerializer, ProductoSerializer, UsuarioSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.

class ProductoView(APIView):
    def get(self, request):
        producto = Productos.objects.all()
        producto_serializer = ProductoSerializer(producto, many=True)

        return Response(producto_serializer.data)

class ClientesView(APIView):

    def get(self, request):
        cliente = Clientes.objects.all()
        cliente_serializer = ClientesSerializer(cliente, many=True)

        return Response(cliente_serializer.data)


class UsuarioView(APIView):

    def get(self, request):
        usuario = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuario, many=True)
        return Response(usuario_serializer.data)
    
    def post(self, request):
        usuario_serializer = UsuarioSerializer(data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)

class UsuarioLoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'usuario': str(request.user),  # `django.contrib.auth.User` instance.
            'autenticación': str(request.auth),  # None
        }
        return Response(content)
