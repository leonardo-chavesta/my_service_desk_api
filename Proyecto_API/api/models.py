from django.db import models


class Perfil(models.Model):
    etiqueta = models.CharField(max_length=50, null=True)
    # descripcionPerfil = models.TextField(max_length=200, null=True)
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        db_table = 'perfil'
    def __str__(self):
        return self.etiqueta

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    correo = models.EmailField(max_length=200)
    clave = models.CharField(max_length=50)
    perfil=models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario' 
           

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion =  models.TextField(max_length=200, null=True)
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
    def __str__(self):
        return self.nombre

class PrioridadIncidencia(models.Model):
    estado = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'
        db_table = 'prioridad'
    def __str__(self):
        return self.estado


class TecnicoAsignado(models.Model):
    nombre = models.CharField(max_length=50)
    incidenciaAsigandas = models.IntegerField()
    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        db_table = 'tecnico'
    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    reporte = models.TextField(max_length=200)
    correo = models.EmailField(blank=False, unique=True, null=True,)
    numero = models.TextField(max_length=50, blank=False, null=True,)
    producto = models.ForeignKey(Productos, null=True, blank=True, on_delete=models.PROTECT)
    tecnico = models.ForeignKey(TecnicoAsignado,  null=True, blank=True, on_delete=models.PROTECT)
    prioridad = models.ForeignKey(PrioridadIncidencia, null=True, blank=True, on_delete=models.PROTECT)
    fechaReporte = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'