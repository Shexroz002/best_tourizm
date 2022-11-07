fetch( 'https://navoiytravel.uz/mehmonxonda/open/and/close' )
    .then( response => response.json() )
    .then (response => {
        let timeBox = document.querySelector("#time_id");
        let timeData = []
        timeData = response;
        timeBox.innerHTML = `
        <div class="row">
        <div class="col-md-6">
            <div class="schedule">
                <h1>${timeData[0]?.opan_close_day}</h1>
                <h1>${timeData[0]?.open_hour}</h1>
                <h1>${timeData[0]?.close_hour}</h1>
            </div>
        </div>
        <div class="col-md-6">
            <div class="schedule schedule-after-none">
            <h1>${timeData[1]?.opan_close_day}</h1>
            <h1>${timeData[1]?.open_hour}</h1>
            <h1>${timeData[1]?.close_hour}</h1>
            </div>
        </div>
    </div>
        `
}).catch((error) => {
    console.log("Error vaqt : ", error);
});


fetch( 'https://navoiytravel.uz/mehmonxonda/rooms' )
    .then( response => response.json() )
    .then( response => {
        let ourCardBlack = document.querySelector("#ourRooms_card");
        let cardOurRoomData = ""
        let ourRooms = [];
        ourRooms = response;
        if(ourRooms?.length>0){
            ourRooms?.map((item) => {
                cardOurRoomData += `<div class="swiper-slide">
                <img src="${item?.room_file}" alt="">
                <div class="text-hotels">
                    <h4>${item.room_name}</h4>
                    <ul>
                        <li><i class="fa fa-star"></i></li>
                        <li><i class="fa fa-star"></i></li>
                        <li><i class="fa fa-star"></i></li>
                        <li><i class="fa fa-star"></i></li>
                        <li><i class="fa fa-star"></i></li>
                    </ul>
                    <p>${item.room_title}</p>
                    <div class="img-hotels-box">
                        <a href="#">BOOK NOW</a>
                        <h4>$ <span>${item.room_price}</span></h4>
                    </div>
                </div>
              </div>`
            })
            ourCardBlack.innerHTML = cardOurRoomData;
        } else {
            ourCardBlack.innerHTML = `<h3>Ma'lumotlar kiritilmagan</h3>`;
        }
} ).catch((error) => {
    let ourCardBlack = document.querySelector("#ourRooms_card");
    ourCardBlack.innerHTML = `<h3>${error}</h3>`
});


fetch( 'https://navoiytravel.uz/mehmonxonda/meals' )
    .then( response => response.json() )
    .then( response => { 
        let hotdogSection = document.querySelector("#hotdog_row");
        let hotdogData = ""
        let allData = [];
        allData = response;
        let hotDishes = allData.filter(item => item?.catagorya === 'hot');
        hotDishes?.map(item => {
            hotdogData+=`
            <div class="col-md-6">
            <div class="menu-items">
                <span data-bs-toggle="modal" data-bs-target="#modalImages_1">
                    <a data-bs-container="body" data-bs-toggle="tooltip" data-bs-placement="top"
                        data-bs-delay="100" data-bs-html="true"
                        title="<b><em>Click To View The Image</em></b>">${item?.meal_name}</a>
                </span>
                <span class="custom-rounded-dots"></span>
                <span>$<span>${item?.meal_price}</span></span>
                <p>${item?.meal_title}</p>
            </div>
            <!-- FOR MODAL IMAGE START-->
            <div class="modal fade" id="modalImages_1" tabindex="-1" aria-labelledby="ModalImages_1"
                aria-hidden="true">
                <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="ModalImages_1">${item?.meal_name}</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal"
                                aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <img class="img-fluid w-100" src="${item?.meal_image}"
                                alt="${item?.meal_name}">
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary"
                                data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
            <!-- FOR MODAL IMAGE END-->
        </div>
            `
        })
        hotdogSection.innerHTML=hotdogData
} ).catch((error) => {
    console.log("Xatolik : ", error)
});


fetch( 'https://navoiytravel.uz/mehmonxonda/meals' )
    .then( response => response.json() )
    .then( response => { 
        let hotdogSection = document.querySelector("#disert_row");
        let hotdogData = ""
        let allData = [];
        allData = response;
        let hotDishes = allData.filter(item => item?.catagorya === 'disert');
        hotDishes?.map(item => {
            hotdogData+=`
            <div class="col-md-6">
            <div class="menu-items">
                <span data-bs-toggle="modal" data-bs-target="#modalImages_1">
                    <a data-bs-container="body" data-bs-toggle="tooltip" data-bs-placement="top"
                        data-bs-delay="100" data-bs-html="true"
                        title="<b><em>Click To View The Image</em></b>">${item?.meal_name}</a>
                </span>
                <span class="custom-rounded-dots"></span>
                <span>$<span>${item?.meal_price}</span></span>
                <p>${item?.meal_title}</p>
            </div>
            <!-- FOR MODAL IMAGE START-->
            <div class="modal fade" id="modalImages_1" tabindex="-1" aria-labelledby="ModalImages_1"
                aria-hidden="true">
                <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="ModalImages_1">${item?.meal_name}</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal"
                                aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <img class="img-fluid w-100" src="${item?.meal_image}"
                                alt="${item?.meal_name}">
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary"
                                data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
            <!-- FOR MODAL IMAGE END-->
        </div>
            `
        })
        hotdogSection.innerHTML=hotdogData
} ).catch((error) => {
    console.log("Xatolik : ", error)
});


let form = document.querySelector('#form');

form.addEventListener('submit', function(e){
    e.preventDefault();

    let name = document.querySelector('#text').value;
    let phone = document.querySelector('#number').value;
    let email = document.querySelector('#email').value;
    let textArea = document.querySelector('#textarea').value;
    if(textArea.trim()){
      fetch(`https://navoiytravel.uz/mehmonxonda/customermassage/`, {
        method: 'POST',
        body: JSON.stringify({
            name: name,
            phone_number: phone,
            email: email,
            message:textArea 
        }),
        headers: {
         'Content-type': 'application/json; charset=UTF-8',
        },
       })
      .then((response) => response.json())
      .then((json) => console.log("Javob : ", json));
    }
    else{
      alert("Biror bir so'z kiriting")
    }
})