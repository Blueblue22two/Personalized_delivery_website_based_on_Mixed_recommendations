// 对于html中的图片用图片路径显示并使用media: "/media/${image_path}"
// 以确保csrf与url无误

const cartItemContainer = $('.cart-items'); // 使用新添加的类名作为选择器

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

// store info
function storeInfo(){
    // get shop name
    let shopNameElement = document.querySelector('.shop-name');
    let shopName = shopNameElement.textContent;

    $.ajax({
        url: '/store/shop_info/',
        type: 'POST',
        data: {'shopName': shopName,},
        headers: {'X-CSRFToken': getCsrfTokenFromForm()},
        success: function(response) {
            // 更新星级评分图标
            let ratingElement = document.getElementById('shopRating');
            let totalRating = ratingElement.getAttribute('data-total-rating');
            $('.rating-stars').html(generateStars(parseFloat(totalRating)));
            // 更新评分人数的数值
            $('.label-rating').text(` (${response.ratingsCount} rated)`);
        },
        error: function(xhr, status, error) {
            console.log("Error: " + error);
        }
    });
}


// get category and product info
function productInfo(){
    // get shop name
    let shopNameElement = document.querySelector('.shop-name');
    let shopName = shopNameElement.textContent;
    $.ajax({
        type: "POST",
        url: '/store/product_info/',
        data: {'shopName': shopName,},
        headers: {'X-CSRFToken': getCsrfTokenFromForm()},
        success: function(products){
            let categoryMap = {}; // store the category of this shop
            products.forEach(function(product) {
                // 如果该类别不存在，创建一个空数组
                if (!categoryMap[product.category]) {
                    categoryMap[product.category] = [];
                }
                // 将商品添加到对应的类别中
                categoryMap[product.category].push(product);
            });

            // 遍历分类并生成 HTML 元素
            for (const category in categoryMap) {
                // category header
                let categoryHtml = `<h6 class="p-3 m-0 category-title">${category}</h6>`;
                $('.menu-container').append(categoryHtml);

                // create product
                categoryMap[category].forEach(function(product) {
                    let productHtml = `
                        <div class="p-3 border-bottom gold-members">
                            <!--  add to cart button-->
                            <span class="float-right"><a href="#" class="btn btn-outline-secondary btn-sm">ADD</a></span>
                            <div class="media">
                                <img src="/media/${product.image_path}" class="mr-3 rounded-pill product-img">
                                <div class="media-body">
                                    <!--product id-->
                                    <p class="text-muted mb-0">ID: ${product.id}</p>
                                    <!--  product name-->
                                    <h6 class="mb-1">${product.name}</h6>
                                    <p class="text-muted mb-0">${product.price} $</p>
                                </div>
                            </div>
                        </div>`;
                    $('.menu-container').append(productHtml);
                });
            }
        },
        error: function(error){
            console.log(error);
        }
    });
}

function addToCart() {
    $('.menu-container').on('click', '.btn-outline-secondary', function(event) {
        event.preventDefault(); // Prevent default anchor action
        const productCard = $(this).closest('.gold-members');
        const productId = productCard.find('p.text-muted.mb-0').text().split(': ')[1];

        // 检查该商品是否已存在于购物车中
        let existingCartItem = $(`.osahan-cart-item .gold-members[data-product-id="${productId}"]`);
        if (existingCartItem.length) {
            // 商品已存在，仅增加数量
            let quantityInput = existingCartItem.find('.count-number-input');
            let quantity = parseInt(quantityInput.val(), 10);
            quantityInput.val(quantity + 1);
        } else {
            // 商品不存在，添加新商品到购物车
            const productName = productCard.find('h6').text();
            const productPrice = productCard.find('p.text-muted.mb-0').last().text().split(' $')[0];

            const cartItemHtml = `
                <div class="gold-members d-flex align-items-center justify-content-between px-3 py-2 border-bottom" data-product-id="${productId}">
                    <div class="media align-items-center">
                        <div class="mr-2 text-danger">&middot;</div>
                        <div class="media-body">
                            <p class="m-0">${productName}</p>
                        </div>
                    </div>
                    <div class="d-flex align-items-center">
                        <span class="count-number float-right">
                            <button type="button" class="btn-sm left dec btn btn-outline-secondary">
                                <i class="feather-minus"></i>
                            </button>
                            <input class="count-number-input" type="text" readonly="" value="1">
                            <button type="button" class="btn-sm right inc btn btn-outline-secondary">
                                <i class="feather-plus"></i>
                            </button>
                        </span>
                        <p class="text-gray mb-0 float-right ml-2 text-muted small">${productPrice} $</p>
                    </div>
                </div>`;
            cartItemContainer.append(cartItemHtml);
            // $('.osahan-cart-item .bg-white.border-bottom').append(cartItemHtml);
        }
        getTotalPrice();
    });
}

function addNumber() {
    $('.osahan-cart-item').on('click', '.inc', function() {
        const input = $(this).siblings('.count-number-input');
        let value = parseInt(input.val(), 10);
        input.val(++value);
        getTotalPrice();
    });
}

function minusNumber() {
    $('.osahan-cart-item').on('click', '.dec', function() {
        const input = $(this).siblings('.count-number-input');
        let value = parseInt(input.val(), 10);
        if (value > 1) {
            input.val(--value);
        } else {
            $(this).closest('.gold-members').remove(); // Remove item if quantity is 1 and minus is clicked
        }
        getTotalPrice();
    });
}


function getTotalPrice() {
    let itemTotal = 0; // 商品总金额
    $('.osahan-cart-item .gold-members').each(function() {
        const price = parseFloat($(this).find('.text-gray').text().split(' $')[0]);
        const quantity = parseInt($(this).find('.count-number-input').val(), 10);
        itemTotal += price * quantity; // 累加每个商品的价格乘以其数量
    });

    // 假设配送费为固定值，根据您的应用逻辑调整
    const deliveryFee = 0;
    const toPay = itemTotal + deliveryFee; // 总金额加上配送费
    $('.osahan-cart-item .font-weight-bold').find('span').text(`$${toPay.toFixed(2)}`); // 更新 "TO PAY" 部分
    // 更新商品总金额
    $('.osahan-cart-item').find('.mb-1').first().find('span.text-dark').text(`$${itemTotal.toFixed(2)}`);
    // 更新配送费
    $('.osahan-cart-item').find('p.mb-1').last().find('span.text-dark').text(`$${deliveryFee.toFixed(2)}`);
}


function showCart(){
    // TODO:从django数据库中获取cartItem数据中是否有属于该商店的，若有，则在该cart都显示出来
}

function updateCart(){
    // TODO:更新购物车信息，每当用户在html中修改cart中的商品数据（增删改）时，调用该方法，将html中的cart的改变在数据库CartItem中存储
    // TODO:存储时还需注意避免遇见重复的情况
}

function checkLogin2(){
    // TODO:后续操作，检查进行操作时是否为customer，如果是merchant或者未登录则提示需登录才能使用该功能
}

function addFavorite(){
    // TODO:用户添加商店到收藏夹中的功能
}

$(document).ready(function(){
    storeInfo();
    productInfo();
    addToCart();
    addNumber();
    minusNumber();
    console.log("Initialization complete.");
});
