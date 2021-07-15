console.log("hello");

const th = document.getElementById("1");


const table = document.getElementById("countryTable");
const container = document.querySelector(".statcontainer");
const table2 = document.querySelector("#countryTable2");

if (window.matchMedia("(max-width: 600px)").matches) {
  table.style.display="none";
  container.style.display = "block";
  table2.style.display="none";
}

//document.body.onload = addElement;

/*

function addElement() {
  const newDiv = document.createElement("div");
  newDiv.innerHTML = "{{cases}}";
  const search = document.getElementById("countrySearch");
  document.body.insertBefore(newDiv, search);
}*/
