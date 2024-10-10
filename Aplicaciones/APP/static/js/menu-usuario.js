console.log("menu-usuario.js cargado");

// Selecciona el menú del usuario
const userDropdownMenu = document.querySelector('.user-menu');

// Manejo del clic en el icono de usuario para mostrar/ocultar el menú
document.querySelector('.user-icon').addEventListener('click', function (event) {
    event.stopPropagation(); // Evita que el clic se propague al documento
    // Alterna la visibilidad del menú
    if (userDropdownMenu.style.display === 'block') {
        userDropdownMenu.style.display = 'none';
    } else {
        userDropdownMenu.style.display = 'block';
    }
});

// Evento para cerrar el menú si se hace clic fuera de él
document.addEventListener('click', function (event) {
    // Verifica si el clic fue fuera del menú y el icono de usuario
    if (!userDropdownMenu.contains(event.target) && !document.querySelector('.user-icon').contains(event.target)) {
        userDropdownMenu.style.display = 'none'; // Cierra el menú
    }
});
