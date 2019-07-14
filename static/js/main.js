let mobile_button = document.getElementById("mobile-toggle");
let mobile_menu = document.getElementById("mobile-menu");
let modal = document.getElementById('myModal');
let modalCloseBtn = document.getElementsByClassName("close")[0];
mobile_button.onclick = function () {
      mobile_menu.classList.toggle('is-visible');

}

var error = '<div class="form-error">Обязательно</div>'
function openModal() {
    modal.style.display = "block";
}

modalCloseBtn.onclick = function () {
    modal.style.display = "none";

}

function sendFormStatic() {
    let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].defaultValue
    let name = document.getElementsByName('name')[0]
    let email = document.getElementsByName('email')[0]
    let phone = document.getElementsByName('phone')[0]
    let file = document.getElementsByName('file')[0].files[0]
    let btn = document.getElementById('static_submit')
    let div = document.getElementsByClassName('send_success')[0]
    let label_name = document.getElementById('name')
    let label_phone = document.getElementById('phone')
    let label_email = document.getElementById('email')
        btn.setAttribute('disabled', 'disabled');
        btn.firstChild.data = 'Отправка ...'
        name.classList.remove('error-field')
        phone.classList.remove('error-field')
        email.classList.remove('error-field')
        label_name.innerText = ''
        label_phone.innerText = ''
        label_email.innerText = ''


    let fd = new FormData();

    fd.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
    fd.append('name',name.value)
    fd.append('email',email.value)
    fd.append('phone',phone.value)
    fd.append('file',file)

    let xhr = new XMLHttpRequest();
	xhr.open('POST', '/createform', true);
	xhr.onload = function () {
		console.log(this.response);
            if (JSON.parse(this.response)['result'] === 'ok'){
            btn.style.display = 'none'
            div.style.display = 'block'
            }
            else{
                btn.removeAttribute('disabled')
                btn.firstChild.data = 'отправить'
                if (JSON.parse(this.response)['errors']['name']){
                    label_name.innerText = JSON.parse(this.response)['errors']['name']
                    name.classList.add("error-field");

                }
                if (JSON.parse(this.response)['errors']['phone']){
                    label_phone.innerText = JSON.parse(this.response)['errors']['phone']
                    phone.classList.add("error-field");

                }
                  if (JSON.parse(this.response)['errors']['email']){
                    label_email.innerText = JSON.parse(this.response)['errors']['email']
                    email.classList.add("error-field");

                }

            }
		};
	xhr.send(fd);

}

function sendFormModal(){
    let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].defaultValue
    let name = document.getElementsByName('modal-name')[0]
    let email = document.getElementsByName('modal-email')[0]
    let phone = document.getElementsByName('modal-phone')[0]
    let file = document.getElementsByName('modal-file')[0].files[0]
    let btn = document.getElementById('modal_submit')
    let div = document.getElementsByClassName('modal-send_success')[0]
    let label_name = document.getElementById('modal-name')
    let label_phone = document.getElementById('modal-phone')
    let label_email = document.getElementById('modal-email')
        btn.setAttribute('disabled', 'disabled');
        btn.firstChild.data = 'Отправка ...'
        name.classList.remove('error-field')
        phone.classList.remove('error-field')
        email.classList.remove('error-field')
        label_name.innerText = ''
        label_phone.innerText = ''
        label_email.innerText = ''


    let fd = new FormData();

    fd.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
    fd.append('name',name.value)
    fd.append('email',email.value)
    fd.append('phone',phone.value)
    fd.append('file',file)

    let xhr = new XMLHttpRequest();
	xhr.open('POST', '/createform', true);
	xhr.onload = function () {
		console.log(this.response);
            if (JSON.parse(this.response)['result'] === 'ok'){
            btn.style.display = 'none'
            div.style.display = 'block'
            }
            else{
                btn.removeAttribute('disabled')
                btn.firstChild.data = 'отправить'
                if (JSON.parse(this.response)['errors']['name']){
                    label_name.innerText = JSON.parse(this.response)['errors']['name']
                    name.classList.add("error-field");

                }
                if (JSON.parse(this.response)['errors']['phone']){
                    label_phone.innerText = JSON.parse(this.response)['errors']['phone']
                    phone.classList.add("error-field");

                }
                  if (JSON.parse(this.response)['errors']['email']){
                    label_email.innerText = JSON.parse(this.response)['errors']['email']
                    email.classList.add("error-field");

                }

            }
		};
	xhr.send(fd);
}