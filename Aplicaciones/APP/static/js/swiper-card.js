// Inicialización del Swiper con configuración mejorada
var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    spaceBetween: 10,
    loop: false, // Desactivamos el loop para evitar duplicados
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets: true, // Mejora visual para muchos slides
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    // Autoplay opcional

    // Mejores breakpoints para responsividad
    breakpoints: {
        // Móvil
        320: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        // Tablet
        768: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        // Desktop
        992: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
        // Large Desktop
        1200: {
            slidesPerView: 4,
            spaceBetween: 40,
        }
    },
    // Mejora la experiencia táctil
    touchEventsTarget: 'wrapper',
    grabCursor: true,
    // Mejora la accesibilidad
    a11y: {
        prevSlideMessage: 'Slide anterior',
        nextSlideMessage: 'Siguiente slide',
        firstSlideMessage: 'Este es el primer slide',
        lastSlideMessage: 'Este es el último slide',
    }
});
