$(document).ready(function () {
    $('nav-link').click(function () {
        $(this).parent().siblings('li').removeClass('active');
        $(this).parent().addClass('active');
    });
});
