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
                        <div class="star position-absolute"><span class="badge badge-success"><i class="feather-star"></i> ${item.shop__total_rating} (${item.shop_rate_number})</span></div>
                        <a href="/store/shop/${item.shop__name}/">
                            <img alt="#" src="/media/${item.shop__image_path}" class="img-fluid item-img w-100 card-img">
                        </a>
                    </div>
                    <div class="p-3 position-relative">
                        <div class="list-card-body">
                            <h6 class="mb-1 font-weight-bold"><a href="/store/shop/${item.shop__name}/" class="text-black">${item.shop__name}</a></h6>
                            <p class="small text-gray category-underline">• ${item.shop__address}</p>
                        </div>
                        <a href="/customers/cancel_shop_fav/${item.shop__name}/" class="btn cancel-btn">Cancel</a>
                    </div>
                </div>
            </div>
        `;
    } else if (type === 'product') {
        cardHtml = `
            <div class="col-md-3 pb-3">
                <div class="list-card bg-white h-100 rounded overflow-hidden position-relative shadow-sm">
                    <div class="list-card-image">
                        <div class="star position-absolute"><span class="badge badge-success"><i class="feather-star"></i> ${item.product__average_rate} (${item.product_rate_number})</span></div>
                        <a href="/products/product_view/${item.product__id}/">
                            <img alt="#" src="/media/${item.product__image_path}" class="img-fluid item-img w-100 card-img">
                        </a>
                    </div>
                    <div class="p-3 position-relative">
                        <div class="list-card-body">
                            <h6 class="mb-1 font-weight-bold"><a href="/products/product_view/${item.product__id}/" class="text-black">${item.product__name}</a></h6>
                            <p class="mb-1 font-weight-bold price-color">Price: $${item.product__price}</p>
                            <p class="mb-1 small category-underline">Category: ${item.product__category}</p> 
                        </div>
                        <a href="/customers/cancel_product_fav/${item.product__id}/" class="btn cancel-btn">Cancel</a>
                    </div>
                </div>
            </div>
        `;
    }
    return cardHtml;
}


// function to display all favorite data
function displayData() {
    $.ajax({
        url: '/recommend/get_favorite/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // update number
            $('#home-tab').html(`<i class="feather-home mr-2"></i>Restaurants (${data.shops.length})`);
            $('#profile-tab').html(`<i class="feather-disc mr-2"></i>Dishes (${data.products.length})`);
            // clear row
            $('#home .container .row').empty();
            $('#profile .container .row').empty();

            // add card
            data.shops.forEach(shop => {
                $('#home .container .row').append(createCard(shop, 'shop'));
            });

            data.products.forEach(product => {
                $('#profile .container .row').append(createCard(product, 'product'));
            });
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
}

$(document).ready(function() {
    displayData();
});