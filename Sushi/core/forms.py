from django import forms
from django.forms import ModelForm
from .models import Usuarios, Productos, Pedidos

class ObraForm(ModelForm):


    class Meta:


        model = Usuarios
        fields =['nombre','contraseña','correo','telefono','direccion','tipo']

        model = Pedidos
        fields = ['nombreUsuario','combos','direccion','telefono', 'total']

        model = Productos
        fields = ['id','nombre','porciones','imagenes','descripcion','precio']


     

  