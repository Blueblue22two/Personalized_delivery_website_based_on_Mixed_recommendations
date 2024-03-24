"use strict"

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}


// 使用ajax request =get，从后端获取my order的数据并按照html中展示
function displayData() {
    $.ajax({
        url: '/orders/get_order/',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            const userType = response.user_type;
            const orders = response.orders;

            // 清空现有的订单信息，以防重复
            $('#completed .order-body').empty();
            $('#progress .order-body').empty();
            $('#canceled .order-body').empty();

            orders.forEach(order => {
                let statusSection = '';
                let sendButtonHtml = '';
                let commentButtonHtml = '';

                // 根据订单状态确定要插入的部分
                if (!order.payment_status) {
                    statusSection = '#canceled .order-body';
                } else if (order.payment_status && !order.delivery_status) {
                    statusSection = '#progress .order-body';
                    if (userType === '2') {
                        sendButtonHtml = `
                            <div class="text-right">
                                <!-- TODO:send button，让js获取该按钮-->
                                <a href="#" class="btn btn-primary px-3 send_btn" data-order-id="${order.order_id}">Send</a>
                            </div>
                        `;
                    }
                } else if (order.payment_status && order.delivery_status) {
                    statusSection = '#completed .order-body';
                    if (userType === '1' && !order.isComment) {
                        commentButtonHtml = `
                            <div class="text-right">
                                <!-- TODO: 获取该order id并替换为<int:id>跳转到对应链接中去-->
                                <a href="/orders/post_comment/<int:id>/" class="btn btn-primary px-3 post_btn" data-order-id="${order.order_id}">post a comment</a>
                            </div>
                        `;
                    }
                }

                // 生成订单的HTML
                let orderHtml = `
                    <div class="pb-3">
                        <div class="p-3 rounded shadow-sm bg-white">
                            <div class="d-flex border-bottom pb-3 store_card">
                                <div class="text-muted mr-3">
                                    <img alt="#" src="/media/${order.shop_image_path}" class="img-fluid order_img rounded shop-logo">
                                </div>
                                <div>
                                    <p class="mb-0 font-weight-bold ">
                                        <a href="/shop/${order.shop_name}/" class="text-dark shop-name">${order.shop_name}</a>
                                    </p>
                                    <p class="mb-0 text-dark font-italic shop-name">${order.shop_address}</p>
                                    <p class="order-id">#${order.order_id}</p>
                                </div>
                                <div class="ml-auto">
                                    <p class="bg-success text-white py-1 px-2 rounded small mb-1 order-status">${order.delivery_status ? 'Delivered' : 'On Process'}</p>
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

// function  displayData(){
//     $.ajax({
//         url: '/orders/get_order/',
//         type: 'GET',
//         dataType: 'json',
//         // TODO:补全下面function
//         success: function() { // TODO:该函数中的参数未知，待修改
//             // TODO:先接受返回的数据中的user_type
//             // 若user_type='1'，表示用户类型为customer
//             // 若user_type='2'，表示用户类型为merchant
//
//             // TODO:接收来自后端传送的数据，然后按照html的example,在对应的order status下生成Order and store info card的html元素并展示
//             // 对于payment_status=False的所有order数据，其所有数据都在order status=canceled的部分生成html
//             // 对于payment_status=True并且delivery_status=False的所有order数据，其所有数据都在order status=progress的部分生成html
//             // 对于payment_status=True并且delivery_status=True的所有order数据，其所有数据都在order status=completed的部分生成html,且html中最开始默认为显示completed的数据
//             // TODO:需要注意的第一点：只有user_type='2'时，对于order status=progress（即payment_status=True并且delivery_status=False）的订单数据中，其中需要在每个product info card添加该html元素(该元素已在html中已告知):
//             // Example:
//             //  <div class="text-right">
//             //     <!-- send button-->
//             //     <a href="" class="btn btn-primary px-3">Send</a>
//             // </div>
//
//             // TODO:需要注意的第二点：user_type='1'时，对于order status=completed（即payment_status=True并且delivery_status=True）并且isComment=False的订单数据中，其中需要在每个product info card添加该html元素(该元素已在html中已告知):
//             // Example:
//             // <!--对于customer显示，该按钮叫post a comment，用于商家发送订单-->
//             // <!--仅对于customer用户，order status='completed并且isComment为False的订单中加入该部分-->
//             // <div class="text-right">
//             //     <!-- post button-->
//             //     <a href="" class="btn btn-primary px-3">post a comment</a>
//             // </div>
//
//             // 注意：对于html中的商店图片用图片路径显示并使用media: "/media/${image_path}"
//         },
//         error: function(xhr, status, error) {
//             console.error("Error fetching sales data:", error);
//         }
//     });
// }


// event of click send_btn
$(document).on('click', '.send_btn', function(e) {
    e.preventDefault(); // 防止链接跳转
    sendOrder(this); // 传递当前点击的按钮作为参数
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
            window.alert(response.message); // 假设后端返回一个包含消息的JSON对象
        },
        error: function(xhr, status, error) {
            console.error("Error sending order data:", error);
            window.alert("Error sending order."); // 提示用户错误信息
        }
    });
}


// event of click post_btn
$(document).ready(function() {
    $('.post_btn').click(function(e) {
        // 阻止默认的链接跳转行为
        e.preventDefault();

        // 获取存储在data-order-id属性中的订单ID
        var orderId = $(this).data('order-id');
        // 构建新的URL，其中<int:id>被替换为实际的订单ID
        var newUrl = '/orders/post_comment/' + orderId + '/';
        // 跳转到新的URL
        window.location.href = newUrl;
    });
});


$(document).ready(function() {
    displayData();
});