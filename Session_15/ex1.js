const $ulElement = document.querySelector('ul');

$ulElement.addEventListener("click",(e)=>{
    const $target = e.target;
    if($target.classList.contains('close')){
        const $parentTarget = $target.parentElement;
        $parentTarget.style.display = "none";
        console.dir($parentTarget)
        const deleteItem = $parentTarget.childNodes[1].innerText;
        deleteTodoList('todoList', deleteItem);
    }
    $target.classList.toggle('checked');
})

function newElement() {
    const inputValue = document.getElementById("myInput").value;
    const $liElement = `
        <li>
            <span>${inputValue}</span>
            <span class="close">&#215;</span>
        </li>
    `

    if (inputValue === '') {
        alert("You must write something!");
    } else {
        $ulElement.insertAdjacentHTML('beforeend', $liElement);
        addTodoList('todoList', inputValue)
    }
    document.getElementById("myInput").value = "";
}


function init() {
    let todoList = getTodoList('todoList');
    for(let i=0; i<todoList.length; i++){
        $liElement = `
            <li>
                <span>${todoList[i]}</span>
                <span class="close">&#215;</span>
            </li>
        `
        $ulElement.insertAdjacentHTML('beforeend', $liElement);
    }
}

function getTodoList(key) {
    return localStorage.getItem(key) ? localStorage.getItem(key).split(',') : [];
}

function addTodoList(key, value) {
    const todoList = getTodoList(key)
    return localStorage.setItem(key,[...todoList, value])
}

function deleteTodoList(key,value) {
    const todoList = getTodoList(key)
    return localStorage.setItem(key,todoList.filter(todo => todo !== value))
}

init()

function myFunction () {
    const x = document.getElementById ("click");
    if (x.style.disply === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

const modal = document.getElementById("myModal");
const btn = document.getElementById("myBtn");
const span = document.getElementsByClassName ("close");

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}