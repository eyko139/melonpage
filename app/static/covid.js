console.log("hello");

const th = document.getElementById("1");


const table = document.getElementById("countryTable");
const container = document.querySelector(".statcontainer");
const table2 = document.querySelector("#countryTable2");

if (window.matchMedia("(max-width: 600px)").matches) {
  //table.style.display="none";
  //container.style.display = "block";
  //table2.style.display="none";
  const button = document.getElementById("update-button");
  button.innerHTML = "Display";
  const worlddiv = document.getElementById("country");
  worlddiv.style.display = "none";
}

//document.body.onload = addElement;

/*

function addElement() {
  const newDiv = document.createElement("div");
  newDiv.innerHTML = "{{cases}}";
  const search = document.getElementById("countrySearch");
  document.body.insertBefore(newDiv, search);
}*/
function picInsert(path) {
    return `<img src="/static/flags/${path}">`
}
console.log(picInsert("corona.png"));
const bla = '<img href=\"{{url_for(\"static}\", filename=\"corona.png\")}}\">'
const confirmed = document.getElementById("New Confirmed");
confirmed.insertAdjacentHTML("afterbegin", picInsert("corona.png"));
const dead = document.getElementById("New Deaths");
dead.insertAdjacentHTML("afterbegin", picInsert("death.png"));

const queried_value = document.getElementById("javaproxy").innerHTML;
const form_select = document.querySelector(`option[value="${queried_value}"]`);
form_select.setAttribute("selected", "");

const queried_days = document.getElementById("javaproxy2").innerHTML;
const days_select = document.getElementById("world-days-select");
days_select.setAttribute("placeholder", `Interval (current: ${queried_days})`);


