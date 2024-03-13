"use strict"
// This file is only used for main.html

// check user is login or not
function checkLogin() {
    console.log('start checking...');
    fetch('/accounts/get_user_info/')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                console.log("Logged in as", data.username);
                console.log("usertype: ", data.user_type);
                if (data.user_type === '1') {
                    customerLogin();
                } else if (data.user_type === '2') {
                    merchantLogin();
                } else {
                    logOut();
                    console.log("User type undefined!");
                }
            } else {
                console.log("Not logged in");
                logOut();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            logOut();
        });
}


function logOut() {
    window.location.href = '/accounts/logout/';
}


function customerLogin(){
    // 显示购物车，个人信息图标
    $(".shopping-cart, .user-info").show();
    // 隐藏商店图标
    $(".store-icon").hide();
}


function merchantLogin(){
    // 显示商店图标
    $(".store-icon").show();
    // 隐藏购物车
    $(".shopping-cart").hide();
    // 隐藏下面这两个东西
    $(".dropdown-item:contains('Information'), .dropdown-item:contains('Favorite')").hide();
}


$(document).on("click", ".dropdown-item:contains('Log out')", function() {
    console.log("Log out")
    logOut();
});

$(window).on("load", function() {
    console.log("Loading the page");
    checkLogin();
});

$(document).ready(function() {
    $('.user-info').hover(
        function() { // Mouse enter event
            $('.dropdown-menu', this).slideDown();
        },
        function() { // Mouse leave event
            $('.dropdown-menu', this).slideUp();
        }
    );
});

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll('.btn');
    buttons.forEach(function(button) {
        button.onmouseover = function() {
            this.style.cursor = 'pointer';
        };
    });
});
