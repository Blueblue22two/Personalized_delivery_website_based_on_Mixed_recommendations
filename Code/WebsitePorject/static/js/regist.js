<!-- MD5 -->
<script src="https://cdn.bootcss.com/blueimp-md5/2.12.0/js/md5.min.js"/>


/**
 * Validate that user input is valid
 * return the form is valid or not
 */
function validateForm(formData) {
    // Check if any field is empty
    if (!formData.username || !formData.password || !formData.confirmPassword || !formData.phone || !formData.city) {
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

    // Form is valid
    console.log("Form validation passed")
    return true;
}

// Submit event
$(document).ready(function () {
    console.log("Submit...");
    $('#registrationForm').submit(function (event) {
        event.preventDefault(); // 阻止表单提交，等待数据发送完成

        // 提取表单数据
        var formData = {
            username: $('#username').val().trim(),
            password: $('#password').val().trim(),
            confirmPassword: $('#confirm_password').val().trim(),
            phone: $('#phone').val().trim(),
            userType: $("#userType").text().trim()
        };

        // 验证表单数据
        if (!validateForm(formData)) {
            return; // 如果表单验证失败，则不发送数据
        }

        // 加密密码(md5)
        formData.password = md5(formData.password);
        console.log("Hash: ", formData.password);

        // set the url
        let url_regis;
        if (formData.userType === 1){
            url_regis = "accounts/register/customer/";
        }else{
            url_regis="accounts/register/merchant/";
        }

        // 发送POST请求
        $.ajax({
            type: "POST",
            url: url_regis, // 后台Django处理的URL
            data: formData,
            success: function (response) {
                // 处理成功响应
                console.log("Data sent successfully!", response.message);
                // TODO:弹窗显示注册成功
                // TODO:跳转到主页面并登录
            },
            error: function (error) {
                // 处理错误响应
                console.error("Error sending data:", error);
                // TODO:显示错误信息
            }
        });
    });
});
