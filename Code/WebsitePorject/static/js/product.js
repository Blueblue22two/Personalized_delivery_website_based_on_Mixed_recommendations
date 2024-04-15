"use strict"
// get product id
const productIdText = document.getElementById("product-id").textContent;

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

// check user login and user type
function checkLogin2() {
    console.log('start checking...');
    fetch('/accounts/get_info')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                if (data.user_type === '1') {
                    console.log("User type: customer")
                } else {
                    console.log("User type: not customer");
                    displayNotification("Please login as customer to use favorite and cart functions");
                    disableFunctions();
                }
            } else {
                console.log("User not logged in");
                displayNotification("Please login as customer to use favorite and cart functions");
                disableFunctions();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            displayNotification("Please login as customer to use favorite and cart functions");
            disableFunctions();
        });
}

// display notification message
function displayNotification(message) {
    let notification = document.createElement('div');
    notification.style.backgroundColor = 'white';
    notification.style.color = '#FF6666'
    notification.style.padding = '10px';
    notification.style.position = 'fixed'
    notification.style.top = '0';
    notification.style.width = '100%';
    notification.style.textAlign = 'center';
    notification.style.fontSize = '16px';
    notification.style.border = '2px solid lightgreen';
    notification.textContent = message;
    document.body.prepend(notification);
}

// disable button
function disableFunctions() {
    // Disable the favorite function
    let favButton = document.getElementById("fav_button");
    if (favButton) {
        favButton.disabled = true;
        favButton.classList.add("disabled");
    }
    // Disable the cart function
    let cartButton = document.getElementById("cart_button");
    if (cartButton) {
        cartButton.disabled = true;
        cartButton.classList.add("disabled");
    }
}

function generateStars(rating){
    let starsHtml = '';
    for(let i = 0; i < 5; i++){
        starsHtml += `<i class="feather ${i < Math.round(rating) ? 'feather-star text-warning' : 'feather-star'}"></i>`;
    }
    return `<span class="stars">${starsHtml}</span>`;
}

// get all the comment and display it in html
function getComment() {
    let productId = productIdText.replace('ID:', '').trim();
    let formData = new FormData();
    formData.append('productId', productId);
    $.ajax({
        url: '/products/get_comment/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        headers: {'X-CSRFToken': getCsrfTokenFromForm()},
        success: function(response) {
            let comments = response.comments;
            let commentsHtml = '';
            comments.forEach(function(comment) {
                let starRating = generateStars(comment.rating);
                commentsHtml += `
                    <div class="comment py-2 border rounded mb-2 bg-light">
                        <p><strong>Username:</strong> ${comment.customer_username}</p>
                        <p><strong>Rate:</strong> ${starRating} </p>
                        <p><strong>Comment:</strong> ${comment.text}</p>
                    </div>
                `;
            });
            document.querySelector('.comments-section').innerHTML += commentsHtml;
            console.log("Comments set successfully");
        },
        error: function(xhr, status, error) {
            console.log("Error: " + error);
        }
    });
}

// add product to favorite
function addFavorite() {
    console.log("add favorite function...")
    // get product id
    let productId = productIdText.replace('ID:', '').trim();
    console.log('Product ID:', productId);
    let formData = new FormData();
    formData.append('productId', productId);

    $.ajax({
        type: 'POST',
        url: '/customers/add_fav_product/',
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        data: formData,
        processData: false, // Important: tell jQuery not to process the data
        contentType: false, // Important: tell jQuery not to set contentType; it will be set automatically with the correct boundary

        success: function(data) {
            console.log(data.message)
            window.alert(data.message); // Show the message from the backend
            // Disable the button and change its color to indicate it has been clicked
            let button = document.getElementById("fav_button");
            button.disabled = true;
            button.classList.remove("btn-success");
            button.classList.add("btn-primary");
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            window.alert(error);
        }
    });
}


// add this product to shopping cart
function addCart() {
    console.log("add cart function...");
    // get product id
    let productId = productIdText.replace('ID:', '').trim();
    console.log('Product ID:', productId);
    let formData = new FormData();
    formData.append('productId', productId);

    $.ajax({
        type: 'POST',
        url: '/carts/add_cart/',
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            console.log(data.message);
            window.alert(data.message);
            // Disable the button and change its color to indicate it has been clicked
            let button = document.getElementById("cart_button");
            button.disabled = true;
            button.classList.remove("btn-success");
            button.classList.add("btn-primary");
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            window.alert('Failed to add to cart: ' + error);
        }
    });
}


$(document).ready(function() {
    checkLogin2();
    getComment();
    // Add event listener to the favorite button
    $("#fav_button").click(function() {addFavorite();});
    // Add event listener to the cart button
    $("#cart_button").click(function() {addCart();});
});