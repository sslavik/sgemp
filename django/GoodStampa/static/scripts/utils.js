function changeActive(elem) {
    // get all 'a' elements
    var nav = document.getElementsByClassName('nav-item');
    // loop through all 'a' elements
    for (i = 0; i < nav.length; i++) {
        // Remove the class 'active' if it exists
        nav[i].classList.remove('active')
    }
    // add 'active' classs to the element that was clicked
    elem.parentElement.classList.add('active');
}