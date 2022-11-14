const hash = window.location.hash.substring(1);

const SliderWrapper = document.querySelector("#news-slider");

const getAllNews = async () => {
  try {
    const response = await fetch(
      `http://navoiytravel.uz/api/yangiliklar?language=${hash}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    const data = await response.json();
    console.log(data)
    return data;
  } catch (error) {
    console.log(error);
  }
};

class News {
  constructor(date, id, image_file, name, title) {
    this.date = date;
    this.id = id;
    this.image_file = image_file;
    this.name = name;
    this.title = title;
  }

  render() {
    SliderWrapper.innerHTML += `<div class="swiper-slide">
    <a href="/news/detail/?id=${this.id}/#${hash}">
      <div class="news-img">
        <div class="news-img-text">
          <img src="${this.image_file[0].image_file}" />
        </div>
        <div class="img-news-text">
          <div class="img-news-text">
            <div class="news-icons-hover">
              <i class="uil uil-search"></i> 
              <div class="eye-icons">
                <i class="uil uil-eye"></i>
                <span>100</span>
              </div>
            </div>
          </div>
        </div>
      </div> 
      <h3>${this.name}</h3>
    </a>
    <p class="ellipsesTextDate">${this.title}</p>
    <div class="icons-date">
      <i class="uil uil-calendar-alt"></i>
      <p>${new Date(this.date).toLocaleDateString()}</p>
    </div>
    <div class="box-btn-news"><a href="/news/detail/?id=${
      this.id
    }/#${hash}" class="btn-news">Batafsil</a></div> 
  </div>`;
  }
}

document.addEventListener("DOMContentLoaded", async function () {
  const news = (await getAllNews()) || [];
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
