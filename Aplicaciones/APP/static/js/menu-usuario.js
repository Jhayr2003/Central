// Obtén el ícono y el cuadro de inicio de sesión
const userIcon = document.getElementById('user-icon');
const loginBox = document.getElementById('login-box');

// Evento para mostrar/ocultar el cuadro de inicio de sesión
userIcon.addEventListener('click', function(event) {
    // Evita que se propague el evento de clic al documento
    event.stopPropagation();
    
    if (loginBox.style.display === 'none' || loginBox.style.display === '') {
        loginBox.style.display = 'block';
    } else {
        loginBox.style.display = 'none';
    }
});

// Cerrar el cuadro al hacer clic fuera de él
document.addEventListener('click', function(event) {
    if (!userIcon.contains(event.target) && !loginBox.contains(event.target)) {
        loginBox.style.display = 'none';
    }
});

// Evita que el enlace sea bloqueado
loginBox.addEventListener('click', function(event) {
    event.stopPropagation();  // Permite que el enlace funcione correctamente
});
