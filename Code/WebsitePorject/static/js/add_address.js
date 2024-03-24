function getCsrfTokenFromForm() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

function addAddress() {
    // get form data
    let province = $('#province').val();
    let city = $('#city').val();
    let distrct = $('#distrct').val();
    let detail = $('#detail').val();
    console.log("province: ",province)
    console.log("city: ",city)
    console.log("Distrct",distrct)
    console.log("detail: ",detail)

    let formData = new FormData();
    formData.append('province', province);
    formData.append('city', city);
    formData.append('distrct',distrct);
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
                window.alert('Address added successfully!');
            } else {
                alert('Failed to add address: ' + response.message);
            }
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}


document.addEventListener("DOMContentLoaded", function() {
  // json path已经在html中定义全局变量
  fetch(jsonPath)
    .then(response => response.json())
    .then(data => {
      populateProvinces(data);
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