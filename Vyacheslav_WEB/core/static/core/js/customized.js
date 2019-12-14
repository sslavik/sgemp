// TOGGLE
$(document).ready(function() {
    $('.button.toggle').click(function() {
        var toggle= $(this);
        var _height;
        if ($(this).next("#box_service").hasClass("show")) {
            toggle.text("Complementos");
            $(this).next("#box_service").removeClass("show");
        }
        else {
            toggle.text("Ocultar");
            $(this).next("#box_service").addClass("show");
        }
    });
  });
// VIDEO
