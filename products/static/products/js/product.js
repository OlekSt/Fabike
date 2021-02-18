$(document).ready(function() {

    $("input[type=radio][name=components]").on('change', function() {
        var componentChoice = $("[name=components]:checked").val();
        if (componentChoice == "alloy") {
            $("#price_alloy, #weight_alloy").removeClass("price-muted").addClass("text-white").change(); 
            $("#price_carbon, #weight_carbon").removeClass("text-white").addClass("price-muted").change();
        }
        else if (componentChoice == "carbon") {
            $("#price_carbon, #weight_carbon").removeClass("price-muted").addClass("text-white").change(); 
            $("#price_alloy, #weight_alloy").removeClass("text-white").addClass("price-muted").change();
        }
    });

});