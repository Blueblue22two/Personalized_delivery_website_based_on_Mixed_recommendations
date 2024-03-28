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


document.addEventListener('DOMContentLoaded', function() {
    // add a event for result
    document.querySelector('.input-group-prepend button').addEventListener('click', function() {
        displayResult();
    });
});


function displayResult(){
    // get input value
    let inputText = document.getElementById('inlineFormInputGroup').value;
    if (inputText.length > 50) {
        window.alert('The entered text is too long. Please enter less than 50 characters.');
        return;
    }

    // TODO:使用Post方法将字符串发送到后端,url='/recommend/get_search/'
}


function displayData(){
    // TODO:使用get形式，向后端获取所有store的信息
    // url='/recommend/get_search/'
    // TODO:若获取成功则按照html中的example来显示
    $.ajax({
        url: '/recommend/get_popular/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            let popularSection = $('.most_popular');
            popularSection.empty(); // 清空现有内容
            // 2 row
            let row1 = $('<div class="row"></div>');
            let row2 = $('<div class="row"></div>');

            data.forEach(function(shop, index) {
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
                                <h6 class="mb-1"><a href="/shop/${shop.name}/" class="text-black">${shop.name}</a></h6>
                                <p class="text-gray mb-1 small">• ${shop.address}</p>
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
                // 根据索引，将商店卡片分配到不同的行
                if(index < 4) {
                    row1.append(shopCard);
                } else {
                    row2.append(shopCard);
                }
            });
            // 将行添加到 most_popular 部分
            popularSection.append(row1);
            popularSection.append(row2);
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
}


$(document).ready(function() {
    displayStore();
    displayProduct();
});