$(document).ready(function() {


$("input[type=radio][name=components]").on('change', function() {
    var componentChoice = $("input[type=radio][name=components]:checked").val();
    if (componentChoice == "alloy") {
        $("#price-alloy, #weight-alloy").removeClass("price-muted").addClass("text-white").change(); 
        $("#price-carbon, #weight-carbon").removeClass("text-white").addClass("price-muted").change();
    }
    else if (componentChoice == "carbon") {
        $("#price-carbon, #weight-carbon").removeClass("price-muted").addClass("text-white").change(); 
        $("#price-alloy, #weight-alloy").removeClass("text-white").addClass("price-muted").change();
    }
});

});