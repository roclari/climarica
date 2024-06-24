function infoPopup(content) {
    const popup = content.querySelector(".popuptext");
    popup.innerHTML = content.querySelector("span").textContent;
    popup.classList.toggle("show");
  }

  function search() {
    let input = document.getElementById("searchbar").value
    input = input.toLowerCase();
    let items = document.getElementsByClassName("opt-list");
    for (i = 0; i < items.length; i++) {
      if (!items[i].innerHTML.toLowerCase().includes(input)) {
        items[i].style.display="none";
      }
      else {
        items[i].style.display="list-item";
      }
    }
  }