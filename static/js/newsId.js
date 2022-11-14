const hash = window.location.hash.substring(1);

const NewsWrapper = document.querySelector(".big-card");
const newBannerText = document.querySelector("#mainBannerNew");
const newHomeCard = document.querySelector("#newTextHomePage");
class News {
  constructor(date, id, image_file, name, title) {
    this.date = date;
    this.id = id;
    this.image_file = image_file;
    this.name = name;
    this.title = title;
  }

  render() {
    NewsWrapper.innerHTML += `<img src="${this.image_file[0]?.image_file}" alt="${this.image_file[0]?.name}">
    <div class="info-time">
      <p>
         ${new Date(this.date).toLocaleDateString()}
      </p>
      <span>|</span>
      <p>
         <i class="uil uil-eye"></i>
         <span>100</span>
      </p>
    </div>
    <h5>"${this.name}"</h5>
    <p>${this.title}</p>
    <div class="img-info">
      ${
        this.image_file?.map(item => {
          return(
             `<img src="${item?.image_file}" alt="${item?.name}">`
          )
        })
      }
    </div>`;
    newBannerText.innerHTML = `
      <h1>${this.name}</h1>
    `
    newHomeCard.innerHTML = `
      ${this.name} 
    `
  }
}

const getNews = async (id) => {
  try {
    const response = await fetch(
      `http://navoiytravel.uz/api/yangiliklar/${id}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
};

document.addEventListener("DOMContentLoaded", async function () {
  // get id from url by query string
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get("id").replace("/", "");
  console.log('id',id)
  const news = [await getNews(id)];
  news.forEach((item) => {
    let news;
    if (hash === "uzb") {
      news = new News(
        item.date,
        item.id,
        item.image_file,
        item.name_uzb,
        item.title_uzb
      );
    } else if (hash === "rus") {
      news = new News(
        item.date,
        item.id,
        item.image_file,
        item.name_ru,
        item.title_ru
      );
    } else {
      news = new News(
        item.date,
        item.id,
        item.image_file,
        item.name_eng,
        item.title_eng
      );
    }

    news.render();
  });
});



// yangililar : 
fetch( `http://navoiytravel.uz/api/yangiliklar`)
    .then( response => response.json() )
    .then(response => {
      console.log(response)
        let museumSection = document.querySelector("#lastNews");
        let swapMuseum = "";
        let allImgs = [];
        allImgs = response;
        if(allImgs?.length > 0){
          allImgs?.map((item, index) => {
            swapMuseum += `
            <li>
            <div class="img-news-about">
                <img src="${item?.image_file[0]?.image_file}" alt="">
            </div>  
            <div class="news-about-text">
                <span>${new Date(item?.date).toLocaleDateString()}</span>
                <a href="/news/detail/?id=${
                  item.id
                }/#${hash}">${item?.name_uzb}</a>
                <div class="news-card1-eye">
                    <i class="uil uil-eye"></i>
                    <span>100</span>
                </div>
            </div>
        </li>
            `
          })
         
          museumSection.innerHTML=swapMuseum;
        }
    }).catch(error => {
        console.log("Error : ", error)
})