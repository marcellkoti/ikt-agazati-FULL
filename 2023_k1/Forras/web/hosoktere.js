function alapallapot() {
    var kezdokep = document.getElementById('inditokep');
    kiemeles(kezdokep);
}

function kiemeles(element) {
    document.getElementById('kiemelt-kep').style.backgroundImage = "url(" + element.src + ")";
    document.getElementById('kiemelt-nev').innerText = element.alt;
}

function nagyit(szorzo) {
    document.getElementById('nyil-fel').style.height = szorzo + 'px';
}
