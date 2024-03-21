-- drop schema if exists OnlineFoodDelivery;

-- Drop tables in reverse order to avoid foreign key constraints
-- DROP TABLE IF EXISTS ShopRatings;
-- DROP TABLE IF EXISTS Orders;
-- DROP TABLE IF EXISTS Comments;
-- DROP TABLE IF EXISTS FavItems;
-- DROP TABLE IF EXISTS Favorites;
-- DROP TABLE IF EXISTS CartItems;
-- DROP TABLE IF EXISTS ShoppingCarts;
-- DROP TABLE IF EXISTS Products;
-- DROP TABLE IF EXISTS Shops;
-- DROP TABLE IF EXISTS Merchants;
-- DROP TABLE IF EXISTS Addresses;
-- DROP TABLE IF EXISTS Customers;
-- DROP TABLE IF EXISTS Admins;

USE OnlineFoodDelivery; -- use this database
-- show tables 
-- show columns from OnlineFoodDelivery.customers

SELECT * FROM accounts_customer;
-- SELECT * FROM accounts_merchant;
-- SELECT * FROM accounts_shop;
-- SELECT * FROM merchants_product;
SELECT * FROM accounts_shoppingcart;
SELECT * FROM cart_cartitem;
-- SELECT * FROM  accounts_favorite;
SELECT * FROM accounts_address;

