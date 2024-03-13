"use strict"
// This file is different with Log.js
// The code in this file is generally applicable to most of the code in the project

// check user is login or not
function checkLogin() {
    console.log('start checking...');
    fetch('/accounts/get_user_info/')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                if (data.user_type === '1') {
                    console.log("User:customer")
                } else if (data.user_type === '2') {
                    console.log("User:merchant")
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


$(window).on("load", function() {
    console.log("Loading the page");
    checkLogin();
});