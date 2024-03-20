"use strict"

// 从后端获取商店信息并将其展示在html页面中
function displayData(){
    displayRecommend();
    displayPopular();
    displaySales();
}

function displayRecommend(){
    // TODO:从后端django接收推荐的商店的信息
    // TODO: URL='/recommend/get_recommend/'
    // TODO:后端从共传来6个商店数据，将其对应的生成6个商店card，并放在slider中可以左右切换
    // TODO:对于html中的商店图片用图片路径显示并使用media: "/media/${image_path}"
    console.log("displayRecommend function....")
    $.ajax({
        url: '/recommend/get_recommend/', // 从 Django 视图 `get_recommend` 获取数据
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            let sliderSection = $('.trending-slider');
            sliderSection.empty(); // 清空现有内容

            data.forEach(function(shop) {
                // 创建商店卡片
                let shopCard = `
                <div class="osahan-slider-item">
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
                                <p class="text-gray mb-3">${shop.address}</p>
                            </div>
                            <div class="list-card-badge">
                                <span class="badge badge-danger">OFFER</span>
                            </div>
                        </div>
                    </div>
                </div>
                `;
                // 将商店卡片 HTML 添加到滑动轮播中
                sliderSection.append(shopCard);
            });
            // 初始化或刷新滑动轮播插件（如果你使用了如 Slick Slider 等插件）
            // 注意：根据你实际使用的滑动轮播插件，这里的代码可能需要相应调整
            $('.trending-slider').slick('refresh');
        },
        error: function(xhr, status, error) {
            console.error("An error occurred: " + status + " " + error);
        }
    });
}


function displayPopular(){
    console.log("displayPopular function....")
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

function displaySales() {
    console.log("displaySales function....")
    $.ajax({
        url: '/recommend/get_sales/',
        type: 'GET',
        dataType: 'json',
        success: function(shops) {
            // 清除现有内容
            const salesSection = $('.most_sale .row.mb-3');
            salesSection.empty();

            // 仅处理前3个商店
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
                                        <h6 class="mb-1"><a href="/shop/${shop.name}/" class="text-black">${shop.name}</a></h6>
                                        <p class="text-gray mb-3">${shop.address}</p>
                                    </div>
                                    <div class="list-card-badge">
                                        <span class="badge badge-danger">OFFER</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                    // 将商店卡片 HTML 添加到页面中
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