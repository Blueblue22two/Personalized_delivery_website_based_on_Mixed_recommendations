"use strict"// generate star ratings

// get product id
const productIdText = document.getElementById("product-id").textContent;

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

// get all the comment
function getComment() {
    // get product id
    let productId = productIdText.replace('ID:', '').trim();
    let formData = new FormData();
    formData.append('productId', productId);
    $.ajax({
        url: '/products/get_comment/',
        type: 'POST',
        data: formData,
        processData: false, // Important: tell jQuery not to process the data
        contentType: false, // Important: tell jQuery not to set contentType; it will be set automatically with the correct boundary
        headers: {'X-CSRFToken': getCsrfTokenFromForm()},
        success: function(response) {
            var comments = JSON.parse(response.comments);
            var commentsHtml = '';
            // 动态生成评论HTML
            comments.forEach(function(comment) {
                var commentObj = JSON.parse(comment.fields);
                commentsHtml += '<div class="comment py-2 border rounded mb-2">' +
                                '<p><strong>Username:</strong> ' + commentObj.customer + '</p>' +
                                '<p><strong>Rate:</strong> ' + commentObj.rating + ' Stars</p>' +
                                '<p><strong>Comment:</strong> ' + commentObj.text + '</p>' +
                                '</div>';
            });
            // 将生成的评论HTML添加到评论区域
            document.querySelector('.comments-section').innerHTML += commentsHtml;
            console.log("comment set successfully")
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
    getComment();
});