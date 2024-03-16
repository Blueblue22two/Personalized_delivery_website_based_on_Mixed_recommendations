function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

$(document).ready(function() {
    // Display products
    function displayProduct() {
        $.ajax({
            url: '/merchants/my_store/show_product/',
            type: 'GET',
            headers: {
                'X-CSRFToken': getCsrfTokenFromForm()
            },
            success: function(response) {
                // 假设后端返回的response是一个包含商品信息的数组
                response.forEach(product => {
                    $('#productTable tbody').append(`
                        <tr>
                            <td><input type="number" class="Pid" name="productID" readonly="true" value="${product.id}"/></td>
                       
                            <td><img src="/media/${product.image_path}" alt="Product Image" style="width: 100px; height: 100px;"/></td>
                            <td><input type="text" name="productName" value="${product.name}"/></td>
                            <td><input type="number" name="productPrice" min="0.1" step="0.1"  value="${product.price}"/></td>
                            <td><input type="text" name="category" readonly="true" value="${product.category}"/></td>
                            <td><button class="removeBtn" data-id="${product.id}">Remove</button></td>
                            <td><button class="updateBtn" data-id="${product.id}">Update</button></td>
                        </tr>
                    `);
                });
                addEventListeners();
            },error: function(jqXHR, textStatus, errorThrown) {
                    // 尝试解析来自后端的JSON响应体中的错误信息
                    let errorMessage = "An unknown error occurred"; // 默认错误消息
                    try {
                        let responseJson = JSON.parse(jqXHR.responseText);
                        if (responseJson.error) {
                            errorMessage = responseJson.error;
                        }
                    } catch(e) {
                        // 解析JSON失败，使用默认错误消息
                    }
                    console.error("Error sending data:", textStatus, errorThrown, errorMessage);
                    alert("Error: " + errorMessage);
                }
        });
    }

    function update(productID, productName, price) {
        $.ajax({
            url: '/merchants/my_store/modify_product/',
            type: 'POST',
            headers: {
                'X-CSRFToken': getCsrfTokenFromForm()
            },
            data: {
                id: productID,
                name: productName,
                price: price
            },
            success: function(response) {
                alert('Product updated successfully!');
                // Reload products to show the updated info
                $('#productTable tbody').empty();
                displayProduct();
            },error: function(jqXHR, textStatus, errorThrown) {
                    // 尝试解析来自后端的JSON响应体中的错误信息
                    let errorMessage = "An unknown error occurred"; // 默认错误消息
                    try {
                        let responseJson = JSON.parse(jqXHR.responseText);
                        if (responseJson.error) {
                            errorMessage = responseJson.error;
                        }
                    } catch(e) {
                        // 解析JSON失败，使用默认错误消息
                    }
                    console.error("Error sending data:", textStatus, errorThrown, errorMessage);
                    alert("Error: " + errorMessage);
                }
        });
    }

    function removeRow(row) {
        const productID = $(row).data('id');
        $.ajax({
            url: '/merchants/my_store/delete_product/',
            type: 'POST',
            headers: {
                'X-CSRFToken': getCsrfTokenFromForm()
            },
            data: { id: productID },
            success: function(response) {
                alert('Product removed successfully!');
                $(row).closest('tr').remove(); // Remove row from HTML table
            },error: function(jqXHR, textStatus, errorThrown) {
                    // 尝试解析来自后端的JSON响应体中的错误信息
                    let errorMessage = "An unknown error occurred"; // 默认错误消息
                    try {
                        let responseJson = JSON.parse(jqXHR.responseText);
                        if (responseJson.error) {
                            errorMessage = responseJson.error;
                        }
                    } catch(e) {
                        // 解析JSON失败，使用默认错误消息
                    }
                    console.error("Error sending data:", textStatus, errorThrown, errorMessage);
                    alert("Error: " + errorMessage);
                }
        });
    }

    function addEventListeners() {
        $('.updateBtn').click(function() {
            const row = $(this).closest('tr');
            const productID = $(this).data('id');
            const productName = row.find('input[name="productName"]').val();
            const price = row.find('input[name="productPrice"]').val();
            update(productID, productName, price);
        });

        $('.removeBtn').click(function() {
            removeRow(this);
        });
    }
    displayProduct();
});
