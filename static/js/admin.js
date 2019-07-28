var el_p=''
var el_h = ''
var header_target = ''
var csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].defaultValue

function changeImg(el) {
    let target = el.dataset.target
    let id = el.dataset.id
    let file = el.files[0]
    let reader = new FileReader();
    reader.onload = function(e) {
        $('#'+target+'_img_'+id).attr('src', e.target.result);
    }
    reader.readAsDataURL(el.files[0]);

    let fd = new FormData();
    fd.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
    fd.append('id',id)
    fd.append('target',target)
    fd.append('image',file)
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/changeImg/', true);
    xhr.onload = function () {
        console.log(JSON.parse(this.response));

    };
    xhr.send(fd);

}

function saveSEO(el) {
    let title= document.getElementById('page_title').value
    let description= document.getElementById('page_description').value
    let keywords= document.getElementById('page_keywords').value
    let target= document.getElementById('page_target').value
    let page_type= document.getElementById('page_type').value

    $.ajax({
        url: "/saveSEO/",
        type: "POST",
        data: ({ csrfmiddlewaretoken: csrfmiddlewaretoken,target: target, page_type:page_type, title: title, description:description, keywords:keywords}),
        dataType: "html",
        success: function(msg) {
            el.innerText = 'СОХРАНЕНО'
        },
        error: function(msg) {

        }
    });

}
function editHeader(el,target) {
    el_h = el
    header_target = target
    let input = document.getElementById(target);
    let senddata_btn = document.getElementById(target+'_btn')
    senddata_btn.dataset.target = target
    el.style.display = "none";
    input.style.display = "flex";

}
function saveHeader(el) {
    let input_div = document.getElementById(header_target);
    let input_val = document.getElementById(header_target+'_input').value
    let target = document.getElementById(header_target+'_btn').dataset.target

    $.ajax({
        url: "/changeHeader/",
        type: "POST",
        data: ({ csrfmiddlewaretoken: csrfmiddlewaretoken,target: target, data: input_val }),
        dataType: "html",
        success: function(msg) {
            input_div.style.display = "none";
            el_h.style.display = "block";
            el_h.innerText = input_val
        },
        error: function(msg) {

        }
    });

}


function closeEditModal() {
    let editmodal = document.getElementById('editModal');
    editmodal.style.display = "none";
}
function editInfo(el,target) {
    el_p = el
    let senddata_btn = document.getElementById('sendData')
    senddata_btn.dataset.target = target
    let editmodal = document.getElementById('editModal');
    let editor = document.getElementById('editor');
    let modal_content = document.getElementById('modal-content')


    editmodal.style.display = "block";
    CKEDITOR.replace( 'editor' );
    CKEDITOR.instances['editor'].setData(el.innerHTML);
}

function sendData() {

    let target = document.getElementById("sendData").dataset.target
    let editmodal = document.getElementById('editModal');
    el_p.innerHTML = CKEDITOR.instances.editor.getData()
    editmodal.style.display = "none";
    console.log( CKEDITOR.instances.editor.getData())


    $.ajax({
        url: "/changeInfo/",
        type: "POST",
        data: ({ csrfmiddlewaretoken: csrfmiddlewaretoken,target: target, data: el_p.innerHTML }),
        dataType: "html",
        success: function(msg) {
            editmodal.style.display = "none";
        },
        error: function(msg) {

        }
    });



}
