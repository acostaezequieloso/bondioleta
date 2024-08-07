
document.addEventListener('DOMContentLoaded', function () {
    const cartToggle = document.getElementById('cart-toggle');
    const cartDropdown = document.getElementById('carrito');

    cartToggle.addEventListener('click', function (e) {
        e.preventDefault();
        if (cartDropdown.style.display === 'block') {
            cartDropdown.style.display = 'none';
        } else {
            cartDropdown.style.display = 'block';
        }
    });
});