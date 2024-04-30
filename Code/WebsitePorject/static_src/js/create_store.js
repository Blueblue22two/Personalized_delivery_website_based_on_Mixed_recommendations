var submitButton = $('#submit_btn');

function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}


function createStore(){
    let name = $("#name").val(); // store name
    let province = $('#province').val();
    let city = $('#city').val();
    let district = $('#district').val();
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
    formData.append('district',district);
    formData.append('detail', detail);

    $.ajax({
        type: "POST",
        url: '/merchants/new/store/',
        data: formData,
        processData: false,
        contentType: false,
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
            }
            console.error("Error sending data:", textStatus, errorThrown, errorMessage);
            alert("Error: " + errorMessage);
        }
    });

}


document.addEventListener("DOMContentLoaded", function() {
  fetch(jsonPath)
    .then(response => response.json())
    .then(data => {
      populateProvinces(data);
    });

  function populateProvinces(data) {
    const provinceSelect = document.getElementById('province');
    data.forEach(item => {
      const option = new Option(item.province, item.province);
      provinceSelect.add(option);
    });

    provinceSelect.addEventListener('change', function() {
      const selectedProvince = this.value;
      const cities = data.find(item => item.province === selectedProvince).citys;
      populateCities(cities);
    });
  }

  function populateCities(cities) {
    const citySelect = document.getElementById('city');
    citySelect.innerHTML = '<option selected>Choose a City</option>';  // 重置城市列表
    cities.forEach(cityItem => {
      const option = new Option(cityItem.city, cityItem.city);
      citySelect.add(option);
    });

    citySelect.addEventListener('change', function() {
      const selectedCity = this.value;
      const areas = cities.find(city => city.city === selectedCity).areas;
      populateAreas(areas);
    });
  }

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