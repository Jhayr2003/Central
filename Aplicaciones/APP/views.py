from django.shortcuts import render,redirect

from typing import Any
from django.db.models.query import QuerySet
from .models import *
from django.views.generic import ListView
from django.template import *
from .models import Usuario
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

#CLASE PROMOCION
class PromocionListView(ListView):
    model = Promocion
    template_name = "inicio.html"

#CLASE LOGIN
class LoginListView(ListView):
    model = Promocion
    template_name = "login_register.html"

#CLASE NOSOTROS
class NosotrosListView(ListView):
    model = Promocion
    template_name = "plantillaPadre.html"
#-------------------------------------------------------

# registro de usuario
def registrarUsuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        
        
        # Verificar si ya existe un usuario con ese correo
        if Usuario.objects.filter(correo=correo).exists():
            # alerta si el correo ya existe
            return redirect('/login/?usuario_existente=true')

        # crea el usuario
        usuario = Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            correo=correo,
            contraseña=make_password(contraseña)
        )
        usuario.save()
        # Redirige a login con parámetro en la URL para activar la alerta
        return redirect('/login/?registro_exitoso=true')
    else:
        return redirect('/login/?registro_exitoso=false')

# inicio de sesión
def validarUsuario(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        try:
            # Buscar el usuario con el
            usuario = Usuario.objects.get(correo=correo) 
            # Validar la contraseña
            if check_password(contraseña, usuario.contraseña):
                # Iniciar sesión del usuario
                request.session['usuario_nombre'] = usuario.nombre
                return redirect('/pagina_inicio/?login_exitoso=true')
            else:
                # Contraseña incorrecta
                return redirect('/login/?login_exitoso=false')
        except Usuario.DoesNotExist:
            # Usuario no encontrado
            return redirect('/login/?login_exitoso=false')
    else:
        return redirect('/login/?login_exitoso=false')


def Contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'Usuario/Nosotros.html')

def Contactos(request):
    return render(request, 'Usuario/contactos.html')

def pagina_inicio(request):
    return render(request, 'Usuario/pagina_inicio.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

def configuracion_usuario(request):
    return render(request,'Usuario/configuracion_usuario.html')

def datos_personales(request):
    return render(request, 'Usuario/datos_personales.html')

def historial_compras(request):
    return render(request, 'Usuario/historial_compras.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def editar_usuario(request):
    # Obtener el usuario autenticado
    correo_usuario = request.session.get('usuario')  # Verifica que el usuario esté en la sesión
    if not correo_usuario:
        return redirect('/login')  # Redirige si no está autenticado

    usuario = Usuario.objects.get(correo=correo_usuario)

    if request.method == 'POST':
        # Recuperar datos del formulario manualmente
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')

        # Validar campos si es necesario (opcional)
        if not nombre or not apellido:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
        else:
            # Actualizar datos del usuario
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.telefono = telefono
            usuario.save()

            # Mensaje de éxito
            messages.success(request, '¡Cambios guardados con éxito!')
            return redirect('/editar_usuario')  # Recargar la página

    return render(request, 'editar_usuario.html', {'usuario': usuario})


