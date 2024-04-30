"use strict"

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}


// generate star ratings
function generateStars(rating){
    let starsHtml = '';
    for(let i = 0; i < 5; i++){
        starsHtml += `<i class="feather-star ${i < Math.round(rating) ? 'star_active' : ''}"></i>`;
    }
    return `<li>${starsHtml}</li>`;
}


// function to dynamically create shop or product card
function createCard(item, type) {
    let cardHtml = '';
    if (type === 'shop') {
        cardHtml = `
            <div class="col-md-3 pb-3">
                <div class="list-card bg-white h-100 rounded overflow-hidden position-relative shadow-sm">
                    <div class="list-card-image">
                        <div class="star position-absolute"><span class="badge badge-success"><i class="feather-star"></i> ${item.total_rating} (${item.shop_rate_number})</span></div>
                        <a href="/store/shop/${item.name}/">
                            <img alt="#" src="/media/${item.image_path}" class="img-fluid item-img w-100 card-img">
                        </a>
                    </div>
                    <div class="p-3 position-relative">
                        <div class="list-card-body">
                            <h6 class="mb-1 font-weight-bold"><a href="/store/shop/${item.name}/" class="text-black">${item.name}</a></h6>
                            <p class="small category-underline text-gray">• ${item.address}</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
    } else if (type === 'product') {
        cardHtml = `
            <div class="col-md-3 pb-3">
                <div class="list-card bg-white h-100 rounded overflow-hidden position-relative shadow-sm">
                    <div class="list-card-image">
                        <div class="star position-absolute"><span class="badge badge-success"><i class="feather-star"></i> ${item.average_rate} (${item.product_rate_number})</span></div>
                        <a href="/products/product_view/${item.id}/">
                            <img alt="#" src="/media/${item.image_path}" class="img-fluid item-img w-100 card-img">
                        </a>
                    </div>
                    <div class="p-3 position-relative">
                        <div class="list-card-body">
                            <h6 class="mb-1"><a href="/products/product_view/${item.id}/" class="font-weight-bold">${item.name}</a></h6>
                            <p class="mb-1 font-weight-bold price-color">$${item.price}</p>
                            <p class="mb-1 small category-underline">Category: ${item.category}</p> 
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    return cardHtml;
}

// display recommend dish
function displayRecommend(){
    $.ajax({
        url: '/recommend/recommend_view/',
        type: 'POST',
         headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(data) {
             // empty row
            $("#category_box .row").empty();
            // add product card
            data.products.forEach(product => {
                $("#category_box .row").append(createCard(product, 'product'));
            });
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
    console.log("displayRecommend done");
}

// display most popular store
function displayPopular(){
    $.ajax({
        url: '/recommend/popular_view/',
        type: 'POST',
         headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(data) {
            $("#category_box .row").empty();
            if (data.shops && Array.isArray(data.shops)) { // 确保 data.shops 存在且为数组
                data.shops.forEach(shop => {
                    $("#category_box .row").append(createCard(shop, 'shop'));
                });
            } else {
                console.error("Expected 'shops' to be an array, received:", data.shops);
            }
        },
        // success: function(data) {
        //     // empty row
        //     $("#category_box .row").empty();
        //     console.log(data);
        //     data.shops.forEach(shop => {
        //         $("#category_box .row").append(createCard(shop, 'shop'));
        //     });
        // },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
    console.log("displayPopular done");
}

// display most sales store
function displaySales(){
    $.ajax({
        url: '/recommend/sales_view/',
        type: 'POST',
         headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(data) {
            // empty row
            $("#category_box .row").empty();

            data.shops.forEach(shop => {
                $("#category_box .row").append(createCard(shop, 'shop'));
            });
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
    console.log("displaySales done");
}



$(document).ready(function() {
    // get value of type
    let value = $("#category_type").text();
    console.log("display: ",value);
    if (value === 'recommend') {
        displayRecommend();
    } else if (value === 'popular') {
        displayPopular();
    } else if (value === 'sales') {
        displaySales();
    }else{
        console.log("Error: not found type");
        window.alert("Error: not found type");
    }
});