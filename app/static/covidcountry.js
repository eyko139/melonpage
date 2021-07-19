console.log("what up");


if (window.matchMedia("(max-width: 600px)").matches) {
  let header = document.querySelector("h1");
  document.querySelector(".btn").innerHTML = "Update";
  const breaks = document.querySelectorAll("br");
  breaks.forEach(element=> {
    element.remove()});
}
function picInsert(path) {
    return `<img src="/static/flags/${path}">`
}
//Inserting flag pics
const active = document.getElementById("Active")
active.insertAdjacentHTML("afterbegin", picInsert("sick.png"))
const deaths = document.getElementById("Deaths")
deaths.insertAdjacentHTML("afterbegin", picInsert("death.png"));
const countryname = document.getElementById("countryname").innerHTML;
let header = document.querySelector("h1");
header.insertAdjacentHTML("afterbegin", picInsert(countryname.toLowerCase()));

date_panel = document.getElementById("Date-h")
temp_inner = date_panel.innerHTML
document.getElementById("Date-h").innerHTML = "National Numbers for "+temp_inner;

//Change the placeholder values of both Graph search bars when queried
const queried_value = document.getElementById("javaproxy").innerHTML;
const form_select = document.querySelector(`option[value="${queried_value}"]`);
form_select.setAttribute("selected", "");

const queried_days = document.getElementById("javaproxy2").innerHTML;
const days_select = document.getElementById("country-days-select");
days_select.setAttribute("placeholder", `Interval (${queried_days})`);
