$(document).ready(function () {
    let productTypeChoice = $("#id_product_type").val();
    if (productTypeChoice == "FRAMES") {
        // Onload to hide fields which are only for bikes
        $("#div_id_wheels, #div_id_tyres, #div_id_crankset, #div_id_shift_levers, #div_id_derailleurs, #div_id_casette_or_sprocket, #div_id_chain_or_belt, #div_id_handlebar, #div_id_stem, #div_id_saddle, #div_id_seatpost, #div_id_price_alloy, #div_id_price_carbon, #div_id_weight_carbon, #div_id_weight_alloy").hide();
    }
    // Onload to hide fields which are only for frames
    else if (productTypeChoice == "BIKES") {
        $("#div_id_headset, #div_id_seat_clamp, #div_id_bottom_bracket, #div_id_seatpost_diameter, #div_id_dropouts, #div_id_max_tyre_size, #div_id_price, #div_id_weight").hide(); 
    }
    //Updated fields visibility based on users' choice
    $("#id_product_type").change( function() {
        var productTypeChoice = $("#id_product_type").val();
        if (productTypeChoice == "BIKES") {
            // On user's choice to show fields which are only for bikes
            $("#div_id_wheels, #div_id_tyres, #div_id_crankset, #div_id_shift_levers, #div_id_derailleurs, #div_id_casette_or_sprocket, #div_id_chain_or_belt, #div_id_handlebar, #div_id_stem, #div_id_saddle, #div_id_seatpost, #div_id_price_alloy, #div_id_price_carbon, #div_id_weight_carbon, #div_id_weight_alloy").show(); 
            // On user's choice to hide fields for frames
            $("#div_id_headset, #div_id_seat_clamp, #div_id_bottom_bracket, #div_id_seatpost_diameter, #div_id_dropouts, #div_id_max_tyre_size, #div_id_price, #div_id_weight").hide(); 
        }
        else if (productTypeChoice == "FRAMES") {
            // On user's choice to hide fields which are only for bikes
            $("#div_id_wheels, #div_id_tyres, #div_id_crankset, #div_id_shift_levers, #div_id_derailleurs, #div_id_casette_or_sprocket, #div_id_chain_or_belt, #div_id_handlebar, #div_id_stem, #div_id_saddle, #div_id_seatpost, #div_id_price_alloy, #div_id_price_carbon, #div_id_weight_carbon, #div_id_weight_alloy").hide(); 
            // On user's choice to show fields for frames
            $("#div_id_headset, #div_id_seat_clamp, #div_id_bottom_bracket, #div_id_seatpost_diameter, #div_id_dropouts, #div_id_max_tyre_size, #div_id_price, #div_id_weight").show(); 
        }
    });
});