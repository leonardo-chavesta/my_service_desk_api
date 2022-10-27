from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoView , ClientesView, UsuarioView 
from .api import UsuarioViewSet, PerfilViewSet, PrioridadViewSet, TecnicoViewSet, ProductoViewSet, ClienteViewSet



router = DefaultRouter()

router.register('usuario', UsuarioViewSet , 'usuario')
router.register('perfil', PerfilViewSet , 'perfil')
router.register('prioridad', PrioridadViewSet , 'prioridad')
router.register('tecnico', TecnicoViewSet , 'tecnico')
router.register('producto', ProductoViewSet , 'producto')
router.register('cliente', ClienteViewSet , 'cliente')

urlpatterns = [
    path('',include(router.urls))
]
