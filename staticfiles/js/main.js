function losujKolor() {
    console.log('losuj click');
    let select = document.querySelector("#id_kolor");
    let optionsLenght = select.options.length;
    let randomNuber = getRandom(1, optionsLenght);
    console.log(randomNuber);
    select.options.selectedIndex = randomNuber;
}

function getRandom(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}