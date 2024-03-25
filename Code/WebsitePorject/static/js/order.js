"use strict"

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}


// 从后端获取my order的数据并按照html中展示
function displayData() {
    $.ajax({
        url: '/orders/get_order/',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            const userType = response.user_type;
            const orders = response.orders; // order data
            // 清空现有的订单信息，以防重复
            $('#completed .order-body').empty();
            $('#progress .order-body').empty();
            $('#canceled .order-body').empty();

            orders.forEach(order => {
                let statusSection = '';
                let sendButtonHtml = '';
                let commentButtonHtml = '';
                console.log("orded if: ",order.order_id);
                console.log("order.payment_status: ",order.payment_status);
                // 根据订单状态确定要插入的部分
                if (!order.payment_status) { // status = Canceled
                    statusSection = '#canceled .order-body';
                } else if (order.payment_status && !order.delivery_status) { // status = Progress
                    statusSection = '#progress .order-body';
                    if (userType === '2') {
                        sendButtonHtml = `
                            <div class="text-right">
                                <!-- TODO:send button，让js获取该按钮-->
                                <a href="#" class="btn btn-primary px-3 send_btn" data-order-id="${order.order_id}">Send</a>
                            </div>
                        `;
                    }
                } else if (order.payment_status && order.delivery_status) { // status = Completed
                    statusSection = '#completed .order-body';
                    if (userType === '1' && !order.isComment) {
                        commentButtonHtml = `
                            <div class="text-right">
                                <a href="/orders/post_comment_view/${order.order_id}/" class="btn btn-primary px-3 post_btn" >post a comment</a>
                            </div>
                        `;
                    }
                }

                // create order info card html
                let orderHtml = `
                    <div class="pb-3">
                        <div class="p-3 rounded shadow-sm bg-white">
                            <div class="d-flex border-bottom pb-3 store_card">
                                <div class="text-muted mr-3">
                                    <img alt="#" src="/media/${order.shop_image_path}" class="img-fluid order_img rounded shop-logo">
                                </div>
                                <div>
                                    <p class="mb-0 font-weight-bold ">
                                        <a href="/store/shop/${order.shop_name}/" class="text-danger shop-name">${order.shop_name}</a>
                                    </p>
                                    <p class="mb-0 text-dark font-italic shop-name">${order.shop_address}</p>
                                    <p class="order-id">id: ${order.order_id}</p>
                                </div>
                                <div class="ml-auto">
                                    <p class="${order.delivery_status ? 'bg-success' : order.payment_status ? 'bg-warning' : 'bg-danger'} text-white py-1 px-2 rounded small mb-1 order-status">${order.delivery_status ? 'Delivered' : order.payment_status ? 'On Process' : 'Canceled'}</p>
                                    <p class="small font-weight-bold text-center order-date"><i class="feather-clock"></i> ${order.sale_time}</p>
                                </div>
                            </div>
                            <div class="d-flex pt-3 product_card">
                                <div class="small product-info">
                `;

                order.order_items.forEach(item => {
                    orderHtml += `<p class="text- font-weight-bold mb-0 name_price">${item.product_name} x ${item.quantity}</p>`;
                });

                orderHtml += `
                                </div>
                                <div class="text-muted m-0 ml-auto mr-3 small total_info">Total Payment<br>
                                    <span class="text-dark font-weight-bold total_price">$${order.total_price}</span>
                                </div>
                                ${sendButtonHtml}
                                ${commentButtonHtml}
                            </div>
                        </div>
                    </div>
                `;

                $(statusSection).append(orderHtml);
            });
        },
        error: function(xhr, status, error) {
            console.error("Error fetching order data:", error);
        }
    });
}

// event of click send_btn
$(document).on('click', '.send_btn', function(e) {
    e.preventDefault();
    sendOrder(this);
});

function sendOrder(element) {
    var orderId = $(element).data('order-id'); // 获取data-order-id属性的值
    $.ajax({
        url: `/orders/send_order/${orderId}/`, // 使用模板字符串插入orderId
        type: 'POST',
        data: { order_id: orderId },
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            console.log(response.message)
            window.alert(response.message);
        },
        error: function(xhr, status, error) {
            console.error("Error sending order data:", error);
            window.alert("Error sending order.");
        }
    });
}

// $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
//   displayData(); // 在这里调用displayData函数重新加载并显示数据
// });

$(document).ready(function() {
    displayData();
});