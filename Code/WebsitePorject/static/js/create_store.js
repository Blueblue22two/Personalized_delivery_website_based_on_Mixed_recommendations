var submitButton = $('#submit_btn');

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}


function createStore(){
    let name = $("#name").val(); // store name
    let province = $('#province').val();
    let city = $('#city').val();
    let distrct = $('#distrct').val();
    let detail = $('#detail').val();
    let fileInput = $('#storeImage')[0]; // get image of store logo
    let file = fileInput.files[0];

    if (name === "") {
        window.alert("Please fill in all items");
        return false;
    }

    // verify image
    if (!fileInput.value) {
        window.alert('Please upload image!');
        return;
    }
    fileInput.setAttribute("accept", "image/jpeg, image/png"); // limit the image file type

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

    let formData = new FormData();
    formData.append('storeImage', file);
    formData.append('name', name);
    formData.append('province', province);
    formData.append('city', city);
    formData.append('distrct',distrct);
    formData.append('detail', detail);

    $.ajax({
        type: "POST",
        url: '/merchants/new/store/',
        data: formData,
        processData: false, // 防止jQuery处理数据，使其不适用于multipart/form-data
        contentType: false, // 防止jQuery设置不正确的Content-Type请求头
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


document.addEventListener("DOMContentLoaded", function() {
  // json path已经在html中定义全局变量
  fetch(jsonPath)
    .then(response => response.json())
    .then(data => {
      populateProvinces(data);  // 用获取到的数据填充省份下拉列表
    });

  // 填充省份下拉列表
  function populateProvinces(data) {
    const provinceSelect = document.getElementById('province');
    data.forEach(item => {
      const option = new Option(item.province, item.province);
      provinceSelect.add(option);
    });

    // 当省份选择改变时，更新城市下拉列表
    provinceSelect.addEventListener('change', function() {
      const selectedProvince = this.value;
      const cities = data.find(item => item.province === selectedProvince).citys;
      populateCities(cities);
    });
  }

  // 填充城市下拉列表
  function populateCities(cities) {
    const citySelect = document.getElementById('city');
    citySelect.innerHTML = '<option selected>Choose a City</option>';  // 重置城市列表
    cities.forEach(cityItem => {
      const option = new Option(cityItem.city, cityItem.city);
      citySelect.add(option);
    });

    // 当城市选择改变时，更新区域下拉列表
    citySelect.addEventListener('change', function() {
      const selectedCity = this.value;
      const areas = cities.find(city => city.city === selectedCity).areas;
      populateAreas(areas);
    });
  }

  // 填充区域下拉列表
  function populateAreas(areas) {
    const areaSelect = document.getElementById('distrct');
    areaSelect.innerHTML = '<option selected>Choose a District</option>';  // 重置区列表
    areas.forEach(areaItem => {
      const option = new Option(areaItem.area, areaItem.area);
      areaSelect.add(option);
    });
  }
});


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