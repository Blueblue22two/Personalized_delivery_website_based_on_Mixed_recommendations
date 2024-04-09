
USE OnlineFoodDelivery; -- use this database
-- show tables 
-- show columns from OnlineFoodDelivery.customers
SELECT * FROM accounts_customer WHERE id = 10;
-- SELECT * FROM accounts_merchant;
-- SELECT * FROM accounts_shop;
-- SELECT * FROM merchants_product where id = 47;


-- SELECT * FROM accounts_shoppingcart;
-- SELECT * FROM cart_cartitem;
-- SELECT * FROM orders_order;
-- SELECT * FROM orders_orderitem;
-- SELECT * FROM cart_cartitem;
-- SELECT * FROM  accounts_favorite;
-- SELECT * FROM customers_favitem;
-- SELECT * FROM accounts_address;
-- SELECT * FROM merchants_shoprating where shop_id=7;
-- SELECT * FROM customers_comment;

SELECT COUNT(*) FROM orders_order;

SELECT * FROM orders_order
WHERE payment_status = 1 AND delivery_status = 0;

-- UPDATE orders_order
-- SET delivery_status = 1
-- WHERE payment_status = 1 AND delivery_status = 0;



