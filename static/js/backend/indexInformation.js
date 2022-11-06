let hash = window.location.hash;
hash = hash.substring(1)

//tarixiy joylar
fetch( `https://navoiytourizm.pythonanywhere.com/api/tarixiy/turizm/rasmlar?language=${hash}`)
    .then( response => response.json() )
    .then(response => {
        let historicalSection = document.querySelector("#tarixiy_joylar");
        let swapHistorical = "";
        let allImgs = [];
        allImgs = response;
        if(allImgs?.length > 0){
          allImgs?.map((item) => {
            swapHistorical += `
            <div class="swiper-slide">
              <img src="${item?.image_file}" />
              <h3>${hash === 'uzb' ? item?.name_uzb: ''}</h3>
              <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus, pariatur!</p>
            </div>
            `
          })
          historicalSection.innerHTML = swapHistorical
        }
       console.log("Tarixiy joylar : ", response)
    }).catch(error => {
        console.log("Error : ", error)
})

// bizning galereyamiz
fetch( `https://navoiytourizm.pythonanywhere.com/api/bizning/galeryamiz`)
    .then( response => response.json() )
    .then(response => {
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
fetch( `https://navoiytourizm.pythonanywhere.com/api/client/bilan/boglanish?language=${hash}`)
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
      fetch(`https://navoiytourizm.pythonanywhere.com/api/biz/bilan/boglanish`, {
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