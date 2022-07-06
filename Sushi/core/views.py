from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.db import connection
from core.models import Usuarios
from django.apps import apps
import cx_Oracle




# Create your views here.
def index(request):
    data={
        'producto':lista_productos()
    }
    return render(request,'core/index.html',data) #contenido hacia la vista





    
def login(request):  #login
    data={}
    if request.method == 'POST':
        
        Nombre= request.POST.get('user')
        Contrasenia= request.POST.get('pass')   
        respuesta = log(Nombre,Contrasenia)
        if respuesta=='Admin':
            data['validador'] =1
            return render(request, 'core/login.html',data)
            
        elif respuesta=='Cliente':
            data['validador'] =2
            return render(request, 'core/login.html',data)
        
        else:
            data['validador'] =3
            print('no paso')
    return render(request, 'core/login.html',data)  #enviamos el contenido a la vista

def log(usuario,contrasenia):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    Nombre = cursor.var(cx_Oracle.STRING)

    cursor.callproc("SP_LOGIN",[usuario,contrasenia,Nombre]) 
    
    return Nombre.getvalue()


def registro(request):
    
    data={
        'usuario':lista_usuarios()
    }

    if request.method == 'POST':
        
        Nombre= request.POST.get('nombre')
        Correo= request.POST.get('correo')
        Telefono= request.POST.get('telefono')
        Direccion= request.POST.get('direccion')
        Contrasenia1= request.POST.get('pass1')
        Contrasenia2=request.POST.get('pass2')
        Tipo=request.POST.get('tipo')
        if Contrasenia1==Contrasenia2:
            
            respuesta = crear_usuario(Nombre,Contrasenia1,Correo,Telefono,Direccion,Tipo)
        
            if respuesta== 1:
                data['validador'] =1
            else:  
                data['validador'] =2
        else:
                data['validador'] =3

    return render(request,'core/registro.html',data)

#put crear




def quienes(request):
    return render(request,'core/quienes.html')

def ubicacion(request):
    return render(request,'core/ubicacion.html')

def evento(request):
    return render(request,'core/evento.html')

def indexlog(request):
    data={
        'producto':lista_productos()
    }
    
    
    return render(request,'core/indexlog.html',data) #contenido hacia la vista

# def get_user(nombre):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     resp = cursor.var(cx_Oracle.STRING)

#     cursor.callproc("getuser",[nombre,resp]) 

  
        
#     return resp.getvalue()
    



def quieneslog(request):
    return render(request,'core/quieneslog.html')

def ubicacionlog(request):
    return render(request,'core/ubicacionlog.html')

def eventolog(request):
    return render(request,'core/eventolog.html')    

def dashboard(request):
    data={
        'producto':lista_pedidos()
        
    }
    if request.method == 'POST':
        # boton= request.POST.get('boton')
        idpedido= request.POST.get('idpedido')
        Nombreusuario= request.POST.get('nombreusuario')
        Combos= request.POST.get('combos')
        Direccion= request.POST.get('direccion')
        Telefono= request.POST.get('telefono')
        Total= request.POST.get('total')
        respuesta = crear_pedido(idpedido,Nombreusuario, Combos, Direccion, Telefono, Total)
        if respuesta== 1:
            data['validador'] =1
        else:  
            data['validador'] =2
        

        

    return render(request, 'core/dashboard.html',data)  #enviamos el contenido a la vista

def crear_pedido(idpedido,Nombreusuario, Combos, Direccion, Telefono, Total):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    resp = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_CREAR_PEDIDOS",[idpedido,Nombreusuario, Combos, Direccion, Telefono, Total,resp]) 

    return resp.getvalue()

def lista_pedidos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PEDIDOS",[out_cur]) 

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista

def estadistica(request):
    return render(request, 'core/estadistica.html')


def inventario(request):
    data={
        'producto':lista_productos()
    }
    
    if request.method == 'POST':
        # boton= request.POST.get('boton')
        Nombre= request.POST.get('nombre')
        Porciones= request.POST.get('porciones')
        Imagen= request.POST.get('imagen')
        Descripcion= request.POST.get('descripcion')
        Precio= request.POST.get('precio')
        respuesta = crear_producto(Nombre,Porciones,Imagen,Descripcion,Precio)
        if respuesta== 1:
            data['validador'] =1
        else:  
            data['validador'] =2
        
        # if boton == "Modificar":
        #     resp_mod = modificar_producto(Nombre,Porciones,Imagen,Descripcion,Precio)
        #     if resp_mod == 1:
        #         data['msg'] = 'Producto Modificado'
        #     else:
        #         data['msg'] = 'Error al Modificar producto, Verifica los datos'
        # elif boton == "Eliminar":
        #     resp_del = eliminar_producto(Nombre)
        #     if resp_del == 1:
        #         data['msg'] = 'Producto Eliminado'
        #     else:
        #         data['msg'] = 'Error al Eliminar Producto, Verifica los datos'

    return render(request, 'core/inventario.html',data)  #enviamos el contenido a la vista

# def modificar_producto(Nombre,Porciones,Imagen,Descripcion,Precio):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     respuesta = cursor.var(cx_Oracle.NUMBER)

#     cursor.callproc("SP_MODIFICAR_PRODUCTO",[Nombre,Porciones,Imagen,Descripcion,Precio,respuesta]) 
#     return respuesta.getvalue()

# def eliminar_producto(Nombre):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     respuesta = cursor.var(cx_Oracle.NUMBER)

#     cursor.callproc("SP_ELIMINAR_PRODUCTO",[Nombre,respuesta]) 
#     return respuesta.getvalue()


def crear_producto(Nombre,Porciones,Imagen,Descripcion,Precio):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    resp = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_CREAR_PRODUCTOS",[Nombre,Porciones,Imagen,Descripcion,Precio,resp]) 

    return resp.getvalue()




def lista_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS",[out_cur]) 

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista

def ventas(request):
    return render(request, 'core/ventas.html')    

def logadm(request):
    return render(request, 'core/logadm.html')    

def usuarios(request):
    data={
        'usuario':lista_usuarios()
    }
    if request.method == 'POST':
        
        Nombre= request.POST.get('nombre')
        Contrasenia= request.POST.get('contraseña')
        Correo= request.POST.get('correo')
        Telefono= request.POST.get('telefono')
        Direccion= request.POST.get('direccion')
        respuesta = crear_usuario(Nombre,Contrasenia,Correo,Telefono,Direccion)
        if respuesta== 1:
            data['validador'] =1
        else:  
            data['validador'] =2


    return render(request, 'core/usuarios.html',data)
def crear_usuario(Nombre,Contrasenia,Correo,Telefono,Direccion,Tipo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    resp = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_CREAR_USUARIO",[Nombre,Contrasenia,Correo,Telefono,Direccion,Tipo,resp]) 

    return resp.getvalue()
    
    
def lista_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_USUARIO",[out_cur]) 

    lista = []
    for fila in out_cur:
        lista.append(fila)
        
    return lista


# def repartidores(request):
#     return render(request, 'core/repartidores.html')    
def perfil(request):
    return render(request, 'core/perfil.html')  
# def administradores(request):
#     return render(request, 'core/administradores.html')        


    