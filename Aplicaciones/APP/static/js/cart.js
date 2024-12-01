document.addEventListener('DOMContentLoaded', () => {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const modal = document.getElementById('cartModal');
    updateCartCount();
    // Escuchar el evento 'hidden.bs.modal' cuando el modal se cierra
    modal.addEventListener('hidden.bs.modal', () => {
        location.reload(); // Recargar la página
    });

    document.querySelectorAll('.btn-danger').forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const card = event.target.closest('.card');
            const title = card.querySelector('.card-title').innerText;
            const price = parseFloat(card.querySelector('.card-text').innerText.replace('S/.', '').replace(',', '.'));

            const existingProduct = cart.find(product => product.title === title);

            if (existingProduct) {
                existingProduct.quantity += 1;
            } else {
                const product = { title, price, quantity: 1 };
                cart.push(product);
            }

            localStorage.setItem('cart', JSON.stringify(cart));
            updateCartCount();
        });
    });

    document.querySelector('.cart-menu').addEventListener('click', () => {
        displayCartItems();
    });
});

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    document.querySelector('.cart-menu .badge').innerText = totalItems;
}

function displayCartItems() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    let cartItemsHtml = '<ul class="list-group">';
    let total = 0;

    cart.forEach((item, index) => {
        total += item.price * item.quantity;

        cartItemsHtml += `
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                    <h5>${item.title}</h5>
                    <p>Precio: S/.${item.price.toFixed(2)} x ${item.quantity}</p>
                </div>
                <button class="btn btn-danger btn-sm" onclick="removeCartItem(${index})">Eliminar</button>
            </li>`;
    });

    cartItemsHtml += '</ul>';
    cartItemsHtml += `<div class="mt-3"><h5>Total: S/.${total.toFixed(2)}</h5></div>`;

    document.querySelector('#cartModal .modal-body').innerHTML = cartItemsHtml;
}

function removeCartItem(index) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Reducir la cantidad del producto
    if (cart[index].quantity > 1) {
        cart[index].quantity -= 1; // Reduce la cantidad
    } else if (cart[index].quantity === 1) {
        // Mostrar alerta de confirmación antes de eliminar
        Swal.fire({
            title: '¿Estás seguro?',
            text: "¡No podrás revertir esto!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, eliminarlo',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                // Eliminar el producto del carrito
                cart.splice(index, 1);
                // Actualiza el localStorage
                localStorage.setItem('cart', JSON.stringify(cart));
                // Actualiza el contador y el carrito en la vista
                updateCartCount();
                displayCartItems();
                // Mostrar alerta de éxito
                Swal.fire(
                    'Eliminado!',
                    'El producto ha sido eliminado.',
                    'success'
                );
            }
        });
    }
    // Actualiza el localStorage
    localStorage.setItem('cart', JSON.stringify(cart));

    // Actualiza el contador y el carrito en la vista
    updateCartCount();
    displayCartItems();
}