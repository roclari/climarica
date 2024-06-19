function infoPopup(content) {
    const popup = content.querySelector(".popuptext");
    popup.innerHTML = content.querySelector("span").textContent;
    popup.classList.toggle("show");
  }

  function search() {
    let input = document.getElementById("searchbar").value    // obtém o valor digitado na caixa de pesquisa
    input = input.toLowerCase();   // transforma o valor em letras minúsculas
    let items = document.getElementsByClassName("opt-list");  // obtém todos os elementos com a classe "opt-list"

    for (i = 0; i < items.length; i++) {   // loop for que percorre todos os itens da lista; 'i' é usado para acompanhar a posição atual no loop
      if (!items[i].innerHTML.toLowerCase().includes(input)) {  // verifica se o conteúdo de cada item da lista contém o valor pesquisado
        items[i].style.display="none";   // valor pesquisado não estiver presente no conteúdo do item, não aparece
      }
      else {
        items[i].style.display="list-item";   // faz com que o item seja exibido na página
      }
    }
  }