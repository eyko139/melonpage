console.log("hello world");
const todoArrow = document.getElementById("todo-arrow");


const todox = document.getElementById("todoClick");
const old = todox.innerHTML;
const todoHoverHandler = () => {
    const todo = document.getElementById("row2");
    const oldInner = todo.innerHTML
    const todoContainer = document.getElementById("todoContainer");
    todoContainer.style.gridArea = "1/2/2/4";
    todo.innerHTML = "You're hovering";
}

const todoLeaverHandler = () => {
    todox.innerHTML = old;
}

todox.addEventListener("mouseover", todoHoverHandler);
todox.addEventListener("mouseleave", todoLeaverHandler);
