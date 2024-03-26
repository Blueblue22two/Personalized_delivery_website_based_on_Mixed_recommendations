"use strict"// generate star ratings

// get product id
const productIdText = document.getElementById("product-id").textContent;

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

function checkLogin2(){
    console.log('start checking...');
    fetch('/accounts/get_info')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                if (data.user_type === '1') {
                    console.log("")
                } else {
                    console.log("Not customer user type");
                    // Disable the favorite function
                    let favButton = document.getElementById("fav_button");
                    if (favButton) {
                        favButton.disabled = true;
                        favButton.classList.add("disabled");
                    }
                }
            } else {
                console.log("Not logged in");
                // Disable the favorite function
                let favButton = document.getElementById("fav_button");
                if (favButton) {
                    favButton.disabled = true;
                    favButton.classList.add("disabled");
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // Disable the favorite function
            let favButton = document.getElementById("fav_button");
            if (favButton) {
                favButton.disabled = true;
                favButton.classList.add("disabled");
            }
        });
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
    // get product id
    let productId = productIdText.replace('ID:', '').trim();
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
            alert(data.message); // Show the message from the backend
            // Disable the button and change its color to indicate it has been clicked
            let button = document.getElementById("fav_button");
            button.disabled = true;
            button.classList.remove("btn-primary");
            button.classList.add("btn-success");
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}

// event of add to favorite button
document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the favorite button
    let favButton = document.getElementById("fav_button");
    if (favButton) {
        favButton.addEventListener('click', function() {
            addFavorite(); // Call the addFavorite function when the button is clicked
        });
    }
});

$(document).ready(function() {
    checkLogin2();
    getComment();
});