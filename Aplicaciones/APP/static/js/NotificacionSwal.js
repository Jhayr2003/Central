// Obtener los parámetros de la URL
const urlParams = new URLSearchParams(window.location.search);
const registroExitoso = urlParams.get('registro_exitoso');
const loginExitoso = urlParams.get('login_exitoso');
const usuarioExistente = urlParams.get('usuario_existente');
const error = urlParams.get('error');

// Seleccionar todos los enlaces con la clase "btn-comprar"
const enlacesComprar = document.querySelectorAll('.btn-comprar');

// Mostrar alerta si el registro fue exitoso
if (registroExitoso === 'true') {
    Swal.fire({
        icon: 'success',
        title: 'Registro exitoso',
        text: 'Por favor, inicia sesión.',
        confirmButtonText: 'Aceptar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Recarga la página sin el parámetro en la URL
            window.location.href = 'login/';
        }
    });
} else if (registroExitoso === 'false') {
    Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Hubo un problema en el registro. Inténtalo nuevamente.',
        confirmButtonText: 'Aceptar'
    });
}

// Mostrar alerta si el usuario ya existe
if (usuarioExistente === 'true') {
    Swal.fire({
        icon: 'error',
        title: 'Usuario existente',
        text: 'El usuario con este correo ya existe. Intenta con otro correo.',
        confirmButtonText: 'Aceptar'
    });
}

// Mostrar alerta si el inicio de sesión falló
if (loginExitoso === 'false') {
    Swal.fire({
        icon: 'error',
        title: 'Error de autenticación',
        text: 'Credenciales incorrectas. Inténtalo nuevamente.',
        confirmButtonText: 'Aceptar'
    });
}

//Mostrar alerta por campos incompletos y vacios
if (error === 'campos_incompletos') {
    Swal.fire({
        icon: 'error',
        title: 'Error en el registro',
        text: 'Por favor completa todos los campos.',
        confirmButtonText: 'Aceptar'
    });
} else if (error === 'campos_vacios') {
    Swal.fire({
        icon: 'error',
        title: 'Error en el inicio de sesión',
        text: 'Por favor ingresa tu correo y contraseña.',
        confirmButtonText: 'Aceptar'
    });
}

// Iterar sobre cada enlace y agregar un evento de clic
enlacesComprar.forEach((enlace) => {
    enlace.addEventListener('click', (event) => {
        // Prevenir que el enlace redirija
        event.preventDefault();

        // Simula la lógica de autenticación
        const usuarioAutenticado = false; // Cambia esto según tu lógica de autenticación

        if (!usuarioAutenticado) {
            // Mostrar alerta si no está autenticado
            Swal.fire({
                icon: 'warning',
                title: 'Iniciar sesión',
                text: 'Debe iniciar sesión para poder realizar una compra.',
                confirmButtonText: 'Aceptar'
            });
        } else {
            // Lógica para continuar con la compra
            window.location.href = '/comprar'; // Cambia "/comprar" por la URL real de compra
        }
    });
});

