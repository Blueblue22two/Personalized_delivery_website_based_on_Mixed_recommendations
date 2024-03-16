"use strict"
// File: use for the top menu

// function：get is_logged_in, username, user_type from django session
function checkLogin() {
    console.log('start checking...');
    fetch('/accounts/get_info')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                if (data.user_type === '1') {
                    console.log("User:customer")
                    customer_login();
                    display_name(data.username);
                } else if (data.user_type === '2') {
                    console.log("User:merchant")
                    merchant_login();
                    display_name(data.username);
                } else {
                    console.log("User type undefined!");
                    not_login();
                }
            } else {
                console.log("Not logged in");
                not_login();
            }
        })
        .catch(error => {
            console.error('Error:', error);
           not_login();
        });
}


function  not_login(){
    // Hide the shopping cart
    $("#cart").hide();
    // Hide the My account dropdown
    $(".dropdown").hide();
    // Hide the toggle menu
    $(".toggle").hide();
}


function customer_login(){
    $(".toggle").show();
    $(".widget-header:contains('Cart')").show(); // Show shopping cart
    $("#signin").hide();
    $(".dropdown").show(); // Show the My account dropdown
    $("a:contains('My store')").hide();
}


function merchant_login(){
    $(".toggle").show();
    $("#signin").hide();
    $(".widget-header:contains('Cart')").hide();
    $(".dropdown").show(); // Show the My account dropdown
    $("a:contains('Profile')").hide();
    $("a:contains('Favorite')").hide();
}

// 若用户登录则将html中my account中<img></img>中的文字Hi后面加上username
function display_name(name){
    let greetingText = "Hi " + name;
    // Find the element containing the text "Hi" and append the username
    $(".dropdown-toggle").each(function() {
        if ($(this).text().includes("Hi")) {
            $(this).text(function() {
                return $(this).text().replace("Hi", greetingText);
            });
        }
    });
}


$(window).on("load", function() {
    checkLogin();
});