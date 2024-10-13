// Selecciona el menú del usuario
const userDropdownMenu = document.querySelector('.user-menu');

// Manejo del clic en el icono de usuario para mostrar/ocultar el menú
document.querySelector('.user-icon').addEventListener('click', function (event) {
    event.stopPropagation(); // Evita que el clic se propague al documento
    // Alterna la visibilidad del menú con opacity y visibility
    if (userDropdownMenu.style.opacity === '1') {
        userDropdownMenu.style.opacity = '0';
        userDropdownMenu.style.visibility = 'hidden';
    } else {
        userDropdownMenu.style.opacity = '1';
        userDropdownMenu.style.visibility = 'visible';
    }
});

// Evento para cerrar el menú si se hace clic fuera de él
document.addEventListener('click', function (event) {
    // Verifica si el clic fue fuera del menú y el icono de usuario
    if (!userDropdownMenu.contains(event.target) && !document.querySelector('.user-icon').contains(event.target)) {
        userDropdownMenu.style.opacity = '0';
        userDropdownMenu.style.visibility = 'hidden'; // Cierra el menú con animación
    }
});
// Permitir que el colapso funcione sin interferencia del menú de usuario
document.querySelector('.navbar-toggler').addEventListener('click', function (event) {
    event.stopPropagation(); // Permitir que Bootstrap maneje el colapso correctamente
});