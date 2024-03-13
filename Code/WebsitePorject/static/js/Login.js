// log in function
function validation(formdata){
    let username = formdata.username;
    let password = formdata.password;

    if (!username.trim()) {
        window.alert("Username cannot be empty.");
        return false;
    }
    if (!password.trim()) {
        window.alert("Password cannot be empty.");
        return false;
    }

    // verify data is valid or not
    if(username.length > 50) {
        window.alert("The username must <= 50 characters");
        return false
    }
    // Determines whether special characters are included
    if (/[\W_]/.test(username)) {
        window.alert("The username cannot contain special characters.");
        return false
    }
    if(password.length > 50) {
        window.alert(".");
        return false
    }
    if (/[\W_]/.test(password)) {

        window.alert("The password cannot contain special characters.");
        return false
    }
    console.log("Data validation has passed");
    return true
}

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

$(document).ready(function() {
    $('form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission

        var formData = {
            username: $('#username').val().trim(),
            password: $('#password').val().trim(),
            userType: $("#userType").text().trim()
        };

        if(!validation(formData)){
            console.log("Verification failed");
            return;
        }
        formData.password = md5(formData.password); // Hash the password
        console.log("Hashed Password: ", formData.password);

        // based on the userType, decide where to send the data
        let loginUrl = '';
        switch (formData.userType) {
            case '1':
                loginUrl = '/accounts/login/customer/'; // Set this to your actual customer login endpoint
                break;
            case '2':
                loginUrl = '/accounts/login/merchant/'; // Set this to your actual merchant login endpoint
                break;
            default:
                window.alert("Invalid user type");
                return;
        }

        // Perform the AJAX request to the server
        $.ajax({
            type: 'POST',
            url: loginUrl,
            data: formData,
            headers: {'X-CSRFToken': getCsrfTokenFromForm()},
            success: function(response) {
                console.log("Login successful: ", response);
                // TODO: Redirect to main page after successful login
                setTimeout(function(){
                    window.location.href = response.redirect_url;
                }, 500);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                    console.error("Error sending data:", textStatus, errorThrown);
                    alert("Error: " + jqXHR.responseText);
            }
        });
    });
});
