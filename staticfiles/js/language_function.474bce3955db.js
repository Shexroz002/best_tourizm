const select = document.querySelector('select');
const allLang = ['eng', 'rus', 'uzb']

select.addEventListener('change', changeURLLanguage)

function changeURLLanguage() {
    let lang = select.value;
    location.href = window.location.pathname + '#' + lang;
    location.reload();
}

function changeLanguage() {
    let hash = window.location.hash;
    hash = hash.substring(1)
    // console.log(hash)
    if(!allLang.includes(hash)){
        location.href = window.location.pathname + '#uzb';
        location.reload();
    }
    select.value = hash;
    document.querySelector('title').innerHTML = langArr['unit'][hash];
    for (let key in langArr) {
        let elem = document.querySelector('.lng-' + key);
        if (elem) {
            elem.innerHTML = langArr[key][hash];
        }
    }
}

changeLanguage()
