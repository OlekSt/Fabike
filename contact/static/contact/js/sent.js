$(document).ready(function() {

    $("#contact-send").on('click', function() {
        console.log("visible to invisible")
        $("#message-hello").removeClass("visible").addClass("invisible"); 
        $("#message-sent").removeClass("invisible").addClass("visible");
    }
    );

});