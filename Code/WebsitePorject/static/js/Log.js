// Login, logout
// Check whether the user is logged in
"use strict"

// check user is login or not
function checkLogin() {
    console.log('start checking...')
    var user = getCookie('username');
    if (user) {
        let type = getCookie('user_type');
        if(type==='1'){
            customerLogin();
        }else if(type==='2'){
            merchantLogin();
        }else{
            logOut();
            console.log("user type undefined!");
            return;
        }
    } else {
        console.log("Not logged in");
        logOut();
    }
}

// get Cookie
function getCookie(name) {
    var cookies = document.cookie.split(';'); // Split them into an array
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.indexOf(name) === 0) {
        return cookie.substring(name.length + 1, cookie.length);
        }
    }
    return null;
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
    //  <a class="dropdown-item" href="#">Information</a>
    //  <a class="dropdown-item" href="#">Favorite</a>
    $(".dropdown-item:contains('Information'), .dropdown-item:contains('Favorite')").hide();
    // TODO:隐藏搜索框
}


function logOut(){
    // delete cookie
    document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = "user_type=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    // redirect to index
    window.location.href = '/'; // Replace 'index.html' with your index page URL
}

// 添加事件当用户点击按钮Logout时触发这个函数
$(document).on("click", ".dropdown-item:contains('Log out')", function() {
    console.log("Log out")
    logOut();
});

window.addEventListener("load", function() {
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
