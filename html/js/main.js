let mobile_button = document.getElementById("mobile-toggle");
let mobile_menu = document.getElementById("mobile-menu");
let modal = document.getElementById('myModal');
let modalCloseBtn = document.getElementsByClassName("close")[0];
mobile_button.onclick = function () {
      mobile_menu.classList.toggle('is-visible');

}
function openModal() {
    modal.style.display = "block";
}

modalCloseBtn.onclick = function () {
    modal.style.display = "none";

}

function sendForm() {
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].defaultValue
    console.log (csrf_token)
}