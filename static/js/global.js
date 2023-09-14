const mobileMenuToggle = document.querySelector('#mobile-menu-toggle');
const closeOffCanvasBtn = document.querySelector('#btn-close-off-canvas');
const offCanvasMenu = document.querySelector('#nav-off-canvas');


function toggleMobileMenu() {
    offCanvasMenu.classList.toggle('show');
}
mobileMenuToggle.addEventListener('click', toggleMobileMenu);
closeOffCanvasBtn.addEventListener('click', toggleMobileMenu);