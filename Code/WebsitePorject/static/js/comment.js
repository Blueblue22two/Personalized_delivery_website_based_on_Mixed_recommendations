"use strict"

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}


// function displayDataInComment(){
//     // get order id
//     let orderIdText = $('#order-id').text();
//     let orderId = orderIdText.split(': ')[1];
//
//     $.ajax({
//         url: `/orders/get_info/`,
//         type: 'POST',
//         data: { order_id: orderId },
//         headers: {
//             'X-CSRFToken': getCsrfTokenFromForm()
//         },
//         success: function(response) {
//             // TODO:若获取成功，接收数据
//             // TODO:然后按照html中的example生成对应的html元素
//         },
//         error: function(xhr, status, error) {
//             console.error("Error sending order data:", error);
//             window.alert("Error sending order."); // 提示用户错误信息
//         }
//     });
// }

// get all order info from database, and display it in html
function displayDataInComment() {
    // get order id
    let orderIdText = $('#order-id').text();
    let orderId = orderIdText.split(': ')[1];
    $.ajax({
        url: `/orders/get_info/`,
        type: 'POST',
        data: { order_id: orderId },
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            // 清除现有的订单信息
            $('.order-body').empty();
            // 遍历每个订单数据
            response.orders.forEach(order => {
                let orderHtml = `
                <div class="pb-3">
                    <div class="p-3 rounded shadow-sm bg-white">
                        <div class="d-flex border-bottom pb-3 store_card">
                            <div class="text-muted mr-3">
                                <img alt="#" src="/media/${order.shop_image_path}" class="img-fluid order_img rounded shop-logo">
                            </div>
                            <div>
                                <p class="mb-0 font-weight-bold"><a href="/shop/${order.shop_name}/" class="text-dark shop-name">${order.shop_name}</a></p>
                                <p class="mb-0 text-dark font-italic shop-name">${order.shop_address}</p>
                                <p class="order-id">#${orderId}</p>
                            </div>
                            <div class="ml-auto">
                                <p class="bg-success text-white py-1 px-2 rounded small mb-1 order-status">Delivered</p>
                                <p class="small font-weight-bold text-center order-date"><i class="feather-clock"></i> ${order.sale_time}</p>
                            </div>
                        </div>
                        <div class="d-flex pt-3 product_card">`;

                // 遍历每个订单项
                order.order_items.forEach(item => {
                    orderHtml += `
                        <div class="small product-info">
                            <p class="text- font-weight-bold mb-0 name_price">${item.product_name} x ${item.quantity}</p>
                        </div>`;
                });
                orderHtml += `
                        <div class="text-muted m-0 ml-auto mr-3 small total_info">Total Payment<br>
                            <span class="text-dark font-weight-bold total_price">$${order.total_price}</span>
                        </div>
                    </div>
                </div>
            </div>`;

                // 将生成的HTML添加到页面上
                $('.order-body').append(orderHtml);
            });
        },
        error: function(xhr, status, error) {
            console.error("Error fetching order data:", error);
            window.alert("Error fetching order data.");
        }
    });
}


// event of post button
$(document).ready(function() {
    $('#post_btn').click(function(e) {
        e.preventDefault(); // Prevent form submission if inside a form
        submitComment();
    });
});

function submitComment() {
    let orderIdText = $('#order-id').text();
    let orderId = orderIdText.split(': ')[1];
    // get shopRating value
    let shopRating = $('input[name="shopRating"]').val();
    // get product name and productRating
    let productRatings = [];
    $('.product-info').each(function() {
        let productName = $(this).find('.p_name').text().trim();
        let productRating = $(this).find('input[name="productRating"]').val();
        productRatings.push({name: productName, rating: productRating});
    });
    // get comment content
    let commentText = $('textarea[name="commentText"]').val();

    let formData = new FormData();
    formData.append('order_id', orderId);
    formData.append('shopRating', shopRating);
    formData.append('commentText', commentText);
    productRatings.forEach((item, index) => {
        formData.append(`productRatings[${index}][name]`, item.name);
        formData.append(`productRatings[${index}][rating]`, item.rating);
    });

    $.ajax({
        type: "POST",
        url: '/orders/post_comment/',
        data: formData,
        processData: false, // Prevent jQuery from automatically transforming the data into a query string
        contentType: false, // This is set to false since the data sent is a FormData object which needs the Content-Type header set to multipart/form-data
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            window.alert("Comment posted successfully.");
            window.location.href = response.redirect_url;
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Parse error message from response
            let errorMessage = "An error occurred";
            if (jqXHR.responseJSON && jqXHR.responseJSON.error) {
                errorMessage = jqXHR.responseJSON.error;
            }
            alert(`Error: ${errorMessage}`);
        }
    });
}


$(document).ready(function() {
    displayDataInComment()
});