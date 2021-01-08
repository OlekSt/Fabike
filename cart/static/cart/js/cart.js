$(document).ready(function() {

    let colorChoice = $("input[type=radio][name=color]:checked").val();
    let sizeChoice = $("input[type=radio][name=size]:checked").val();
    componentsChoice = $("input[type=radio][name=components]:checked").val();
    console.log(colorChoice, sizeChoice, componentsChoice);
    
    $("input[type=radio][name=color]").on('change', function() {
        colorChoice = $("input[type=radio][name=color]:checked").val();
        return colorChoice;
    });
    $("input[type=radio][name=size]").on('change', function() {
        sizeChoice = $("input[type=radio][name=size]:checked").val();
        return sizeChoice;
    });
    $("input[type=radio][name=components]").on('change', function() {
        componentsChoice = $("input[type=radio][name=components]:checked").val();
        return componentsChoice;
    });
    $("#add_cart_btn").on('click', function() {
        console.log(colorChoice, sizeChoice, componentsChoice);
    });

}); 


    