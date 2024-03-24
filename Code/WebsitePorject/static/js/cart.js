const cartItemContainer = $('.cart-items');
// 全局变量来存储选中的地址信息
var selectedAddress = {};

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

// add cart item number
function addNumber() {
    $('.osahan-cart-item').on('click', '.inc', function() {
        const input = $(this).siblings('.count-number-input');
        let value = parseInt(input.val(), 10);
        input.val(++value);
        getTotalPrice();
        updateCart();
    });
}

// minus cart item number
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
    $('.osahan-cart-item .font-weight-bold').find('span').text(`$${toPay.toFixed(2)}`); // 更新 "TO PAY" 部分
    // 更新商品总金额
    $('.osahan-cart-item').find('.mb-1').first().find('span.text-dark').text(`$${itemTotal.toFixed(2)}`);
    // 更新配送费
    $('.osahan-cart-item').find('p.mb-1').last().find('span.text-dark').text(`$${deliveryFee.toFixed(2)}`);
}


// 从数据库中获取cartItem的所有数据并在html中显示
function showCart(){
    console.log("show Cart function working... ")
   $.ajax({
        type: "GET",
        url: '/carts/get_cart/',
        headers: {'X-CSRFToken': getCsrfTokenFromForm()},
        processData: true,
        contentType: 'application/json', // GET请求可以设置为application/json

        success: function(response) {
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
    let products = []; // all the cart item info in cart
    // 遍历获取每个cart item
    $('.cart-items .gold-members').each(function() {
        const productId = $(this).data('product-id'); // get product id
        const quantity = parseInt($(this).find('.count-number-input').val(), 10); // get product quantity
        products.push({ id: productId, quantity: quantity });
    });
    console.log("updateCart() :>  products[]: ");
    console.log(products);
    $.ajax({
        type: "POST",
        url: '/carts/upload/',
        data: JSON.stringify({
            products: products,
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

// 从后端获取所有相关的address数据，并使用该数据在html中的address section中生成所有address card
function showAddress() {
   $.ajax({
        url: '/customers/get_address/',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            if (response.addresses && response.addresses.length > 0) {
                let addresses = response.addresses;

                let deliveryAddressSection = $(".osahan-cart-item-profile");
                let addButton = deliveryAddressSection.find('a.btn-primary');
                deliveryAddressSection.find('.address-cards-container').remove();

                let addressCardsContainer = $('<div class="address-cards-container"></div>');
                addButton.before(addressCardsContainer);

                let row = $('<div class="row"></div>'); // 初始化row
                addressCardsContainer.append(row); // 将row添加到容器中

                addresses.forEach(function(address, index) {
                    if (index % 4 === 0 && index !== 0) { // 当index为4的倍数且不为0时，重新创建一个row
                        row = $('<div class="row"></div>');
                        addressCardsContainer.append(row);
                    }

                    // let addressCard = $('<div class="col-lg-3 custom-radio mb-3"></div>');
                    // let input = $('<input type="radio" id="addressRadio' + index + '" name="addressRadio" class="custom-control-input">');
                    // let label = $('<label class="custom-control-label" for="addressRadio' + index + '">...</label>'); // 省略了具体的标签结构以保持简洁

                    // 创建地址卡片HTML结构
                    let addressCard = $('<div class="custom-control col-lg-3 custom-radio mb-3 position-relative border-custom-radio"></div>');
                    let input = $('<input type="radio" id="customRadioInline' + index + '" name="customRadioInline1" class="custom-control-input">');
                    let label = $('<label class="custom-control-label w-100" for="customRadioInline' + index + '"></label>');
                    let cardBody = $('<div><div class="p-3 bg-white rounded shadow-sm w-100"></div></div>');
                    let addressInfo = $(
                        '<div class="d-flex align-items-center mb-2">' +
                        '<h6 class="mb-0">Address:</h6>' +
                        '<p class="mb-0 badge badge-light ml-auto"><i class="icofont-check-circled"></i> id: ' + address.id + '</p>' +
                        '</div>' +
                        '<p class="small text-muted m-0">' + address.province + '</p>' +
                        '<p class="small text-muted m-0">' + address.city + '</p>' +
                        '<p class="small text-muted m-0">' + address.district + '</p>' +
                        '<p class="small text-muted m-0">' + address.detail + '</p>'
                    );
                    cardBody.find('.p-3').append(addressInfo);
                    // Assemble the address card and add it to the current row
                    label.append(cardBody);
                    // addressCard.append(input).append(label);

                    // 添加事件监听器更新全局变量
                    input.change(function() {
                        if (this.checked) {
                            selectedAddress = {
                                id: address.id,
                                province: address.province,
                                city: address.city,
                                district: address.district,
                                detail: address.detail
                            };
                        }
                    });
                    addressCard.append(input).append(label);
                    row.append(addressCard);
                });
            }
        },
        error: function(xhr, status, error) {
            console.error("Failed to fetch addresses:", status, error);
        }
    });
}

// 使用此函数可以在任何地方获取当前选中的地址信息
function getSelectedAddress() {
    return selectedAddress;
}


// event of pay button
$(document).ready(function() {
    $('#pay_btn').click(function(e) {
        e.preventDefault();
        payment();
    });
});

function payment() {
    // get address id
    let addressID=getSelectedAddress().id;
    console.log("select addressID: ",addressID);
    // Check if addressID is undefined or empty, then alert
    if (addressID === undefined || addressID === "") {
        window.alert("Please select an address");
        return
    }
    // get total price
    let totalPriceText = $('#totalPrice').text().trim();
    let totalPrice = parseFloat(totalPriceText.replace('$', '')); // 确保获取的是数字
    console.log("total pay: ",totalPrice)
    if (totalPrice === 0){
        window.alert("There is no item in the cart, please select the item you want to buy!")
        return
    }
    let formData = new FormData();
    formData.append('total_price', totalPrice);
    formData.append('address_id', addressID);

    // store all the product id and quantity
    let products = [];
    // get id and quantity
    $('.gold-members').each(function() {
        let productId = $(this).data('product-id');
        let quantity = $(this).find('.count-number-input').val();
        console.log("product id:",productId);
        console.log("quantity:",quantity);
        products.push({
            product_id: productId,
            quantity: quantity
        });
    });
    let productsJson = JSON.stringify(products);
    formData.append('products', productsJson);

    $.ajax({
        url: '/payment/generate_payment/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            console.log(response.message);
            window.alert(response.message);
        },
        error: function(xhr, status, error) {
            console.error("Error sending order data:", error);
            window.alert("Error sending order.");
        }
    });
}


$(document).ready(function(){
    showAddress()
    showCart();
    addNumber();
    minusNumber();
    console.log("Initialization complete.");
});
