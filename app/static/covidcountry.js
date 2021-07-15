console.log("what up");


if (window.matchMedia("(max-width: 600px)").matches) {
  const table2 = document.querySelector("#countryTable2");
  table2.style.display = "none";
  const container = document.querySelector(".statcontainer");
  container.style.display = "block";
  header = document.querySelector("h1");
  header.style.display = "none";
}
