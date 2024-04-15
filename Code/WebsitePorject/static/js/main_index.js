"use strict"

function displayData(){
    displayRecommend();
    displayPopular();
    displaySales();
}

// display all recommend dish card
function displayRecommend(){
    $.ajax({
        url: '/recommend/get_recommend_dish/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            let sliderSection = $('.trending-slider');
            sliderSection.empty(); // empty all the card

            data.products.forEach(function(item) {
                let cardHtml = `
                    <div class="col-md-3 pb-3">
                        <div class="list-card bg-white h-100 rounded overflow-hidden position-relative shadow-sm">
                            <div class="list-card-image">
                                <div class="star position-absolute"><span class="badge badge-success"><i class="feather-star"></i> ${item.average_rate} (${item.product_rate_number})</span></div>
                                <a href="/products/product_view/${item.id}/">
                                    <img alt="#" src="/media/${item.image_path}" class="img-fluid item-img w-100 max-img-size">
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
                sliderSection.append(cardHtml);
            });

            // refresh slider js
            $('.trending-slider').slick('refresh');
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
}

// display most popular
function displayPopular(){
    console.log("displayPopular function....")
    $.ajax({
        url: '/recommend/get_popular/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            let popularSection = $('.most_popular');
            popularSection.empty();
            // 2 row
            let row1 = $('<div class="row"></div>');
            let row2 = $('<div class="row"></div>');

            // Corrected data.shops to iterate over the shops array
            data.shops.forEach(function(shop, index) {
                // create shop card
                let shopCard = `
                <div class="col-md-3 pb-3">
                    <div class="list-card bg-white h-100 rounded overflow-hidden position-relative shadow-sm">
                        <div class="list-card-image">
                            <div class="star position-absolute"><span class="badge badge-success"><i class="feather-star"></i> ${shop.total_rating} (${shop.popularity_value}+)</span></div>
                            <a href="/store/shop/${shop.name}/">
                                <img alt="${shop.name}" src="/media/${shop.image_path}" class="img-fluid item-img w-100 max-img-size">
                            </a>
                        </div>
                        <div class="p-3 position-relative">
                            <div class="list-card-body">
                                <h6 class="mb-1"><a href="/store/shop/${shop.name}/" class="text-black">${shop.name}</a></h6>
                                <p class="text-gray mb-1 small category-underline">• ${shop.address}</p>
                                <ul class="rating-stars list-unstyled">
                                    ${generateStars(shop.total_rating)}
                                </ul>
                            </div>
                            <div class="list-card-badge">
                                <span class="badge badge-danger">OFFER</span>
                            </div>
                        </div>
                    </div>
                </div>
                `;
                if(index < 4) {
                    row1.append(shopCard);
                } else {
                    row2.append(shopCard);
                }
            });

            popularSection.append(row1);
            popularSection.append(row2);
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
}

// display most sales section
function displaySales() {
    console.log("displaySales function....")
    $.ajax({
        url: '/recommend/get_sales/',
        type: 'GET',
        dataType: 'json',
        success: function(shops) {
            const salesSection = $('.most_sale .row.mb-3');
            salesSection.empty();

            shops.forEach(function(shop, index) {
                if (index < 3) {
                    const starHtml = generateStars(shop.total_rating);
                    const shopCardHtml = `
                        <div class="col-md-4 mb-3">
                            <div class="d-flex align-items-center list-card bg-white h-100 rounded overflow-hidden position-relative shadow-sm">
                                <div class="list-card-image">
                                    <div class="star position-absolute"><span class="badge badge-success"><i class="feather-star"></i> ${shop.total_rating} (${shop.popularity_value}+)</span></div>
                                    <a href="/store/shop/${shop.name}/">
                                        <img alt="${shop.name}" src="/media/${shop.image_path}" class="img-fluid item-img w-100 max-img-size">
                                    </a>
                                </div>
                                <div class="p-3 position-relative">
                                    <div class="list-card-body">
                                        <h6 class="mb-1"><a href="/store/shop/${shop.name}/" class="text-black">${shop.name}</a></h6>
                                        <p class="text-gray mb-3 small category-underline">• ${shop.address}</p>
                                    </div>
                                    <div class="list-card-badge">
                                        <span class="badge badge-danger">OFFER</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;

                    salesSection.append(shopCardHtml);
                }
            });
        },
        error: function(xhr, status, error) {
            console.error("Error fetching sales data:", error);
        }
    });
}

// generate star ratings
function generateStars(rating){
    let starsHtml = '';
    for(let i = 0; i < 5; i++){
        starsHtml += `<i class="feather-star ${i < Math.round(rating) ? 'star_active' : ''}"></i>`;
    }
    return `<li>${starsHtml}</li>`;
}


$(document).ready(function() {
    displayData();
});