"use strict";

AOS.init();

// document.addEventListener('DOMContentLoaded', () => {
//    const loader = document.querySelector('.preloader');
//    setTimeout(() => {
//       loader.style.opacity = 0;
// 	  setTimeout(() => {
//         loader.style.display = none;
// 	  }, 2000)
//    },3500)
// });

var swiper = new Swiper(".bg-slider-thumbs", {
    loop: true,
    spaceBetween: 0,
    slidesPerView: 0,
    autoplay: {
      delay: 5000,
    },
  });
  var swiper2 = new Swiper(".bg-slider", {
    loop: true,
    spaceBetween: 0,
    autoplay: {
      delay: 5000,
    },
    thumbs: {
      swiper: swiper,
    },
});


window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    const head = document.querySelector('.head');
    header.classList.toggle('active', window.scrollY>0)
    head.classList.toggle('active', window.scrollY>0)
})

const menuBtn = document.querySelector('.nav-menu-btn')
const closeBtn = document.querySelector('.nav-close-btn')
const headerUl = document.querySelector('.header-ul')

menuBtn.addEventListener('click', () =>{
   headerUl.classList.add('active')
})

closeBtn.addEventListener('click', () =>{
  headerUl.classList.remove('active')
})


/* trandiing */
var swiper = new Swiper(".Effect-overflow", {
  loop: true,
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  autoplay: {
    delay: 4000,
  },
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 2.5,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
}); 
/* trandiing */



var swiper = new Swiper(".card_slider", {
  loop: true,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  autoplay: {
    delay: 4000,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
    },
    480: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1200: {
      slidesPerView: 4,
    },
  },
});