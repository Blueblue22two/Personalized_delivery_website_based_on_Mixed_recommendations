function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

document.addEventListener('DOMContentLoaded', () => {
    // get the orders data
    let ordersDataElement = document.getElementById('ordersData');
    let orders = JSON.parse(ordersDataElement.getAttribute('data-orders'));

    // event for pay button
    document.getElementById('pay-btn').addEventListener('click', function() {
        console.log('Pay button clicked');
        let formData = new FormData();
        formData.append('result', true);
        formData.append('orders',orders);
        $.ajax({
            type: "POST",
            url: '/payment/payment/',
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                'X-CSRFToken': getCsrfTokenFromForm()
            },
            success: function(response) {
                console.log(response.message);
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
        let formData = new FormData();
        formData.append('result', false);
        formData.append('orders',orders);
        $.ajax({
            type: "POST",
            url: '/payment/payment/',
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                'X-CSRFToken': getCsrfTokenFromForm()
            },
            success: function(response) {
                console.log(response.message);
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
});