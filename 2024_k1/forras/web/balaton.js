function turizmus(melyik) {
  document.getElementById('turizmusszovegkeret').style.display = 'none';
  document.getElementById('turizmuskepkeret').style.display = 'block';
  document.getElementById('turizmuskep').style.display = 'block';
  document.getElementById('turizmuskep').src = 'kepek/' + melyik + '.jpg';
  document.getElementById('turizmuskep').alt = melyik;
}

function keprejt() {
  document.getElementById('turizmusszovegkeret').style.display = 'block';
  document.getElementById('turizmuskepkeret').style.display = 'none';
  document.getElementById('turizmuskep').style.display = 'none';
}