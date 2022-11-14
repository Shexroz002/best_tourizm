let hash = window.location.hash;
hash = hash.substring(1)

// bizning muzeylarimiz 

fetch( `http://navoiytravel.uz/api/bizning/muzeylar?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let museumSection = document.querySelector("#our_museum_id");
        let historicalAllModal = document.querySelector("#museum_all_modal");
        let swapMuseum = "";
        let swapHistoricalModal = "";
        let allImgs = [];
        allImgs = response;
        if(allImgs?.length > 0){
          allImgs?.map((item, index) => {
            swapMuseum += `
            <div class="swiper-slide"  data-aos="fade-down" data-aos-duration="800">
            <img src="${item?.image_file}" alt="">
              <div class="btn_services_box">
                  <button type="button" class="btn btn-danger" data-bs-toggle="modal"  data-bs-target="#exampleModal${index+1}">
                  Batafsil
                  </button>
              </div>
             </div>
            `
          })
          museumSection.innerHTML = swapMuseum;

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


// bizning restoranlar haqida

fetch( `http://navoiytravel.uz/api/restaran/haqida?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
         let restarantText = document.querySelector("#restarant_text");
         if(response?.length){
           let texts = hash === 'uzb' ? response[0]?.title_uzb : hash === 'rus' ? response[0]?.title_ru : hash === 'eng' ? response[0]?.title_eng : '';
           restarantText.innerHTML= texts
         }
    }).catch(error => {
        console.log("Error : ", error)
})


// bizning restoranlar rasmlari

fetch( `http://navoiytravel.uz/api/restaran/rasmlar?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let restorantSection = document.querySelector("#restorant_rasmlari");
        let swapRestorant = "";
        let allImgs = [];
        allImgs = response;
        if(allImgs?.length > 0){
          allImgs?.map((item) => {
            swapRestorant += `
            <div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 col-12 mb-4" data-aos="fade-up" data-aos-duration="800">
              <div class="img-food">
                 <img src="${item?.image_file}" alt="${item?.name}">
              </div> 
            </div>
            `
          })
          restorantSection.innerHTML = swapRestorant
        }
    }).catch(error => {
        console.log("Error : ", error)
})



// bizning savdo markazlarimiz haqida

fetch( `http://navoiytravel.uz/api/savdo/markaz/haqida?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
      let shopText = document.querySelector("#malls-text"); 
      let allData = [];
      allData = response;
      shopText.innerHTML= `
        ${hash === 'uzb' ? allData[0]?.title_uzb : hash === 'rus' ? allData[0]?.title_ru : hash === 'eng' ? allData[0]?.title_eng : ''}
      `
    }).catch(error => {
        console.log("Error : ", error)
})

// bizning savdo markazlarimiz rasmlari

fetch( `http://navoiytravel.uz/api/savdo/markaz/rasmlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let shopSection = document.querySelector("#shop_data_img");
        let swapShop = "";
        let allImgs = [];
        allImgs = response;
        if(allImgs?.length > 0){
          allImgs?.map((item) => {
            swapShop += `
            <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12 mb-4" data-aos="fade-up" data-aos-duration="800">
                    <div class="img-food">
                         <img src="${item?.image_file}" alt="${item?.name}">
                    </div> 
             </div>
            `
          })
          shopSection.innerHTML = swapShop
        }
    }).catch(error => {
        console.log("Error : ", error)
})

// bizning ko'rgazmalar

fetch( `http://navoiytravel.uz/api/korgazmalar?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let ourFotoSection = document.querySelector("#kurgazmalar_rasmi");
        let swapExbition = "";
        let allImgs2 = [];
        allImgs2 = response;
        if(allImgs2?.length > 0){
          allImgs2?.map((item) => {
            swapExbition += `
            <div class="swiper-slide"  data-aos="fade-down" data-aos-duration="800">
              <img src="${item?.image_file}" alt="${item?.name}">
            </div>
            `
          })
          ourFotoSection.innerHTML = swapExbition
        }
    }).catch(error => {
        console.log("Error : ", error)
})


