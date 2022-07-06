from importlib.machinery import FrozenImporter
from msilib.schema import Class
from django.db import models


# Create your models here.

# USUARIOS / PEDIDOS / ADMINISTRADORES

##############################################
#           USUARIOS            #



#modelo para Obras
        

class Usuarios(models.Model):
    
    nombre = models.CharField(primary_key=True,max_length=20,  verbose_name='Nombre')
    contraseña = models.CharField(max_length=20,  verbose_name='Contraseña')
    correo =models.CharField(max_length=150,verbose_name='Correo')
    telefono = models.CharField(max_length=20, verbose_name='Telefono')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')
    tipo= models.CharField(max_length=50, verbose_name="Tipo usuario")

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    idpedido = models.CharField(primary_key=True, max_length=4, verbose_name='Id Pedido')   
    nombreUsuario = models.CharField(max_length=20, verbose_name='Nombre Usuario')
    combos = models.CharField(max_length=150, verbose_name='CombosPedidos')
    direccion=models.CharField(max_length=150,verbose_name="Direccion")
    telefono=models.CharField(max_length=150,verbose_name="Telefono")
    total=models.CharField(max_length=150,verbose_name="Total")
    def __str__(self):
        return self.nombreUsuario       


class Productos (models.Model):

    nombre = models.CharField(primary_key=True,max_length=20,  verbose_name='Nombre Combo')
    porciones = models.CharField(max_length=20,  verbose_name='Porciones')
    imagen=models.CharField(max_length=150,verbose_name="Nombre archivo imagen")
    descripcion =models.CharField(max_length=150,verbose_name='Descripcion')
    precio = models.CharField(max_length=20, null= True, blank=True, verbose_name='Precio')
    
    def __str__(self):
        return self.nombre
