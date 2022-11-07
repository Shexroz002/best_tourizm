let hash = window.location.hash;
hash = hash.substring(1)

// bizning gastro turizm 1

fetch( `https://navoiytourizm.pythonanywhere.com/api/turizm/turlari?language=${hash}`)
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

fetch( `https://navoiytourizm.pythonanywhere.com/api/turizm/turlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
         let gastroSection1 = document.querySelector("#gastro_turizm2");
         let allTypeData = [];
         allTypeData = response;
         gastroSection1.innerHTML = `
          <div class="col-xl-6 col-lg-6 col-md-6 col-12 gastro-text mb-4" data-aos="fade-left" data-aos-duration="800">
           <h4>${hash === 'uzb' ? allTypeData[1]?.name_uzb : hash === 'rus' ? allTypeData[1]?.name_ru : hash === 'eng' ? allTypeData[1]?.name_eng : ''}</h4>
           <p class="lng-gastro_p1">${hash === 'uzb' ? allTypeData[1]?.title_uzb : hash === 'rus' ? allTypeData[1]?.title_ru : hash === 'eng' ? allTypeData[1]?.title_eng : ''}</p>
          </div>
          <div class="col-xl-5 col-lg-6 col-md-6 col-12 gastro-img" data-aos="fade-right" data-aos-duration="800">
            <img src="${allTypeData[1]?.image_file}" alt="">
          </div>
         `
    }).catch(error => {
        console.log("Error : ", error)
})

// bizning tarixiy turizm 

fetch( `https://navoiytourizm.pythonanywhere.com/api/turizm/turlari?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
         let gastroSection1 = document.querySelector("#tarixiy_turizm");
         let allTypeData = [];
         allTypeData = response;
         gastroSection1.innerHTML = `
         <div class="col-xl-5 col-lg-6 col-md-6 col-12 mb-4" data-aos="fade-right" data-aos-duration="800">
         <img src="${allTypeData[3]?.image_file}" alt="">
        </div>
        <div class="col-xl-6 col-lg-6 col-md-6 col-12" data-aos="fade-left" data-aos-duration="800">
         <h4>${hash === 'uzb' ? allTypeData[3]?.name_uzb : hash === 'rus' ? allTypeData[3]?.name_ru : hash === 'eng' ? allTypeData[3]?.name_eng : ''}</h4>
         <p class="lng-gastro_p1">${hash === 'uzb' ? allTypeData[3]?.title_uzb : hash === 'rus' ? allTypeData[3]?.title_ru : hash === 'eng' ? allTypeData[3]?.title_eng : ''}</p>
        </div>
         `
    }).catch(error => {
        console.log("Error : ", error)
})

// tarixiy turizm rasmlar

fetch( `https://navoiytourizm.pythonanywhere.com/api/tarixiy/turizm/rasmlar?language=${hash}`)
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
