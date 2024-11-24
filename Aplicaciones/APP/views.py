from django.shortcuts import render,redirect

from typing import Any
from django.db.models.query import QuerySet
from .models import *
from django.views.generic import ListView
from django.template import *
from .models import Usuario
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout


# Create your views here.

#CLASE PROMOCION
class PromocionListView(ListView):
    model = Promocion
    template_name = "inicio.html"

#CLASE LOGIN
class LoginListView(ListView):
    model = Promocion
    template_name = "login_register.html"

#-------------------------------------------------------

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

def historial_compras(request):
    return render(request, 'Usuario/historial_compras.html')

def datos_personales(request):
    # Recuperar el correo del usuario desde la sesión
    correo_usuario = request.session.get('usuario_correo')
    if not correo_usuario:
        return redirect('/login')  # Redirige si el usuario no está autenticado

    # Obtener el usuario desde la base de datos
    try:
        usuario = Usuario.objects.get(correo=correo_usuario)
    except Usuario.DoesNotExist:
        return redirect('/login')  # Redirige si no se encuentra el usuario

    # Renderizar el template con los datos del usuario
    return render(request, 'Usuario/datos_personales.html', {'usuario': usuario})

# Registro de usuario
def registrarUsuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        correo = request.POST.get('correo', '').strip()
        contraseña = request.POST.get('contraseña', '').strip()
        
        # Verificar si hay campos vacíos
        if not all([nombre, apellido, telefono, correo, contraseña]):
            return redirect('/login/?registro_exitoso=false&error=campos_incompletos')
        
        # Verificar si ya existe un usuario con ese correo
        if Usuario.objects.filter(correo=correo).exists():
            return redirect('/login/?usuario_existente=true')

        # Crear el usuario
        usuario = Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            correo=correo,
            contraseña=make_password(contraseña)
        )
        usuario.save()
        return redirect('/login/?registro_exitoso=true')
    else:
        return redirect('/login/?registro_exitoso=false')


# inicio de sesión
def validarUsuario(request):
    if request.method == 'POST':
        correo = request.POST.get('correo', '').strip()
        contraseña = request.POST.get('contraseña', '').strip()

        # Verificar si hay campos vacíos
        if not correo or not contraseña:
            return redirect('/login/?login_exitoso=false&error=campos_vacios')

        try:
            # Buscar el usuario
            usuario = Usuario.objects.get(correo=correo)
            # Validar la contraseña
            if check_password(contraseña, usuario.contraseña):
                request.session['usuario_nombre'] = usuario.nombre  # Guarda el nombre del usuario
                request.session['usuario_correo'] = usuario.correo  # Guarda el correo del usuario
                return redirect('/pagina_inicio/?login_exitoso=true')
            else:
                return redirect('/login/?login_exitoso=false')
        except Usuario.DoesNotExist:
            return redirect('/login/?login_exitoso=false')
    else:
        return redirect('/login/?login_exitoso=false')


def editar_usuario(request):
    correo_usuario = request.session.get('usuario_correo')  # Obtener el correo desde la sesión
    if not correo_usuario:
        return redirect('/login')  # Redirige si no está autenticado

    try:
        usuario = Usuario.objects.get(correo=correo_usuario)  # Obtener los datos del usuario
    except Usuario.DoesNotExist:
        return redirect('/login')  # Redirige si no se encuentra el usuario

    if request.method == 'POST':
        # Recuperar datos del formulario
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        correo = request.POST.get('correo', '').strip()

        # Validar que los campos necesarios no estén vacíos
        if not nombre or not apellido or not correo:
            return redirect('/datos_personales?error=true')

        # Actualizar los datos del usuario
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.telefono = telefono
        usuario.correo = correo
        usuario.save()

        # Redirigir con mensaje de éxito
        return redirect('/configuracion_usuario?exito=true')

    # Si no es POST, redirigir
    return redirect('/configuracion_usuario')




