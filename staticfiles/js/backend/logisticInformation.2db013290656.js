let hash = window.location.hash;
hash = hash.substring(1)

//Bizning Logistika Turlarimiz

fetch( `https://navoiytourizm.pythonanywhere.com/api/logistika/turlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let ourFotoSection = document.querySelector("#logistika_turlari");
        let swapHistorical1 = "";
        let allImgs1 = [];
        allImgs1 = response;
        if(allImgs1?.length > 0){
          allImgs1?.map((item, index) => {
            swapHistorical1 += `
            <div class="col-xl-4 col-lg-4 col-md-4 col-12 mb-3" data-aos="fade-right" data-aos-duration="800">
                <h3><span>0${index+1}.</span><span>${hash === 'uzb' ? item?.name_uzb : hash === 'rus' ? item?.name_ru : hash === 'eng' ? item?.name_eng : ''}</span></h3>
                <img src='${item?.image_file}' alt="">
                <p>${hash === 'uzb' ? item?.title_uzb : hash === 'rus' ? item?.title_ru : hash === 'eng' ? item?.title_eng : ''}</p>
            </div>
            `
          })
          ourFotoSection.innerHTML = swapHistorical1
       
         }
    }).catch(error => {
        console.log("Error : ", error)
})


//Bizning Logistika Turlarimiz

fetch( `https://navoiytourizm.pythonanywhere.com/api/logistika/rasmlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let ourFotoLogistika = document.querySelector("#logistika_rasmlari");
        let swapHistorical1 = "";
        let allImgs1 = [];
        allImgs1 = response;
        if(allImgs1?.length > 0){
          allImgs1?.map((item) => {
            swapHistorical1 += `
            <div class="swiper-slide" data-aos="fade-down" data-aos-duration="800">
              <div class="swiper-slide">
                <img src="${item?.image_file}" alt="">
              </div>
            </div>
            `
          })
          ourFotoLogistika.innerHTML = swapHistorical1
         }
    }).catch(error => {
        console.log("Error : ", error)
})
