console.log("what up");


if (window.matchMedia("(max-width: 600px)").matches) {
    const timesearch = document.getElementById("mobiledate");
    timesearch.style.display = "block";
  const table2 = document.querySelector("#countryTable2");
  table2.style.display = "none";
  const container = document.querySelector(".statcontainer");
  container.style.display = "block";
  header = document.querySelector("h1");
  header.style.display = "none";
}
function picInsert(path) {
    return `<img src="/static/flags/${path}">`
}
const active = document.getElementById("Active")
active.insertAdjacentHTML("afterbegin", picInsert("sick.png"))
const deaths = document.getElementById("Deaths")
deaths.insertAdjacentHTML("afterbegin", picInsert("death.png"));
const countryname = document.getElementById("countryname").innerHTML;
const country = document.getElementById("country");
country.insertAdjacentHTML("afterbegin", picInsert(countryname.toLowerCase()));

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
