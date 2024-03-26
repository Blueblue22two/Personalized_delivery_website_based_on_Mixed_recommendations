const cartItemContainer = $('.cart-items');

// get shop name element
const shopNameElement = document.querySelector('.shop-name');

// const shopNameElement = document.querySelector("h2.shop-name.font-weight-bold");

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
                              
                                <a href="/products/product_view/${product.id}/">
                                    <img src="/media/${product.image_path}" class="mr-3 rounded-pill product-img">
                                </a>
                                <div class="media-body">
                                    <!--product id-->
                                    <p class="text-muted mb-0 product-id">ID: ${product.id}</p>
                                    <!--  product name-->
                                    <h6 class="mb-1">${product.name}</h6>
                                    <!--product price-->
                                    <p class="text-muted mb-0 product-price">${product.price} $</p>
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

// 将商品添加到购物车并将创建html使其显示到cart item section中
function addToCart() {
    $('.menu-container').on('click', '.btn-outline-secondary', function(event) {
        event.preventDefault(); // Prevent default anchor action
        const productCard = $(this).closest('.gold-members');
        const productId = productCard.find('.product-id').text().split(': ')[1];
        console.log("product id: ",productId)

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
            // 创建cartItem card添加到html中
            const cartItemHtml = `
                <div class="gold-members d-flex align-items-center justify-content-between px-3 py-2 border-bottom" data-product-id="${productId}">
                    <div class="media align-items-center">
                        <div class="mr-2 text-danger">&middot;</div>
                        <div class="media-body">
                            <p class="m-0" id="pid">ID: ${productId}</p>
                            <p class="m-0">${productName}</p>
                        </div>
                    </div>
                    <div class="d-flex align-items-center">
                        <span class="count-number float-right">
                            <button type="button" class="btn-sm left dec btn btn-outline-secondary">
                                <i class="feather-minus"></i>
                            </button>
                            <!-- Quantity of product-->
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
        updateCart();
    });
}


function addNumber() {
    $('.osahan-cart-item').on('click', '.inc', function() {
        const input = $(this).siblings('.count-number-input');
        let value = parseInt(input.val(), 10);
        input.val(++value);
        getTotalPrice();
        updateCart();
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
        updateCart();
    });
}


function getTotalPrice() {
    let itemTotal = 0;
    $('.osahan-cart-item .gold-members').each(function() {
        const price = parseFloat($(this).find('.text-gray').text().split(' $')[0]);
        const quantity = parseInt($(this).find('.count-number-input').val(), 10);
        itemTotal += price * quantity;
    });

    // set the deliveryFee
    const deliveryFee = 0;
    const toPay = itemTotal + deliveryFee;
    $('.osahan-cart-item .font-weight-bold').find('span').text(`$${toPay.toFixed(2)}`);
    // update total
    $('.osahan-cart-item').find('.mb-1').first().find('span.text-dark').text(`$${itemTotal.toFixed(2)}`);
    // update delivery fee
    $('.osahan-cart-item').find('p.mb-1').last().find('span.text-dark').text(`$${deliveryFee.toFixed(2)}`);
}


// 从django数据库中获取cartItem数据中是否有属于该商店的,若有则显示
function showCart(){
    console.log("show Cart function working... ")
    // get shop name
    let shopName = shopNameElement.textContent;
    let formData = new FormData();
    formData.append('shopName', shopName);

    console.log("showCart() :> shop name: ",shopName)
    $.ajax({
        type: "POST",
        url: '/carts/get_cart_store/',
        data: formData,
        headers: {'X-CSRFToken': getCsrfTokenFromForm()},
        processData: false,
        contentType: false,

        success: function(response) {
            // Assuming `cartItemContainer` is the container where cart items should be displayed.
            const products = response.products;
            products.forEach(product => {
                const productHtml = `
                    <div class="gold-members d-flex align-items-center justify-content-between px-3 py-2 border-bottom" data-product-id="${product.id}">
                        <div class="media align-items-center">
                            <div class="mr-2 text-danger">&middot;</div>
                            <div class="media-body">
                                <p class="m-0" id="pid">ID: ${product.id}</p>
                                <p class="m-0">${product.name}</p>
                            </div>
                        </div>
                        <div class="d-flex align-items-center">
                            <span class="count-number float-right">
                                <button type="button" class="btn-sm left dec btn btn-outline-secondary">
                                    <i class="feather-minus"></i>
                                </button>
                                <!--quantity-->
                                <input class="count-number-input" type="text" readonly="" value="${product.quantity}">
                                <button type="button" class="btn-sm right inc btn btn-outline-secondary">
                                    <i class="feather-plus"></i>
                                </button>
                            </span>
                            <p class="text-gray mb-0 float-right ml-2 text-muted small">${product.price} $</p>
                        </div>
                    </div>`;
                // Append productHtml to the cart items container
                cartItemContainer.append(productHtml);
            });
            getTotalPrice(); // Assuming this function recalculates the total price of items in the cart.
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}

// update the cart item
function updateCart() {
    let shopName = shopNameElement.textContent; // get shop name
    let products = []; // all the cart item info in cart
    // Iterate over each cart item
    $('.cart-items .gold-members').each(function() {
        const productId = $(this).data('product-id'); // get product id
        const quantity = parseInt($(this).find('.count-number-input').val(), 10); // get product quantity
        products.push({ id: productId, quantity: quantity });
    });
    console.log("updateCart() :>  products[]: ");
    console.log(products);
    console.log("updateCart() :> shop name: ",shopName);
    $.ajax({
        type: "POST",
        url: '/carts/upload_cart/',
        data: JSON.stringify({
            products: products,
            shopName: shopName
        }),
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm(),
            'Content-Type': 'application/json'
        },
        success: function(data) {
            console.log('Cart updated successfully');
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}


function checkLogin2(){
    console.log('start checking...');
    fetch('/accounts/get_info')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                if (data.user_type === '1') {
                    showCart();
                    addToCart();
                    addNumber();
                    minusNumber();
                } else {
                    console.log("Not customer user type");
                    disableButton();
                    // Disable the favorite function
                    let favButton = document.getElementById("fav_button");
                    if (favButton) {
                        favButton.disabled = true;
                        favButton.classList.add("disabled");
                    }
                }
            } else {
                disableButton();
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
            disableButton();
            console.error('Error:', error);
            // Disable the favorite function
            let favButton = document.getElementById("fav_button");
            if (favButton) {
                favButton.disabled = true;
                favButton.classList.add("disabled");
            }
        });
}

// disable some function which can only access by customer
function disableButton() {
    // Disable the cart link
    let cartLink = document.querySelector("a[href='/carts/main/']");
    if (cartLink) {
        cartLink.href = "#";
        cartLink.addEventListener("click", function(event) {
            window.alert("Only customer user can use cart function, please log in as a customer");
            console.error("Only customer user can use cart function, please log in as a customer");
            event.preventDefault();
        });
    }

    // Disable every add button in product card
    let addButtons = document.querySelectorAll(".product-card .btn-outline-secondary");
    addButtons.forEach(function(button) {
        button.disabled = true;
        button.classList.add("disabled");
        button.addEventListener("click", function(event) {
            window.alert("Only customer user can use cart function, please log in as customer");
            console.error("Only customer user can use cart function, please log in as customer");
            event.preventDefault();
        });
    });
    console.log("Disable function done")
}


function addFavorite() {
    // get shop name
    let shopName = shopNameElement.textContent;
    let csrfToken = getCsrfTokenFromForm();
    let formData = new FormData();
    formData.append('shopName', shopName);
    $.ajax({
        type: 'POST',
        url: '/customers/add_fav/',
        headers: {
            'X-CSRFToken': csrfToken
        },
        processData: false,
        contentType: false,
        data: formData,
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

$(document).ready(function(){
    checkLogin2();
    disableButton();
    storeInfo();
    productInfo();
    console.log("Initialization complete.");
});
