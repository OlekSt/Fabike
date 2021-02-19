$(document).ready(function () {
    //Sets fields ONLOAD
    let productTypeChoice = $("#id_product_type").val();
    if (productTypeChoice == "FRAMES") {
        // to hide fields which are only for bikes
        $("#div_id_wheels, #div_id_tyres, #div_id_crankset, #div_id_shift_levers, #div_id_derailleurs, #div_id_casette_or_sprocket, #div_id_chain_or_belt, #div_id_handlebar, #div_id_stem, #div_id_saddle, #div_id_seatpost, #div_id_price_alloy, #div_id_price_carbon, #div_id_weight_carbon, #div_id_weight_alloy").hide();
        // set IS BIKE To NO for Frames
        $("#id_is_bike").val("false").change();
        // make frame-related fields required to fill in
        $("#id_headset, #id_seat_clamp, #id_bottom_bracket, #id_seatpost_diameter, #id_dropouts, #id_max_tyre_size, #id_price, #id_weight").attr("required", true);
    }
    // to hide fields which are only for frames
    else if (productTypeChoice == "BIKES") {
        $("#div_id_headset, #div_id_seat_clamp, #div_id_bottom_bracket, #div_id_seatpost_diameter, #div_id_dropouts, #div_id_max_tyre_size, #div_id_price, #div_id_weight").hide(); 
        // make bike-related fields required to fill in
        $("#id_wheels, #id_tyres, #id_crankset, #id_shift_levers, #id_derailleurs, #id_casette_or_sprocket, #id_chain_or_belt, #id_handlebar, #id_stem, #id_saddle, #id_seatpost, #id_price_alloy, #id_price_carbon, #id_weight_carbon, #id_weight_alloy").attr("required", true);
    }
    //Updates fields visibility based on users' choice
    $("#id_product_type").change(function() {
        var productTypeChoice = $("#id_product_type").val();
        if (productTypeChoice == "BIKES") {
            // On user's choice to show fields which are only for bikes
            $("#div_id_wheels, #div_id_tyres, #div_id_crankset, #div_id_shift_levers, #div_id_derailleurs, #div_id_casette_or_sprocket, #div_id_chain_or_belt, #div_id_handlebar, #div_id_stem, #div_id_saddle, #div_id_seatpost, #div_id_price_alloy, #div_id_price_carbon, #div_id_weight_carbon, #div_id_weight_alloy").show(); 

            // to make all bike-related fields reuired on BIKES choice change
            $("#id_wheels, #id_tyres, #id_crankset, #id_shift_levers, #id_derailleurs, #id_casette_or_sprocket, #id_chain_or_belt, #id_handlebar, #id_stem, #id_saddle, #id_seatpost, #id_price_alloy, #id_price_carbon, #id_weight_carbon, #id_weight_alloy").attr("required", true);
            
            // show YES for bikes
            $("#id_is_bike").val("true").change();
            
            // On user's choice to hide fields for frames
            $("#div_id_headset, #div_id_seat_clamp, #div_id_bottom_bracket, #div_id_seatpost_diameter, #div_id_dropouts, #div_id_max_tyre_size, #div_id_price, #div_id_weight").hide(); 
            
            // to make all frame-related fields NON-reuired on BIKES choice change
            $("#id_headset, #id_seat_clamp, #id_bottom_bracket, #id_seatpost_diameter, #id_dropouts, #id_max_tyre_size, #id_price, #id_weight").attr("required", false);
        }
        else if (productTypeChoice == "FRAMES") {
            // On user's choice to hide fields which are only for bikes
            $("#div_id_wheels, #div_id_tyres, #div_id_crankset, #div_id_shift_levers, #div_id_derailleurs, #div_id_casette_or_sprocket, #div_id_chain_or_belt, #div_id_handlebar, #div_id_stem, #div_id_saddle, #div_id_seatpost, #div_id_price_alloy, #div_id_price_carbon, #div_id_weight_carbon, #div_id_weight_alloy").hide(); 
            
            // to make all bike-related fields NON-required on FRAMES choice change
            $("#id_wheels, #id_tyres, #id_crankset, #id_shift_levers, #id_derailleurs, #id_casette_or_sprocket, #id_chain_or_belt, #id_handlebar, #id_stem, #id_saddle, #id_seatpost, #id_price_alloy, #id_price_carbon, #id_weight_carbon, #id_weight_alloy").attr("required", false);
            
            // to show NO for frames
            $("#id_is_bike").val("false").change();
           
            // On user's choice to show fields for frames
            $("#div_id_headset, #div_id_seat_clamp, #div_id_bottom_bracket, #div_id_seatpost_diameter, #div_id_dropouts, #div_id_max_tyre_size, #div_id_price, #div_id_weight").show(); 
            
            // to make all frame-related fields required on FRAMES choice change
            $("#id_headset, #id_seat_clamp, #id_bottom_bracket, #id_seatpost_diameter, #id_dropouts, #id_max_tyre_size, #id_price, #id_weight").attr("required", true);
        }
    });
});