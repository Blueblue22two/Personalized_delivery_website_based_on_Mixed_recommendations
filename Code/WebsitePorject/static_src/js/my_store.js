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

// receive data and display it in html
function displayData(){
    console.log("ready to display")
    $.ajax({
        url: '/merchants/my_store/get_info',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log("get successfully")
            // display all data
            $('#storeName').val(data.storeName);
            $('#storeAddress').val(data.address);
            $('#storePhone').val(data.phone);
            $('#storeRate').val(data.rate);
            $('#storeIncome').val(data.totalIncome);
            $('#storeSales').val(data.totalSales);
            $('#totalProducts').val(data.totalProducts);
            $('#topSellingProduct').val(data.topSellingProduct);
            $('#favNumber').val(data.favNumber);
            $('#orderNumber').val(data.orderNumber);
            // add the store url to html
            var storeLinkHtml = `<a class="dropdown-item" href="/store/shop/${data.storeName}/">Visit ${data.storeName}</a>`;
            $('#storeLinkContainer').html(storeLinkHtml);
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
}


$(document).ready(function() {
    displayData();
});

$(window).on("load", function() {
    console.log("Loading the page");
    checkLogin();
});