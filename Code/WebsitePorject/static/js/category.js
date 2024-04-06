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
function createCard(item) {
    let cardHtml = '';
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
    return cardHtml;
}


function displayData() {
    let categoryElement = document.getElementById("category_name");
    let categoryName = categoryElement.textContent.replace("Category: ", "").trim();
    console.log("category name:",categoryName);
    $.ajax({
        url: '/products/category_info/',
        type: 'POST',
        dataType: 'json',
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        contentType: 'application/json',
        data: JSON.stringify({
            'category_name': categoryName
        }),
        success: function(data) {
            let productsRow = $('#category_box .row');
            productsRow.empty(); // 清空现有的产品卡片

            data.products.forEach((product, index) => {
                // 每4个产品卡片开始一个新的行
                if (index % 4 === 0 && index !== 0) {
                    $('#category_box').append('<div class="row"></div>'); // 添加新的行
                    productsRow = $('#category_box .row').last(); // 更新当前行为新添加的行
                }
                productsRow.append(createCard(product)); // 向当前行添加产品卡片
            });
        },
    });
}


$(document).ready(function() {
    displayData();
});