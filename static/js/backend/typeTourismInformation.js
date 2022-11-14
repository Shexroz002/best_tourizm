let hash = window.location.hash;
hash = hash.substring(1)

// bizning gastro turizm 1

fetch( `http://navoiytravel.uz/api/turizm/turlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
         let gastroSection1 = document.querySelector("#gastro_turizm1");
         let allTypeData = [];
         allTypeData = response;
         gastroSection1.innerHTML = `
         <div class="col-xl-5 col-lg-6 col-md-6 col-12 gastro-img mb-5" data-aos="fade-right" data-aos-duration="800">
         <img src="${allTypeData[0]?.image_file}" alt="">
          </div>
         <div class="col-xl-6 col-lg-6 col-md-6 col-12 gastro-text mb-5" data-aos="fade-left" data-aos-duration="800">
          <h4>${hash === 'uzb' ? allTypeData[0]?.name_uzb : hash === 'rus' ? allTypeData[0]?.name_ru : hash === 'eng' ? allTypeData[0]?.name_eng : ''}</h4>
          <p class="lng-gastro_p1">${hash === 'uzb' ? allTypeData[0]?.title_uzb : hash === 'rus' ? allTypeData[0]?.title_ru : hash === 'eng' ? allTypeData[0]?.title_eng : ''}</p>
         </div>
         `
    }).catch(error => {
        console.log("Error : ", error)
})

// bizning gastro turizm 2

fetch( `http://navoiytravel.uz/api/turizm/turlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
         let gastroSection1 = document.querySelector("#gastro_turizm2");
         let allTypeData = [];
         allTypeData = response;
         gastroSection1.innerHTML = `
          <div class="col-xl-6 col-lg-6 col-md-6 col-12 gastro-text mb-4" data-aos="fade-left" data-aos-duration="800">
           <h4>${hash === 'uzb' ? allTypeData[0]?.name_uzb : hash === 'rus' ? allTypeData[0]?.name_ru : hash === 'eng' ? allTypeData[0]?.name_eng : ''}</h4>
           <p class="lng-gastro_p1">${hash === 'uzb' ? allTypeData[0]?.title_uzb : hash === 'rus' ? allTypeData[0]?.title_ru : hash === 'eng' ? allTypeData[0]?.title_eng : ''}</p>
          </div>
          <div class="col-xl-5 col-lg-6 col-md-6 col-12 gastro-img" data-aos="fade-right" data-aos-duration="800">
            <img src="${allTypeData[0]?.image_file}" alt="">
          </div>
         `
    }).catch(error => {
        console.log("Error : ", error)
})

// etnik turizm backend
fetch( `http://navoiytravel.uz/api/etnik/turizm?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let ourEtnik = document.querySelector("#etnik_all_images");
        let ourText = document.querySelector("#etnik_turizm_texts");
        let swapHistorical1 = "";
        let allImgs1 = [];
        allImgs1 = response;
        let allImgsNew = allImgs1[0]?.image_file;
        ourText.innerHTML=`
         ${allImgs1[0]?.title_uzb}
        `
        if(allImgsNew?.length > 0){
          allImgsNew?.map((item) => {
            swapHistorical1 += `
            <div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 col-12 mb-3" data-aos="fade-up" data-aos-duration="800">
              <img src="${item?.image_file}" alt="">
            </div>
            `
          })
          ourEtnik.innerHTML = swapHistorical1
         }
    }).catch(error => {
        console.log("Error : ", error)
})


// bizning tarixiy turizm 

fetch( `http://navoiytravel.uz/api/turizm/turlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
         let gastroSection1 = document.querySelector("#tarixiy_turizm");
         let allTypeData = [];
         allTypeData = response;
         gastroSection1.innerHTML = `
         <div class="col-xl-5 col-lg-6 col-md-6 col-12 mb-4" data-aos="fade-right" data-aos-duration="800">
         <img src="${allTypeData[1]?.image_file}" alt="">
        </div>
        <div class="col-xl-6 col-lg-6 col-md-6 col-12" data-aos="fade-left" data-aos-duration="800">
         <h4>${hash === 'uzb' ? allTypeData[1]?.name_uzb : hash === 'rus' ? allTypeData[3]?.name_ru : hash === 'eng' ? allTypeData[1]?.name_eng : ''}</h4>
         <p class="lng-gastro_p1">${hash === 'uzb' ? allTypeData[1]?.title_uzb : hash === 'rus' ? allTypeData[1]?.title_ru : hash === 'eng' ? allTypeData[1]?.title_eng : ''}</p>
        </div>
         `
    }).catch(error => {
        console.log("Error : ", error)
})

// tarixiy turizm rasmlar

fetch( `http://navoiytravel.uz/api/tarixiy/turizm/rasmlar?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let ourFotoSection = document.querySelector("#tarixiy_turizm_rasm");
        let swapHistorical1 = "";
        let allImgs1 = [];
        allImgs1 = response;
        if(allImgs1?.length > 0){
          allImgs1?.map((item) => {
            swapHistorical1 += `
             <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6 col-12 mb-4" data-aos="fade-up" data-aos-duration="800">
              <img src="${item?.image_file}" alt="">
             </div>
            `
          })
          ourFotoSection.innerHTML = swapHistorical1
        }
    }).catch(error => {
        console.log("Error : ", error)
})


// ekstremal turizm backend
fetch( `http://navoiytravel.uz/api/extremal/turizm?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let ourEtnik = document.querySelector("#extremal_all_images");
        let ourText = document.querySelector("#extremal_text_p");
        let swapHistorical1 = "";
        let allImgs1 = [];
        allImgs1 = response;
        let allImgsNew = allImgs1[0]?.image_file;
        ourText.innerHTML=`
        ${
          hash === 'uzb' ? allImgs1[0]?.title_uzb : hash === 'rus' ? allImgs1[0]?.title_ru : hash === 'eng' ? allImgs1[0]?.title_eng : ''
        }
        `
        if(allImgsNew?.length > 0){
          allImgsNew?.map((item) => {
            swapHistorical1 += `
            <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6 col-12 mb-3" data-aos="fade-right" data-aos-duration="800">
            <img src="${item?.image_file}" alt="">
            </div>
            `
          })
          ourEtnik.innerHTML = swapHistorical1
         }
    }).catch(error => {
        console.log("Error : ", error)
})

// safari turizm backend
fetch( `http://navoiytravel.uz/api/safar/turizm/rasmlar?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let ourEtnik = document.querySelector("#safari_all_images");
        let ourText = document.querySelector("#safari_text_p");
        let swapHistorical1 = "";
        let allImgs1 = [];
        allImgs1 = response;
        let allImgsNew = allImgs1[0]?.image_file;
        ourText.innerHTML=`
        ${
          hash === 'uzb' ? allImgs1[0]?.title_uzb : hash === 'rus' ? allImgs1[0]?.title_ru : hash === 'eng' ? allImgs1[0]?.title_eng : ''
        }
        `
        if(allImgsNew?.length > 0){
          allImgsNew?.map((item) => {
            swapHistorical1 += `
            <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6 col-12 mb-3" data-aos="fade-up" data-aos-duration="800">
             <img src="${item?.image_file}" alt="">
            </div>
            `
          })
          ourEtnik.innerHTML = swapHistorical1
         }
    }).catch(error => {
        console.log("Error : ", error)
})
