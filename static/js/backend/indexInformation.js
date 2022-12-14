let hash = window.location.hash;
hash = hash.substring(1)

//tarixiy joylar
fetch( `http://navoiytravel.uz/api/tarixiy/turizm/rasmlar?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
      console.log("Response : ", response)
        let historicalSection = document.querySelector("#tarixiy_joylar");
        let historicalAllModal = document.querySelector("#historical_all_modal");
        let swapHistorical = "";
        let swapHistoricalModal = "";
        let allImgs = [];
        allImgs = response;
        if(allImgs?.length > 0){
          allImgs?.map((item, index) => {
            swapHistorical += `
            <div class="swiper-slide">
                <img src="${item?.image_file}"/>
                <h3>${hash === 'uzb' ? item?.name_uzb : hash === 'rus' ? item?.name_ru : hash === 'eng' ? item?.name_eng : ''}</h3>
                <div>
                    <div class="historical_place_btn">
                        <button type="button" class="btn btn-danger" data-bs-toggle="modal"
                                data-bs-target="#exampleModal${index+1}">
                            Batafsil
                        </button>
                    </div>
                </div>
            </div>
            `
          })
          historicalSection.innerHTML = swapHistorical;
          
          allImgs?.map((item, index) => {
            swapHistoricalModal += `
            <div class="modal fade" id="exampleModal${index+1}" tabindex="-1" aria-labelledby="exampleModalLabel${index+1}" aria-hidden="true">
           <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel${index+1}">${hash === 'uzb' ? item?.name_uzb : hash === 'rus' ? item?.name_ru : hash === 'eng' ? item?.name_eng : ''}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-xl-6 xol-lg-6 col-md-6 col-12">
                            <img src="${item?.image_file}" alt="">
                        </div>
                        <div class="col-xl-6 xol-lg-6 col-md-6 col-12">
                            <h3>${hash === 'uzb' ? item?.name_uzb : hash === 'rus' ? item?.name_ru : hash === 'eng' ? item?.name_eng : ''}</h3>
                            <p>${hash === 'uzb' ? item?.title_uzb : hash === 'rus' ? item?.title_ru : hash === 'eng' ? item?.title_eng : ''}</p>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Yopish</button>
                </div>
            </div>
        </div>
       </div>
            `
          })
          historicalAllModal.innerHTML=swapHistoricalModal;
        }
    }).catch(error => {
        console.log("Error : ", error)
})

//bizning galereyamiz
fetch( `http://navoiytravel.uz/api/bizning/galeryamiz`)
    .then( response => response.json() )
    .then(response => {
      console.log("Bizning galeriyamiz : ", response)
        let ourFotoSection = document.querySelector("#bizning_foto");
        let swapHistorical1 = "";
        let allImgs1 = [];
        allImgs1 = response;
        if(allImgs1?.length > 0){
          allImgs1?.map((item) => {
            swapHistorical1 += `
            <div class="swiper-slide" data-aos="fade-down" data-aos-duration="800">
            <div class="swiper-slide">
                <img src='${item?.image_file}' alt="">
            </div>
            </div>
            `
          })
          ourFotoSection.innerHTML = swapHistorical1
        }
    }).catch(error => {
        console.log("Error : ", error)
})


// biz bilan bog'laning
fetch( `http://navoiytravel.uz/api/client/bilan/boglanish?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
         let ourAboutUl = document.querySelector("#contact_ul");
          let allInformation = [];
          allInformation = response;
         ourAboutUl.innerHTML = `
            <li>
             <span class="icon-span"><i class="uil uil-map-marker"></i></span>
             <h6>Address: ${hash === 'uzb' ? allInformation[0]?.location_uzb : hash === 'rus' ? allInformation[0]?.location_ru : hash === 'eng' ? allInformation[0]?.location_eng : ''}</h6>
            </li>
          <li>
            <span class="icon-span"><i class="uil uil-phone-alt"></i></span> 
            <h6>Phone: ${allInformation[0]?.phone_number}</h6>
          </li>
          <li>
            <span class="icon-span"><i class="uil uil-envelope-alt"></i></span>
            <h6>Email: ${allInformation[0]?.email}</h6>
          </li>
          <li>
            <span class="icon-span"><i class="uil uil-telegram-alt"></i></span>
            <h6>Telegram: ${allInformation[0]?.telegram_link}</h6>
          </li>
         `
    }).catch(error => {
        console.log("Error : ", error)
})




// contact qismi
// chala


let form = document.querySelector('#form');

form.addEventListener('submit', function(e){
    e.preventDefault();

    let name = document.querySelector('#input-name').value;
    let phone = document.querySelector('#input-phone').value;
    let email = document.querySelector('#input-email').value;
    let textArea = document.querySelector('#story').value;
    if(textArea.trim()){
      fetch(`http://navoiytravel.uz/api/biz/bilan/boglanish`, {
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