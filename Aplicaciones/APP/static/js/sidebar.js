// Seleccionar todos los enlaces con la clase "load-view"
const links = document.querySelectorAll('.load-view');

// Seleccionar el contenedor principal donde se cargará el contenido
const mainContent = document.getElementById('main-content');

// Inicializar la variable urlParams para obtener los parámetros de la URL
const urlParams = new URLSearchParams(window.location.search);

// Obtener los parámetros 'exito' y 'error' de la URL
const exito = urlParams.get('exito');
const error = urlParams.get('error');

// Al hacer clic en un enlace del sidebar
links.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Prevenir la redirección normal
        const url = link.getAttribute('data-url'); // Obtener URL desde el atributo "data-url"

        // Mostrar la alerta de carga
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
                // Retrasar la actualización para simular carga
                setTimeout(() => {
                    // Actualizar solo el contenido principal
                    mainContent.innerHTML = html;

                    // Cerrar la alerta de carga
                    Swal.close();
                }, 1000); // Retraso de 1 segundo
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

document.addEventListener('click', function (event) {
    if (event.target && event.target.id === 'btn-editar') {
        const formEditar = document.getElementById('form-editar');
        if (formEditar) {
            formEditar.classList.toggle('d-none');
        }
    }
});

// Mostrar alertas según los parámetros de la URL


    // Cargar dinámicamente el contenido de la vista sin recargar la página
    fetch('/datos_personales?exito=true')
        .then(response => response.text())
        .then(html => {
            if (exito === 'true') {
                Swal.fire({
                    icon: 'success',
                    title: '¡Cambios guardados!',
                    text: 'Tus datos se actualizaron correctamente.',
                    confirmButtonText: 'Aceptar'
                });
                // Después de la acción, por ejemplo, guardar datos
                window.history.pushState({}, '', '/configuracion_usuario?exito=true');
            }
            // Actualizar el contenido
            mainContent.innerHTML = html;
        });


if (error === 'true') {
    Swal.fire({
        icon: 'error',
        title: 'Error al guardar',
        text: 'Por favor completa los campos obligatorios.',
        confirmButtonText: 'Aceptar'
    });
}