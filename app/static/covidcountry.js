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
    return `<img src="/static/${path}">`
}
const active = document.getElementById("Active")
active.insertAdjacentHTML("afterbegin", picInsert("sick.png"))
const deaths = document.getElementById("Deaths")
deaths.insertAdjacentHTML("afterbegin", picInsert("death.png"));
