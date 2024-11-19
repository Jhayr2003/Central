// Seleccionar todos los enlaces con la clase "load-view"
const links = document.querySelectorAll('.load-view');

// Seleccionar el contenedor principal donde se cargará el contenido
const mainContent = document.getElementById('main-content');

// Agregar evento de clic a cada enlace del sidebar
links.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Prevenir redirección
        const url = link.getAttribute('data-url'); // Obtener URL desde el atributo "data-url"

        // Mostrar una alerta de carga
        Swal.fire({
            title: 'Cargando...',
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
            }
        });

        // Hacer la solicitud para cargar la vista
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al cargar la vista.');
                }
                return response.text();
            })
            .then(html => {
                // Añadir un retraso de 4 segundos antes de mostrar el contenido
                setTimeout(() => {
                    // Actualizar el contenido del contenedor
                    mainContent.innerHTML = html;

                    // Cerrar la alerta de carga
                    Swal.close();
                }, 1000); // Retraso de 4000 ms (4 segundos)
            })
            .catch(error => {
                // Mostrar alerta de error
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: error.message,
                    confirmButtonText: 'Aceptar'
                });
            });
    });
});
