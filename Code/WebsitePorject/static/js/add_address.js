function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

function addAddress() {
    // get form data
    let province = $('#province').val();
    let city = $('#city').val();
    let detail = $('#detail').val();
    console.log("province: ",province)
    console.log("city: ",city)
    console.log("detail: ",detail)

    var formData = new FormData();
    formData.append('province', province);
    formData.append('city', city);
    formData.append('detail', detail);

    $.ajax({
        url: '/customers/add_address/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        headers: {'X-CSRFToken': getCsrfTokenFromForm()},
        success: function(response) {
            if (response.status === 'success') {
                alert('Address added successfully!');
            } else {
                alert('Failed to add address: ' + response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}


$(document).ready(function() {
    $('form').on('submit', function(e) {
        e.preventDefault();
        // Verify that none of the data is null
        let allFieldsFilled = true;
        if ($('select[name="province"]').val() === "") {
            allFieldsFilled = false;
            alert('Please choose a province.');
        }
        if ($('select[name="city"]').val() === "") {
            allFieldsFilled = false;
            alert('Please choose a city.');
        }
        if ($('#detail').val().trim() === "") {
            allFieldsFilled = false;
            alert('Please enter a detail address.');
        }

        if (allFieldsFilled) {
            addAddress();
        }
    });
});