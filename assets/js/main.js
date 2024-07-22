// Give header a shadow after scrolling
function toggleHeaderShadow() {
  let e = document.querySelector("#my-header");
  window.scrollY > 0 ? e.classList.add("shadow") : e.classList.remove("shadow");
}

window.addEventListener("scroll", toggleHeaderShadow);

// Give main a margin-top to account for navbar height
document.addEventListener('DOMContentLoaded', function() {
  var navbar = document.getElementById('my-header');
  var main = document.getElementById('main-section');

  function adjustMarginTop() {
    var navbarHeight = navbar.offsetHeight;
    main.style.marginTop = (navbarHeight * 2) + 'px';
  }

  adjustMarginTop();

  window.addEventListener('resize', adjustMarginTop);
});
