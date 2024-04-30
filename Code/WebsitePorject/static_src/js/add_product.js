function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

function addProduct() {
    let name = $("#name").val(); // product name
    let price = $("#price").val(); // product price
    let description = $("#description").val(); // product description
    let category = $("#category").val(); // product category
    let productImage = $("#productImage")[0].files[0]; // product image

    // 验证数据有效性
    if (!name || !price || !description || !category || !productImage) {
        window.alert("Please fill in all items");
        return false;
    }

    if (name.length > 50) {
        window.alert("The name must be less than or equal to 50 characters");
        return false;
    }

    if (/[^\s\w]/.test(name)) {
        window.alert("Cannot contain special characters other than spaces");
        return false;
    }

    if (description.length > 200) {
        window.alert("The description must be less than or equal to 200 characters");
        return false;
    }

    if (productImage.size > 1024 * 1024) {
        window.alert("Image file should have less than 1MB of memory.");
        return false;
    }

    let formData = new FormData();
    formData.append('name', name);
    formData.append('price', price);
    formData.append('description', description);
    formData.append('category', category);
    formData.append('productImage', productImage);

    $.ajax({
        type: "POST",
        url: '/merchants/my_store/add_product',
        data: formData,
        processData: false, // Prevent jQuery from processing the data, making it unsuitable for multipart/form-data
        contentType: false, // Prevent jQuery from setting the incorrect Content-Type request header
        headers: {
            'X-CSRFToken': getCsrfTokenFromForm()
        },
        success: function(response) {
            console.log(response.message);
            setTimeout(function() {
                window.location.href = response.redirect_url;
            }, 500);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            let errorMessage = "An unknown error occurred";
            try {
                let responseJson = JSON.parse(jqXHR.responseText);
                if (responseJson.error) {
                    errorMessage = responseJson.error;
                }
            } catch(e) {
                // Parsing JSON failed, use default error message
            }
            console.error("Error sending data:", textStatus, errorThrown, errorMessage);
            alert("Error: " + errorMessage);
        }
    });

    return false; // Prevent form from submitting normally
}


$(document).ready(function() {
    $('form').on('submit', function(e) {
        e.preventDefault();
        addProduct();
    });
});
