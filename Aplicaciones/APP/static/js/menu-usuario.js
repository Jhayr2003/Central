// Obtén el ícono y el cuadro de inicio de sesión
const userIcon = document.getElementById('user-icon');
const loginBox = document.getElementById('login-box');

// Evento para mostrar/ocultar el cuadro de inicio de sesión
userIcon.addEventListener('click', function() {
    if (loginBox.style.display === 'none' || loginBox.style.display === '') {
        loginBox.style.display = 'block';
    } else {
        loginBox.style.display = 'none';
    }
});

// Opcional: Si quieres cerrar el cuadro al hacer clic fuera de él
document.addEventListener('click', function(event) {
    if (!userIcon.contains(event.target) && !loginBox.contains(event.target)) {
        loginBox.style.display = 'none';
    }
});
