const cartItemContainer = $('.cart-items');

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


// 从django数据库中获取cartItem的所有数据并返回显示
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
    console.log("updateCart() :> shop name: ",shopName);
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

function showAddress() {
    $.ajax({
        url: '/customers/get_address/',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            // 检查响应中是否有地址数据
            if (response.addresses && response.addresses.length > 0) {
                let addresses = response.addresses;
                let container = $('.mb-3.font-weight-bold').next(); // 获取标题下方的容器
                let row; // 用于动态创建新的行
                addresses.forEach(function(address, index) {
                    // 每4个地址添加到一个新行
                    if (index % 4 === 0) {
                        row = $('<div class="row"></div>'); // 创建新的行
                        container.append(row); // 将新行添加到容器中
                    }
                    // 创建地址卡片的HTML结构
                    let addressCard = $('<div class="col-lg-3 custom-control custom-radio mb-3 position-relative border-custom-radio address-card-container""></div>');
                    let input = $('<input type="radio" class="custom-control-input" name="addressOption">').attr('id', 'customRadioInline' + address.id);
                    let label = $('<label class="custom-control-label w-100"></label>').attr('for', 'customRadioInline' + address.id);
                    let cardBody = $(
                        '<div>' +
                        '   <div class="p-3 bg-white rounded shadow-sm w-100">' +
                        '       <div class="d-flex align-items-center mb-2">' +
                        '           <h6 class="mb-0">Address:</h6>' +
                        '       </div>' +
                        '       <p class="small text-muted m-0">' + address.address_line + '</p>' +
                        '   </div>' +
                        '</div>'
                    );
                    // 组装地址卡片并添加到当前行
                    label.append(cardBody);
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


$(document).ready(function(){
    showAddress()
    showCart();
    addNumber();
    minusNumber();
    console.log("Initialization complete.");
});
