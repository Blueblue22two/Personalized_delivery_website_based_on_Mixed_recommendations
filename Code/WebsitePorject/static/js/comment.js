"use strict"

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

function displayDataInComment() {
    let orderIdText = $('#order-id').text();
    let orderId = orderIdText.split(': ')[1];
    console.log("order id:", orderId);
    $.ajax({
        url: `/orders/get_info/`,
        type: 'POST',
        data: { order_id: orderId },
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            $('.order-body').empty(); // Clear existing order info

            // Loop through each order in the response
            response.orders.forEach((order) => {
                let orderContent = `
                    <div class="p-3 rounded shadow-sm bg-white">
                        <div class="d-flex border-bottom pb-3 store_card">
                            <div class="text-muted mr-3">
                                <img alt="${order.shop_name}" src="/media/${order.shop_image_path}" class="img-fluid order_img rounded shop-logo">
                            </div>
                            <div>
                                <p class="mb-0 fw-bold"><a href="/store/shop/${order.shop_name}/" style="color: red; font-size: 1.5rem; font-weight: bold;" class="text-danger shop-name">${order.shop_name}</a></p>
                                <p class="mb-0 text-dark font-italic shop-address">${order.shop_address}</p>
                            </div>
                            <div class="ml-auto">
                                <p id="order-id" class="small font-weight-bold text-center">Order ID: ${orderId}</p>
                                <p class="small font-weight-bold text-center order-date"><i class = "feather-clock"></i> ${order.sale_time}</p>
                            </div>
                            
                        </div>
                        <div class="shop-rating text-center my-3">
                                <label for="shopRating" class="form-label"><i class="feather-star"></i>Shop rating score:</label>
                                <input type="number" class="form-control" id="shopRating" name="shopRating" min="0" max="5" step="0.1" value="5" required>
                        </div>
                `;

                order.order_items.forEach((item) => {
                    orderContent += `
                        <div class="d-flex justify-content-center align-items-center pt-3 product_card bg-light p-3">
                            <div class="text-center product-info">
                                <p class="font-weight-bold mb-0 p_name">${item.product_name}</p>
                                <p class="font-weight-bold mb-0 p_price">$${item.product_price}</p>
                                <div class="my-2">
                                    <label for="productRating-${item.product_name}" class="form-label"><i class="feather-star"></i>Rate this product:</label>
                                    <input type="number" class="form-control" id="productRating-${item.product_name}" name="productRating" min="0" max="5" step="0.1" value="5" required>
                                </div>
                            </div>
                        </div>
                    `;
                });

                orderContent += `
                    <textarea class="form-control mt-3" name="commentText" rows="3" placeholder="Leave your comment here..." maxlength="225" required></textarea>
                    <button class="btn btn-primary mt-3 d-flex align-items-center justify-content-center" type="submit" id="post_btn"><i class="feather-send"></i> Post</button>
                </div>`;

                $('.order-body').append(orderContent);
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
// submit your comment and rate score
function submitComment() {
    let orderIdText = $('#order-id').text();
    let orderId = orderIdText.split(': ')[1];
    console.log("Order id: ",orderId);

    // get shopRating value
    let shopRating = $('input[name="shopRating"]').val();
    console.log("shopRating: ",shopRating);

    // get product name and productRating
    let productRatings = [];
    $('.product-info').each(function() {
        let productName = $(this).find('.p_name').text().trim();
        let productRating = $(this).find('input[name="productRating"]').val();
        productRatings.push({name: productName, rating: productRating});
    });
    console.log("productRatings: ",productRatings);

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
    displayDataInComment();
});