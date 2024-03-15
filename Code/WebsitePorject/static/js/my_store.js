"use strict"

// function：get is_logged_in, username, user_type from django session
function checkLogin() {
    console.log('start checking...');
    fetch('/accounts/get_info')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                if (data.user_type === '2') {
                    console.log("User:merchant")
                } else {
                    console.log("Error: user type error");
                    logOut();
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


// function: get data of store and display data
function displayData(){
    // TODO:向后端django发送请求获取以下数据：
    // 1. 商店名字（Store name）
    // 2. 商店地址 (address)
    // 3.商店联系电话 (Phone)
    // 4.商店评分(0到5.0的数字) (Rate)
    // 5.商店总收入Total Income
    // 6.商店总销售量 Total Sales
    // 7.商店中已上架的商品数量
    // 8.商店销售最多的商品名

    // TODO:接收到这些数据后，将其展示在html中
}


$(window).on("load", function() {
    console.log("Loading the page");
    checkLogin();
    displayData();
});