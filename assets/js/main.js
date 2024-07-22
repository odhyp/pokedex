// Give header a shadow after scrolling
function toggleHeaderShadow() {
  let e = document.querySelector("#my-header");
  window.scrollY > 0 ? e.classList.add("shadow") : e.classList.remove("shadow");
}

window.addEventListener("scroll", toggleHeaderShadow);
