function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

// get order info and display it in html
function getOrder() {
    $.ajax({
        url: '/payment/get_order_storage/',
        type: 'GET',
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            if(response.status === 'success') {
                console.log("Order data retrieved successfully:", response.data);
                // update total price
                $('#total_price').html(`$${response.data.total_price.toFixed(2)}`);
                // update order info
                let ordersHtml = '';
                response.data.orders.forEach(order => {
                    ordersHtml += `<p class="text-center">Order ID: ${order.orderId}</p>`;
                });
                $('#order_id').html(ordersHtml);
            } else {
                console.error("Error retrieving order data:", response.message);
                alert(response.message);
                window.location.href = '/';
            }
        },
        error: function(xhr, status, error) {
            console.error("Error sending order data:", error);
            window.alert("Error retrieving order.");
        }
    });
}


// get all the order id in html
function getOrderIdInfo() {
    let orderIds = [];
    // get order id
    $('#order_id p').each(function() {
        var text = $(this).text();
        var match = text.match(/Order ID: (\d+)/);
        if (match && match[1]) {
            orderIds.push(match[1]);
        }
    });
    return orderIds;
}

// event for pay button
document.getElementById('pay-btn').addEventListener('click', function() {
    console.log('Pay button clicked');
    let orders = getOrderIdInfo();
    let dataToSend = JSON.stringify({
        result: true,
        orders: orders.join(',') // 将数组转换为以逗号分隔的字符串
    });
    console.log("orders:",orders);

    $.ajax({
        type: "POST",
        url: '/payment/payment_view/',
        data: dataToSend,
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            console.log(response.message);
            window.location.href = response.redirect_url;
        },
        error: function(jqXHR, textStatus, errorThrown) {
            let errorMessage = "An unknown error occurred";
            try {
                let responseJson = JSON.parse(jqXHR.responseText);
                if (responseJson.error) {
                    errorMessage = responseJson.error;
                }
            } catch(e) {
                //
            }
            console.error("Error sending data:", textStatus, errorThrown, errorMessage);
            alert("Error: " + errorMessage);
        }
    });
});


// event for cancel button
document.getElementById('cancel-btn').addEventListener('click', function() {
    console.log('Cancel button clicked');
    let orders = getOrderIdInfo();
    let dataToSend = JSON.stringify({
        result: false,
        orders: orders.join(',') // 将数组转换为以逗号分隔的字符串
    });
    console.log("orders:",orders);

    $.ajax({
        type: "POST",
        url: '/payment/payment_view/',
        data: dataToSend,
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            console.log(response.message);
            window.location.href = response.redirect_url;
        },
        error: function(jqXHR, textStatus, errorThrown) {
            let errorMessage = "An unknown error occurred";
            try {
                let responseJson = JSON.parse(jqXHR.responseText);
                if (responseJson.error) {
                    errorMessage = responseJson.error;
                }
            } catch(e) {
                //
            }
            console.error("Error sending data:", textStatus, errorThrown, errorMessage);
            alert("Error: " + errorMessage);
        }
    });
});


$(document).ready(function(){
    getOrder();
    console.log("Initialization complete.");
});
