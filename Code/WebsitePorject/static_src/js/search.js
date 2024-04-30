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


// function to display result of search page
function displayData() {
    $.ajax({
        url: '/recommend/get_search/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            $('#home-tab').html(`<i class="feather-home mr-2"></i>Restaurants (${data.shops.length})`);
            $('#profile-tab').html(`<i class="feather-disc mr-2"></i>Dishes (${data.products.length})`);
            // clear row
            $('#home .container .row').empty();
            $('#profile .container .row').empty();


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


// function to get search result and display it
function displayResult() {
    let inputText = $('#inlineFormInputGroup').val().trim();
    // verify
    if (inputText.length > 50) {
        alert('The entered text is too long. Please enter less than 50 characters.');
        return;
    } else if (inputText.length === 0) {
        alert('Please enter some text to search.');
        return;
    }

    $.ajax({
        url: '/recommend/get_search/',
        type: 'POST',
        data: {s: inputText},
        dataType: 'json',
        headers: {"X-CSRFToken": getCsrfTokenFromForm()},
        success: function(data) {
            $('#home-tab').html(`<i class="feather-home mr-2"></i>Restaurants (${data.shops.length})`);
            $('#profile-tab').html(`<i class="feather-disc mr-2"></i>Dishes (${data.products.length})`);
            // 清除旧内容
            $('#home .container .row').empty();
            $('#profile .container .row').empty();
            // 处理搜索结果为空的情况
            if (data.shops.length === 0) {
                $('#home .container').html('<div class="text-center py-5">Nothing found for Restaurants</div>');
            } else {
                data.shops.forEach(shop => {
                    $('#home .container .row').append(createCard(shop, 'shop'));
                });
            }
            if (data.products.length === 0) {
                $('#profile .container').html('<div class="text-center py-5">Nothing found for Dishes</div>');
            } else {
                data.products.forEach(product => {
                    $('#profile .container .row').append(createCard(product, 'product'));
                });
            }
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
}


$(document).ready(function() {
    displayData();

    // event for click search button
    $('.input-group-prepend button').on('click', function() {
        displayResult();
    });
});