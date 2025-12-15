
document.addEventListener("DOMContentLoaded", function () {
    let accordions = document.querySelectorAll(".accordion-card");

    accordions.forEach(card => {
        let btn = card.querySelector(".accordion-button");

        btn.addEventListener("click", function () {
            // Remove active from all
            accordions.forEach(c => c.classList.remove("active"));

            // Add active to clicked
            card.classList.add("active");
        });
    });
});

 // Initialize Swiper
        // var swiper = new Swiper(".videoSwiper", {
        //     slidesPerView: 1,
        //     spaceBetween: 30,
        //     loop: true,
        //     pagination: {
        //         el: ".swiper-pagination",
        //         clickable: true,
        //     },
        //     navigation: {
        //         nextEl: ".swiper-button-next",
        //         prevEl: ".swiper-button-prev",
        //     },
        //     breakpoints: {
        //         640: {
        //             slidesPerView: 1,
        //         },
        //         768: {
        //             slidesPerView: 2,
        //         },
        //         1024: {
        //             slidesPerView: 3,
        //         },
        //     },
        // });


