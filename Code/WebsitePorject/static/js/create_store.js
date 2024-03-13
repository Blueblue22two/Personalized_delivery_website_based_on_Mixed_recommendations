var submitButton = $('#submit_btn');


function logOut() {
    window.location.href = '/accounts/logout/';
}


function createStore(){
    let username=null;
    fetch('/accounts/get_user_info/')
        .then(response => response.json())
        .then(data => {
            if (data.is_logged_in) {
                username = data.username;
                console.log("Logged in as", username);
            } else {
                logOut();
                console.log("Not logged in");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            logOut();
        });

    if (username === null){
        console.log("Cookie not exist!");
        return;
    }else{
        console.log("yes")
    }

    let name = $("#name").val(); // store name
    if (name == "") {
        window.alert("Please fill in all items");
        return false;
    }
    // get image of store logo
    var fileInput = $('#storeImage');

    // verify image
    if (!fileInput.value) {
        window.alert('Please upload image!');
        return;
    }
    fileInput.setAttribute("accept", "image/jpeg, image/png"); // limit the image file type
    var file = fileInput.files[0];
    // verify data is valid or not
    if(name.length > 50) {
        window.alert("The name must &lt = 50 characters");
        return false;
    }
    // Determines whether special characters are included
    if (/[^\s\w]/.test(name)) {
        window.alert("Cannot contain special characters other than Spaces");
        return false;
    }
    // Check the size of the image
    if (file.size > 1024 * 1024) {
        console.log("Image file should have less than 1MB of memory.");
        window.alert("Image file should have less than 1MB of memory.");
        return;
    }
    console.log("Data validation has passed");

    // TODO:重写下面部分向后端django发送post申请，存储商店
    var xhr = new XMLHttpRequest();
    xhr.open("POST",  '/merchants/my_store', true);

    // set time out function
    xhr.timeout = 4000; 
    xhr.ontimeout = function () {
        window.alert("Request timeout, please check network connection!");
        console.log("Request timeout, please check network connection!");
        return;
    };
    var formData = new FormData();
    formData.append('storeImage', file);
    formData.append('name', name);
    formData.append('username', username);
    console.log('storeImage: ', file);
    console.log('name: '+name);
    console.log('username: ', username)
    // call back function
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            console.log("Request done");
            closeLoading();
            try {
                var response = JSON.parse(xhr.responseText);
                notification();
                console.log("http status:"+xhr.status);
                if (xhr.status === 200) { // register success and redirect
                    var redirectUrl = response.redirectUrl;
                    console.log("will jump to :"+redirectUrl); 
                    console.log("Register success!!!"); 
                    setTimeout(function(){
                        window.location.href = redirectUrl;
                    }, 500);
                } else if (xhr.status === 400) { // code: 400 bad request
                    console.log("Bad request: "+response.message); 
                    window.alert(response.message); 
                } else {
                    window.alert(response.message); 
                    console.log('HTTP Error: ' + xhr.status); 
                }
            } catch (e) {
                console.log("Parsing response failed :" + e.message);
            }
        }
    };
    // send request
    xhr.send(formData);
}


// add a event, after user click the submit 
submitButton.addEventListener('click',function(event){
    event.preventDefault();
    setTimeout(createStore, 400);
})

window.onload = function() {
    console.log("Loading the page");
    window.alert("You don't have your own store yet, please create one");
};

document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll('.btn');
    buttons.forEach(function(button) {
        button.onmouseover = function() {
            this.style.cursor = 'pointer';
        };
    });
});