
function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

/**
 * Validate that user input is valid
 * return the form is valid or not
 */
function validateForm(formData) {
    // Check if any field is empty
    if (!formData.username || !formData.password || !formData.confirmPassword || !formData.phone) {
        alert('Please fill in all fields.');
        return false;
    }

    // Check if password meets the criteria
    if (formData.password.length < 8 || formData.password.length > 50) {
        alert('Password should be between 8 and 50 characters.');
        return false;
    }

    // Check if passwords match
    if (formData.password !== formData.confirmPassword) {
        alert('Passwords do not match.');
        return false;
    }

    // Check the length of the phone number
    if (formData.phone.length !== 11) {
        alert('The phone number should be 11 digits.');
        return false;
    }

    // Check for special characters in the password
    if (!/^[A-Za-z0-9]+$/.test(formData.password)) {
        alert('Password must not contain special characters.');
        return false;
    }

    // Check for special characters in the phone
    if (!/^[A-Za-z0-9]+$/.test(formData.phone)) {
        alert('phone must not contain special characters.');
        return false;
    }

    // Form is valid
    console.log("Form validation passed")
    return true;
}

// Submit event
$(document).ready(function () {
    $('#registrationForm').submit(function (event) {
        event.preventDefault();

        var formData = {
            username: $('#username').val().trim(),
            password: $('#password').val().trim(),
            confirmPassword: $('#confirm_password').val().trim(),
            phone: $('#phone').val().trim(),
            gender: $('input[name="gender"]:checked').val(),
            userType: $("#userType").text().trim()
        };

        if (!validateForm(formData)) {
            console.log("Validation failed");
        }else{
            // (md5)
            formData.password = md5(formData.password);
            console.log("Hash: ", formData.password);

            // set the url
            let url_regis;
            if (formData.userType === '1'){
                console.log("User type: customer")
                url_regis = "/accounts/register/customer/";
            }else if(formData.userType === '2'){
                console.log("User type: merchant")
                url_regis="/accounts/register/merchant/";
            }else{
                console.log("Error usertype");
                return;
            }

            // send post request
            $.ajax({
                type: "POST",
                url: url_regis,
                data: formData,
                headers: {
                    'X-CSRFToken': getCsrfTokenFromForm()
                },
                success: function (response) {
                    console.log("Data sent successfully!", response.message);
                    alert("Register success");
                    // redirect to main page
                    setTimeout(function(){
                        window.location.href = response.redirect_url;
                    }, 500);
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    let errorMessage = "An unknown error occurred";
                    try {
                        let responseJson = JSON.parse(jqXHR.responseText);
                        if (responseJson.message) {
                            errorMessage = responseJson.message;
                        }
                    } catch(e) {
                        console.error("Error processing response:", e);
                    }
                    console.error("Error sending data:", textStatus, errorThrown, errorMessage);
                    alert("Error: " + errorMessage);
                }
            });
        }
        //
    });
});


 document.addEventListener('DOMContentLoaded', function () {
        // Disable copy, paste, and cut on specified inputs
        var inputs = document.querySelectorAll('#password, #confirm_password, #phone');
        inputs.forEach(function(input) {
            input.addEventListener('copy', function(e) {
                e.preventDefault();
            });
            input.addEventListener('paste', function(e) {
                e.preventDefault();
            });
            input.addEventListener('cut', function(e) {
                e.preventDefault();
            });
        });
 });
