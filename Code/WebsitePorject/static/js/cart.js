

async function getUsernameFromSession() {
    try {
        // 发起请求到 Django 后端以获取用户信息
        const response = await fetch('/accounts/get_user_info');
        // 解析响应的 JSON 数据
        const data = await response.json();

        // check is login or not
        if (data.is_logged_in) {
            console.log("Logged in as", data.username);
            return data.username;
        } else {
            console.log("Not logged in");
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}


getUsernameFromSession().then(username => {
    if (username) {
        console.log("Session username:", username);
    }
});


// get all the address in database and display it
function showAddress(){
    // TODO: 从数据库中获取所有已存储address
    // TODO: 展示address
}


// Get the data from the shopping cart foods and store information and display it
function showCart(){
    // TODO: 从django中 申请数据库中的购物车中的物品信息与对应商品所在商店的信息
    // TODO: 将商品的信息与商店的信息展示出来
    calculateTotalPrice()
}


// TODO:补全函数并创建对应的触发event - change Quantity
function changeQuantity(){
    // TODO: In the Quantity field, check if the user has changed the quantity
    // TODO: and store the change in database
    calculateTotalPrice();
}


// TODO: 实现当用户点击 支付按钮 后的事件
function payment(){
    // TODO:获取商品的价格与信息等等，发送到django后端
    // TODO:若支付成功则弹窗显示支付成功
}


// calculate total price
function calculateTotalPrice() {
  let totalPrice = 0;
  // TODO:获取所有商品价格然后计算出总价格并显示
}


window.addEventListener("load", function() {
  console.log("Loading the page");
  showCart();
  showAddress();
});


