let hash = window.location.hash;
hash = hash.substring(1)
//console.log("hash : ", hash)

// fetch( `https://cors-anywhere.herokuapp.com/navoiytourizm.pythonanywhere.com/api/logistika/turlari?language=${hash}`)
//     .then( response => response.json() )
//     .then(response => {
//         let ourFotoSection = document.querySelector("#logistika_turlari");
//         let swapHistorical1 = "";
//         let allImgs1 = [];
//         allImgs1 = response;
//         if(allImgs1?.length > 0){
//           allImgs1?.map((item, index) => {
//             swapHistorical1 += `
//             <div class="col-4" data-aos="fade-right" data-aos-duration="800">
//                 <h3><span>0${index+1}.</span><span>${item?.name_uzb}</span></h3>
//                 <img src="./../images/log-type1.jpg" alt="">
//                 <p>${item?.title_uzb}</p>
//             </div>
//             `
//           })
//           ourFotoSection.innerHTML = swapHistorical1
       
//          }
//     }).catch(error => {
//         console.log("Error : ", error)
// })
