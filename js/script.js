function ScrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

var btnScrollToTop_index = document.getElementById("scroll-to-top-index")



window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        btnScrollToTop_index.classList.add("d-block")
        btnScrollToTop_index.classList.remove("d-none")
    } else {
        btnScrollToTop_index.classList.add("d-none")
        btnScrollToTop_index.classList.remove("d-block")
    }
}