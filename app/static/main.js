console.log("hello world");
const todoArrow = document.getElementById("todo-arrow");
const todoLink2 = document.getElementById("todoLink");
if (window.matchMedia("(max-width: 600px)").matches) {
  todoLink2.href = "javascript:void(0)";
}
//Translate the Todo Icon
const todoInit = document.getElementById("todoContainer").getBoundingClientRect();
if (window.matchMedia("(max-width: 600px)").matches) {
  document.getElementById("todoContainer").style.gridArea = "1/2/2/4";
};
const todoLast = document.getElementById("todoContainer").getBoundingClientRect();

//document.getElementById("todoContainer").style.gridArea = "1/1/2/4";

const translateX = todoInit.left - todoLast.left+50;
const translateY = todoInit.top - todoLast.top+40;
const scaleX = todoInit.width / todoLast.width;
const scaleY = todoInit.height / todoLast.height;

if (window.matchMedia("(max-width: 600px)").matches){
  const trans = document.getElementById("todoContainer").style.transform = `translate(${translateX}px, ${translateY}px) scale(${scaleX}, ${scaleY})`
};

const TodoIcon = document.getElementById("todoContainer");
const todox = document.getElementById("todoClick");
const small = document.getElementById("small-links");
console.log(small);
if (window.matchMedia("(max-width: 600px)").matches) {
  small.style.left = "-150px";
} else{
  small.style.right="-250px";
  small.style.display = "none";
};
console.log(small.style.left);
const old = todox.innerHTML;
const todoHoverHandler = () => {
    if (window.matchMedia("(max-width: 600px)") && small.style.left=="-150px"){
      TodoIcon.style.transition = "transform 0.5s";
      TodoIcon.style.transform = "";
      TodoIcon.style.position = "relative";
      TodoIcon.style.left = "30px";
      small.style.transition = "all 0.5s ease-in 0s";
      small.style.left = "35px";
    }};

const todoLeaverHandler = () => {
    todox.innerHTML = old;
}

todox.addEventListener("click", todoHoverHandler);
todox.addEventListener("mouseleave", todoLeaverHandler);
