-- Create a database
CREATE SCHEMA IF NOT EXISTS OnlineFoodDelivery;

-- Use this databases
USE OnlineFoodDelivery;

-- Administrator table
CREATE TABLE Admins (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Customer table
CREATE TABLE Customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    phone_number VARCHAR(11) NOT NULL,
    fav_id INT, -- id of favorite
    cart_id INT -- id of shopping cart
);

-- Address table (for customer)
CREATE TABLE Addresses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    address_line VARCHAR(255)
);

-- Shopping cart table (for customer)
CREATE TABLE ShoppingCarts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    quantity INT,
    CHECK (quantity <= 100)
);

-- Cart item
CREATE TABLE CartItems (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cart_id INT,
    product_id INT,
    quantity INT CHECK (quantity > 0)
);

-- Merchant table
CREATE TABLE Merchants (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    phone_number VARCHAR(11) NOT NULL,
    shop_id INT
);

-- Shop table
CREATE TABLE Shops (
    id INT PRIMARY KEY AUTO_INCREMENT,
    merchant_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    total_rating DECIMAL(3, 1),
    image_path VARCHAR(255)
);

-- Product table
CREATE TABLE Products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    shop_id INT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2),
    category VARCHAR(255),
    discount_price DECIMAL(10, 2),
    discount_time DATETIME,
    description TEXT,
    image_path VARCHAR(255)
);

-- the total rate of shop
CREATE TABLE ShopRatings (
	id INT PRIMARY KEY AUTO_INCREMENT,
    shop_id INT,
    average_rating DECIMAL(3, 2)
);

-- Favorites table (for customer)
CREATE TABLE Favorites (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    shop_id INT,
    UNIQUE (user_id, shop_id) -- Ensure that a user cannot favorite the same store twice
);

-- Favorite item table
CREATE TABLE FavItems (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    shop_id INT
);

-- Comment table
CREATE TABLE Comments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    text TEXT,
    image_path VARCHAR(255), -- this is optional
    rating DECIMAL(3, 1)
);

-- purchase record table
CREATE TABLE Orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    customer_id INT,
    merchant_id INT,
    product_price DECIMAL(10, 2),
    quantity INT,
    total_price DECIMAL(10, 2),
    sale_time DATETIME,
    order_type ENUM('delivery', 'pick up'),
    order_status ENUM('Order finished','Order closed', 'Order in delivery', 'Wait for picked up')
);

-- Adding Foreign Keys using ALTER TABLE

ALTER TABLE Customers ADD CONSTRAINT fk_fav_id
FOREIGN KEY (fav_id) REFERENCES Favorites(id);

ALTER TABLE Customers ADD CONSTRAINT fk_cart_id
FOREIGN KEY (cart_id) REFERENCES ShoppingCarts(id);

ALTER TABLE Addresses ADD CONSTRAINT fk_customer_id
FOREIGN KEY (customer_id) REFERENCES Customers(id);

ALTER TABLE Merchants ADD CONSTRAINT fk_shop_id_merchants
FOREIGN KEY (shop_id) REFERENCES Shops(id);

ALTER TABLE Shops ADD CONSTRAINT fk_merchant_id_shops
FOREIGN KEY (merchant_id) REFERENCES Merchants(id);

ALTER TABLE Products ADD CONSTRAINT fk_shop_id_products
FOREIGN KEY (shop_id) REFERENCES Shops(id);

ALTER TABLE ShoppingCarts ADD CONSTRAINT fk_customer_id_carts
FOREIGN KEY (customer_id) REFERENCES Customers(id);

ALTER TABLE CartItems ADD CONSTRAINT fk_cart_id_items
FOREIGN KEY (cart_id) REFERENCES ShoppingCarts(id);

ALTER TABLE CartItems ADD CONSTRAINT fk_product_id_items
FOREIGN KEY (product_id) REFERENCES Products(id);

ALTER TABLE Favorites ADD CONSTRAINT fk_user_id_favorites
FOREIGN KEY (user_id) REFERENCES Customers(id);

ALTER TABLE Favorites ADD CONSTRAINT fk_shop_id_favorites
FOREIGN KEY (shop_id) REFERENCES Shops(id);

ALTER TABLE FavItems ADD CONSTRAINT fk_customer_id_favitems
FOREIGN KEY (customer_id) REFERENCES Customers(id);

ALTER TABLE FavItems ADD CONSTRAINT fk_shop_id_favitems
FOREIGN KEY (shop_id) REFERENCES Shops(id);

ALTER TABLE Comments ADD CONSTRAINT fk_customer_id_comments
FOREIGN KEY (customer_id) REFERENCES Customers(id);

ALTER TABLE Comments ADD CONSTRAINT fk_product_id_comments
FOREIGN KEY (product_id) REFERENCES Products(id);

ALTER TABLE Orders ADD CONSTRAINT fk_customer_id_orders
FOREIGN KEY (customer_id) REFERENCES Customers(id);

ALTER TABLE Orders ADD CONSTRAINT fk_merchant_id_orders
FOREIGN KEY (merchant_id) REFERENCES Merchants(id);

ALTER TABLE Orders ADD CONSTRAINT fk_product_id_orders
FOREIGN KEY (product_id) REFERENCES Products(id);

