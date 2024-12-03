document.addEventListener('DOMContentLoaded', () => {
    const yapeForm = document.getElementById('yape-form');

    yapeForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Evita el envío del formulario por defecto

        // Capturar el código de referencia ingresado por el usuario
        const referenceCode = document.getElementById('reference-code').value.trim();
        if (!referenceCode) {
            Swal.fire({
                icon: 'error',
                title: 'Por favor, ingresa un código de referencia.',
                showConfirmButton: true,
            });
            return;
        }

        // Verificar que el código de referencia está bien capturado
        console.log('Código de referencia:', referenceCode);

        // Recuperar los datos del carrito desde localStorage
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        if (cart.length === 0) {
            Swal.fire({
                icon: 'error',
                title: 'El carrito está vacío.',
                text: 'Agrega productos antes de finalizar la compra.',
                showConfirmButton: true,
            });
            return;
        }

        // Verificar que el carrito tiene datos y calcular el total
        console.log('Datos del carrito:', cart);
        const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
        console.log('Total de la compra:', total);

        // Enviar los datos al backend
        fetch('/procesar_pago/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // Reemplaza con tu lógica para obtener el CSRF token
            },
            body: JSON.stringify({
                cart, // Productos en el carrito
                total, // Total de la compra
                method: 'Yape', // Método de pago
                reference: referenceCode, // Código de referencia ingresado
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    Swal.fire({
                        icon: 'success',
                        title: 'Pago registrado exitosamente.',
                        showConfirmButton: false,
                        timer: 1000
                    }).then(() => {
                        localStorage.removeItem('cart'); // Limpia el carrito
                        location.reload(); // Recarga la página
                        window.location.href = '/pagina_inicio/'; // Redirige a la página de inicio
                    });
                } else {
                    Swal.fire({
                        icon: 'error',
                        title: 'Error al procesar el pago.',
                        text: data.error || 'Intenta nuevamente.',
                        showConfirmButton: true,
                    });
                }
            })
            .catch((error) => {
                console.error('Error al procesar el pago:', error);
                Swal.fire({
                    icon: 'error',
                    title: 'Ocurrió un error.',
                    text: error.message || 'Intenta nuevamente.',
                    showConfirmButton: true,
                });
            });
        const modal = document.getElementById('yapeModal');
        if (modal.style.display === 'block') {
            modal.removeAttribute('aria-hidden');
        }
    });

    // Función para obtener el CSRF token (si usas Django)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
