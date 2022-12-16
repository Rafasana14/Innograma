var goBtn = document.getElementById("goBtn");
var menu = document.getElementById("year-select");

goBtn.onclick = function() {
  window.location = menu.value;
}