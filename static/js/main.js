// NAVBAR AUTO-HIDE
document.addEventListener("DOMContentLoaded", function () {
    el_autohide = document.querySelector('.autohide');
    if (el_autohide) {
        var last_scroll_top = 0;
        window.addEventListener('scroll', function () {
            let scroll_top = window.scrollY;
            if (scroll_top < last_scroll_top) {
                el_autohide.classList.remove('scrolled-down');
                el_autohide.classList.add('scrolled-up');
            } else {
                el_autohide.classList.remove('scrolled-up');
                el_autohide.classList.add('scrolled-down');
            }
            last_scroll_top = scroll_top;
        });
    }
});
// OWL SLIDER
$('.owl-carousel').owlCarousel({
    nav: false,
    items: 1,
    loop: true,
    margin: 15,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplaySpeed: 1000,
    autoplayHoverPause: false,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})
//  SWIPER SLIDER 
var swiper = new Swiper(".mySwiper", {
    loop: true,
    spaceBetween: 30,
    effect: "fade",
    centeredSlides: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});
// Google Map API
let map;

function initMap() {
    var location = {
        lat: 39.045753,
        lng: -76.641273
    };
    map = new google.maps.Map(document.getElementById("map"), {
        center: location,
        zoom: 12
    });
    /*
    
    */
    addMarker({
        coordinates: {
            lat: 38.9897,
            lng: -76.9378
        },
        content: '<h6>Secret Mirage - Maryland Branch</h6>'
    });
    addMarker({
        coordinates: {
            lat: 42.4072,
            lng: -71.3824
        },
        content: '<h6>Secret Mirage - Massachusetts Branch</h6>'
    });
    addMarker({
        coordinates: {
            lat: 39.5501,
            lng: -105.7821
        },
        content: '<h6>Secret Mirage - Colorado Branch</h6>'
    });
    addMarker({
        coordinates: {
            lat: 32.3547,
            lng: -89.3985
        },
        content: '<h6>Secret Mirage - Mississippi Branch</h6>'
    });
    addMarker({
        coordinates: {
            lat: 37.7749,
            lng: -122.4194
        },
        content: '<h6>Secret Mirage - California Branch</h6>'
    });

    function addMarker(properties) {
        var marker = new google.maps.Marker({
            position: properties.coordinates,
            map: map
        });
        if (properties.content) {
            var infoWindow = new google.maps.InfoWindow({
                content: properties.content
            });
            marker.addListener('click', function () {
                infoWindow.open(map, marker);
            })
        }
    }
}
// // PRELOADER
/* ishlatilmagan */
// function preloader() {
//     var page = setTimeout(showPage, 5000);
// }
// function showPage() {
//     document.getElementById("loader").style.setProperty('display', 'none', 'important');
//     document.getElementById("body").style.overflow = "visible";
//     document.getElementById("whole__section").style.visibility = "visible";
// }
/* ishlatilmagan */


// // FakeLoader
// $(document).ready(function () {
//     $.fakeLoader({
//         timeToHide: 4000,
//         bgColor: "#C59D5F",
//         spinner: "spinner1"
//     });
// });


var swiper = new Swiper(".hotelSwiper", {
    loop: true,
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    autoplay: {
      delay: 3000,
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

  // backend settings
/*
  const hotelImgBg = {
    text : {
        description1 : "The History of Kitchens and Cooks gives further intimation on Mr Boulanger usual menu stating confidently that 'Boulanger served salted poultry and fresh eggs, all presented without a tablecloth on small marble tables'. Numerous commentators have also referred to the supposed restaurant owners eccentric habit of touting for custom outside his establishment, dressed in aristocratic fashion and brandishing a sword.",
        description2 : "Numerous commentators have also referred to the supposed restaurant owner's eccentric habit of touting for custom outside his establishment, dressed in aristocratic fashion and brandishing a sword.",      
    },
    imgsBgHotel : {
        imgsArr : ["https://thumbs.dreamstime.com/b/hotel-bed-room-21064950.jpg","https://thumbs.dreamstime.com/b/chambre-d-h-tel-de-luxe-73132780.jpg","https://thumbs.dreamstime.com/b/int%C3%A9rieur-d-h%C3%B4tel-10269311.jpg","https://thumbs.dreamstime.com/b/chambre-pour-deux-personnes-d-h%C3%B4tel-12392330.jpg","https://thumbs.dreamstime.com/b/hotel-bed-room-21064950.jpg","https://thumbs.dreamstime.com/b/hotel-bed-room-21064950.jpg",]
    }
  }
  let AboutImg = []
  for(let i=1; i<=hotelImgBg?.imgsBgHotel?.imgsArr.length; i++) {
    console.log(`.about-img-${i}`)
    AboutImg[i-1] = document.querySelector(`.about-img-${i}`)
    AboutImg[i-1].style.backgroundImage = hotelImgBg?.imgsBgHotel?.imgsArr[i]
  }
*/