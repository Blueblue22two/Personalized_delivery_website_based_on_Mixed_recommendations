-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: onlinefooddelivery
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_address`
--

DROP TABLE IF EXISTS `accounts_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address_line` varchar(255) DEFAULT NULL,
  `customer_id` bigint NOT NULL,
  `city` varchar(25) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `district` varchar(25) NOT NULL,
  `province` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_address_customer_id_224ca293_fk_accounts_customer_id` (`customer_id`),
  CONSTRAINT `accounts_address_customer_id_224ca293_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_address`
--

LOCK TABLES `accounts_address` WRITE;
/*!40000 ALTER TABLE `accounts_address` DISABLE KEYS */;
INSERT INTO `accounts_address` VALUES (3,'四川省-成都市-成华区-CDUT songlin120',4,'成都市','CDUT songlin120','成华区','四川省'),(4,'江苏省-南京市-玄武区-hahha',4,'南京市','hahha','玄武区','江苏省'),(5,'北京市-北京市-朝阳区-jianshe road',4,'北京市','jianshe road','朝阳区','北京市'),(6,'辽宁省-大连市-瓦房店市-dog shop',4,'大连市','dog shop','瓦房店市','辽宁省'),(7,'山东省-济南市-长清区-sanzhong high school',4,'济南市','sanzhong high school','长清区','山东省'),(8,'天津市-天津市-和平区-fandou st',1,'天津市','fandou st','和平区','天津市'),(11,'吉林省-长春市-南关区-fandou st',1,'长春市','fandou st','南关区','吉林省'),(12,'浙江省-温州市-鹿城区-whs ',1,'温州市','whs ','鹿城区','浙江省'),(14,'四川省-成都市-成华区-CDUT',2,'成都市','CDUT','成华区','四川省'),(15,'四川省-成都市-成华区-longguang st.',2,'成都市','longguang st.','成华区','四川省'),(16,'四川省-成都市-成华区-铁建',1,'成都市','铁建','成华区','四川省'),(17,'贵州省-六盘水市-六枝特区-where',6,'六盘水市','where','六枝特区','贵州省'),(18,'浙江省-台州市-路桥区-school',7,'台州市','school','路桥区','浙江省'),(19,'青海省-西宁市-城中区-carzy',8,'西宁市','carzy','城中区','青海省'),(20,'天津市-天津市-西青区-da st.',9,'天津市','da st.','西青区','天津市'),(21,'内蒙古自治区-呼和浩特市-回民区-hui',9,'呼和浩特市','hui','回民区','内蒙古自治区'),(22,'山西省-大同市-云冈区-大同大学',10,'大同市','大同大学','云冈区','山西省'),(23,'四川省-泸州市-江阳区-damn',12,'泸州市','damn','江阳区','四川省');
/*!40000 ALTER TABLE `accounts_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customer`
--

DROP TABLE IF EXISTS `accounts_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer`
--

LOCK TABLES `accounts_customer` WRITE;
/*!40000 ALTER TABLE `accounts_customer` DISABLE KEYS */;
INSERT INTO `accounts_customer` VALUES (1,'calvin','1bbd886460827015e5d605ed44252251','12345678911'),(2,'bob','bae5e3208a3c700e3db642b6631e95b9','12345678911'),(3,'James','25f9e794323b453885f5181f1b624d0b','22345678988'),(4,'Customer4','fbe82b93c071bedda31afded400cca52','12345678911'),(5,'xiangzeqi','25d55ad283aa400af464c76d713c07ad','13808243006'),(6,'reginacustomer','ef775988943825d2871e1cfa75473ec0','33345678965'),(7,'beeflover','60d6ea68bdf457e10a3a18ba34974917','78345678910'),(8,'saladman','f98aa3ec36a5b5086c1a93f689259060','17645676035'),(9,'Customer666','eb0b5599e67e299755bda83b862b23dd','22345678910'),(10,'Zhuzhaoyu','0229c73541dbf156680cb8e3b0cf0fb5','12345678910'),(11,'Ethan Zhu','0229c73541dbf156680cb8e3b0cf0fb5','12345678910'),(12,'Liu金雨','b64f1a77b1b317d347f5cb79332c86d2','14345878913');
/*!40000 ALTER TABLE `accounts_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_favorite`
--

DROP TABLE IF EXISTS `accounts_favorite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_favorite` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `shop_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_favorite_user_id_shop_id_c195a45f_uniq` (`user_id`,`shop_id`),
  KEY `accounts_favorite_shop_id_00c41ad1_fk_accounts_shop_id` (`shop_id`),
  CONSTRAINT `accounts_favorite_shop_id_00c41ad1_fk_accounts_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `accounts_shop` (`id`),
  CONSTRAINT `accounts_favorite_user_id_081a5fb5_fk_accounts_customer_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_favorite`
--

LOCK TABLES `accounts_favorite` WRITE;
/*!40000 ALTER TABLE `accounts_favorite` DISABLE KEYS */;
INSERT INTO `accounts_favorite` VALUES (4,3,1),(7,4,1),(1,5,1),(2,7,1),(36,11,1),(6,2,2),(9,3,2),(13,9,2),(30,1,4),(28,2,4),(10,3,4),(29,4,4),(3,5,4),(5,7,4),(12,8,4),(11,9,4),(27,10,4),(31,12,4),(17,4,6),(16,6,6),(15,7,6),(23,8,6),(14,9,6),(22,10,6),(35,11,6),(19,2,7),(20,4,7),(18,5,7),(34,8,7),(32,10,7),(21,12,7),(26,6,8),(25,7,8),(24,9,8),(41,11,9),(38,13,9),(42,6,12);
/*!40000 ALTER TABLE `accounts_favorite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_merchant`
--

DROP TABLE IF EXISTS `accounts_merchant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_merchant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `shop_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_merchant_shop_id_e1444cf9_fk_accounts_shop_id` (`shop_id`),
  CONSTRAINT `accounts_merchant_shop_id_e1444cf9_fk_accounts_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `accounts_shop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_merchant`
--

LOCK TABLES `accounts_merchant` WRITE;
/*!40000 ALTER TABLE `accounts_merchant` DISABLE KEYS */;
INSERT INTO `accounts_merchant` VALUES (1,'calvin','1bbd886460827015e5d605ed44252251','12345678911',1),(2,'damn','25d55ad283aa400af464c76d713c07ad','22345678910',2),(3,'Dumpling','bae5e3208a3c700e3db642b6631e95b9','22345678910',3),(4,'Beef','d27d320c27c3033b7883347d8beca317','33345678999',4),(5,'Hambuger','b857eed5c9405c1f2b98048aae506792','12345678911',5),(6,'ChinaTown','6ebe76c9fb411be97b3b0d48b791a7c9','98765678911',6),(7,'Fast','d1b2cc725d846f0460ff290c60925070','22345678910',7),(8,'FoodCanteen','25f9e794323b453885f5181f1b624d0b','17711475039',8),(9,'Merchant5','1bbd886460827015e5d605ed44252251','12345678911',9),(10,'Merchant6','d1b2cc725d846f0460ff290c60925070','22345678910',10),(11,'RockRockMerchant','b2023820a60123ef4e6869bacaf7d90c','74345678915',11),(12,'BeefMerchant','22d7fe8c185003c98f97e5d6ced420c7','51365678911',12),(13,'13999','f5c7e3b79fd8c720826692b17eefb4c6','24708045743',13),(14,'MerchantFries','9ae2be73b58b565bce3e47493a56e26a','14765646915',14);
/*!40000 ALTER TABLE `accounts_merchant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_shop`
--

DROP TABLE IF EXISTS `accounts_shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_shop` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `total_rating` decimal(3,1) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `merchant_id` bigint NOT NULL,
  `city` varchar(25) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `district` varchar(25) NOT NULL,
  `province` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_shop_merchant_id_8f01f1ea_fk_accounts_merchant_id` (`merchant_id`),
  CONSTRAINT `accounts_shop_merchant_id_8f01f1ea_fk_accounts_merchant_id` FOREIGN KEY (`merchant_id`) REFERENCES `accounts_merchant` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_shop`
--

LOCK TABLES `accounts_shop` WRITE;
/*!40000 ALTER TABLE `accounts_shop` DISABLE KEYS */;
INSERT INTO `accounts_shop` VALUES (1,'12Food_shop','四川省-成都市-武侯区-52 st',4.4,'12Food_shop\\LOGO\\baozou.png',1,'成都市','52 st','武侯区','四川省'),(2,'Pizza_shop','四川省-成都市-成华区-erxian bridge',4.2,'Pizza_shop\\LOGO\\22489.jpg',2,'成都市','erxian bridge','成华区','四川省'),(3,'Dumpling_store','四川省-成都市-金牛区-haha st',4.2,'Dumpling_store\\LOGO\\62969.jpg',3,'成都市','haha st','金牛区','四川省'),(4,'Beef_store','四川省-成都市-高新区-haha st',4.1,'Beef_store\\LOGO\\118395.jpg',4,'成都市','haha st','高新区','四川省'),(5,'Big_Buger_city','四川省-成都市-金牛区-jianshe road',4.2,'Big_Buger_city\\LOGO\\hamburger-1238246_640.jpg',5,'成都市','jinshan road','金牛区','四川省'),(6,'Chinese_food','四川省-成都市-成华区-erxian bridge',4.0,'Chinese_food\\LOGO\\3046wh300.jpg',6,'成都市','erxian bridge','成华区','四川省'),(7,'2 fast','四川省-成都市-成华区-CDUT',3.9,'2_fast\\LOGO\\1188.jpg_wh300.jpg',7,'成都市','CDUT','成华区','四川省'),(8,'Food canteen','四川省-宜宾市-叙州区-55 st',4.2,'Food_canteen\\LOGO\\109357.jpg',8,'宜宾市','55 st','叙州区','四川省'),(9,'Crazy_Dave_shop','四川省-宜宾市-屏山县-junshan road',4.4,'Crazy_Dave_shop\\LOGO\\img.png',9,'宜宾市','junshan road','屏山县','四川省'),(10,'The Mystery Shop','四川省-乐山市-沐川县-have a guess',4.2,'The_Mystery_Shop\\LOGO\\58582c1cf034562c58220600.png',10,'乐山市','have a guess','沐川县','四川省'),(11,'The rock official','上海市-上海市-黄浦区-Rock st.',4.0,'The_rock_official\\LOGO\\R-C.jfif',11,'上海市','Rock st.','黄浦区','上海市'),(12,'Beef home','吉林省-长春市-宽城区-cow st.',4.3,'Beef_home\\LOGO\\677746.jpg',12,'长春市','cow st.','宽城区','吉林省'),(13,'Loopy canteen ','重庆市-重庆市-城口县-hongya ',4.5,'Loopy_canteen_\\LOGO\\CC1774B4-6AFE-4B78-955A-EA6ED22597D0.jpeg',13,'重庆市','hongya ','城口县','重庆市'),(14,'Fries home','四川省-泸州市-合江县-idk',0.0,'Fries_home\\LOGO\\106608.jpg',14,'泸州市','idk','合江县','四川省');
/*!40000 ALTER TABLE `accounts_shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_shoppingcart`
--

DROP TABLE IF EXISTS `accounts_shoppingcart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_shoppingcart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_shoppingcar_customer_id_27975165_fk_accounts_` (`customer_id`),
  CONSTRAINT `accounts_shoppingcar_customer_id_27975165_fk_accounts_` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_shoppingcart`
--

LOCK TABLES `accounts_shoppingcart` WRITE;
/*!40000 ALTER TABLE `accounts_shoppingcart` DISABLE KEYS */;
INSERT INTO `accounts_shoppingcart` VALUES (1,0,1),(2,0,2),(3,0,3),(4,0,4),(5,0,5),(6,0,6),(7,0,7),(8,0,8),(9,0,9),(10,0,10),(11,0,11),(12,0,12);
/*!40000 ALTER TABLE `accounts_shoppingcart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `address_line` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_customer_id` (`customer_id`),
  CONSTRAINT `fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add address',7,'add_address'),(26,'Can change address',7,'change_address'),(27,'Can delete address',7,'delete_address'),(28,'Can view address',7,'view_address'),(29,'Can add favorite',8,'add_favorite'),(30,'Can change favorite',8,'change_favorite'),(31,'Can delete favorite',8,'delete_favorite'),(32,'Can view favorite',8,'view_favorite'),(33,'Can add shopping cart',9,'add_shoppingcart'),(34,'Can change shopping cart',9,'change_shoppingcart'),(35,'Can delete shopping cart',9,'delete_shoppingcart'),(36,'Can view shopping cart',9,'view_shoppingcart'),(37,'Can add merchant',10,'add_merchant'),(38,'Can change merchant',10,'change_merchant'),(39,'Can delete merchant',10,'delete_merchant'),(40,'Can view merchant',10,'view_merchant'),(41,'Can add customer',11,'add_customer'),(42,'Can change customer',11,'change_customer'),(43,'Can delete customer',11,'delete_customer'),(44,'Can view customer',11,'view_customer'),(45,'Can add shop',12,'add_shop'),(46,'Can change shop',12,'change_shop'),(47,'Can delete shop',12,'delete_shop'),(48,'Can view shop',12,'view_shop'),(49,'Can add Comment',13,'add_comment'),(50,'Can change Comment',13,'change_comment'),(51,'Can delete Comment',13,'delete_comment'),(52,'Can view Comment',13,'view_comment'),(53,'Can add Favorite Item',14,'add_favitem'),(54,'Can change Favorite Item',14,'change_favitem'),(55,'Can delete Favorite Item',14,'delete_favitem'),(56,'Can view Favorite Item',14,'view_favitem'),(57,'Can add product',15,'add_product'),(58,'Can change product',15,'change_product'),(59,'Can delete product',15,'delete_product'),(60,'Can view product',15,'view_product'),(61,'Can add shop rating',16,'add_shoprating'),(62,'Can change shop rating',16,'change_shoprating'),(63,'Can delete shop rating',16,'delete_shoprating'),(64,'Can view shop rating',16,'view_shoprating'),(65,'Can add order',17,'add_order'),(66,'Can change order',17,'change_order'),(67,'Can delete order',17,'delete_order'),(68,'Can view order',17,'view_order'),(69,'Can add cart item',18,'add_cartitem'),(70,'Can change cart item',18,'change_cartitem'),(71,'Can delete cart item',18,'delete_cartitem'),(72,'Can view cart item',18,'view_cartitem'),(73,'Can add order item',19,'add_orderitem'),(74,'Can change order item',19,'change_orderitem'),(75,'Can delete order item',19,'delete_orderitem'),(76,'Can view order item',19,'view_orderitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$JJ7FTxi01vsl7HGXp2jshj$Z8WuUg3w6MUUtRvuoufp7DLVGJGK+AFyu4EcpmVXZ0A=','2024-04-07 10:02:17.296193',1,'Blueblue2222','','','blueblue22@outlook.com',1,1,'2024-04-07 10:01:36.403298');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_cartitem`
--

DROP TABLE IF EXISTS `cart_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `cart_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_cartitem_cart_id_370ad265_fk_accounts_shoppingcart_id` (`cart_id`),
  KEY `cart_cartitem_product_id_b24e265a_fk_merchants_product_id` (`product_id`),
  CONSTRAINT `cart_cartitem_cart_id_370ad265_fk_accounts_shoppingcart_id` FOREIGN KEY (`cart_id`) REFERENCES `accounts_shoppingcart` (`id`),
  CONSTRAINT `cart_cartitem_product_id_b24e265a_fk_merchants_product_id` FOREIGN KEY (`product_id`) REFERENCES `merchants_product` (`id`),
  CONSTRAINT `quantity_gt_0` CHECK ((`quantity` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=262 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_cartitem`
--

LOCK TABLES `cart_cartitem` WRITE;
/*!40000 ALTER TABLE `cart_cartitem` DISABLE KEYS */;
INSERT INTO `cart_cartitem` VALUES (4,2,5,28),(5,3,5,29),(197,1,1,16),(198,1,1,17),(199,1,1,18),(200,1,1,13);
/*!40000 ALTER TABLE `cart_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cartitems`
--

DROP TABLE IF EXISTS `cartitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cartitems` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cart_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_cart_id_items` (`cart_id`),
  KEY `fk_product_id_items` (`product_id`),
  CONSTRAINT `fk_cart_id_items` FOREIGN KEY (`cart_id`) REFERENCES `shoppingcarts` (`id`),
  CONSTRAINT `fk_product_id_items` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `cartitems_chk_1` CHECK ((`quantity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cartitems`
--

LOCK TABLES `cartitems` WRITE;
/*!40000 ALTER TABLE `cartitems` DISABLE KEYS */;
/*!40000 ALTER TABLE `cartitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `text` text,
  `image_path` varchar(255) DEFAULT NULL,
  `rating` decimal(3,1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_customer_id_comments` (`customer_id`),
  KEY `fk_product_id_comments` (`product_id`),
  CONSTRAINT `fk_customer_id_comments` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `fk_product_id_comments` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `fav_id` int DEFAULT NULL,
  `cart_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_fav_id` (`fav_id`),
  KEY `fk_cart_id` (`cart_id`),
  CONSTRAINT `fk_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `shoppingcarts` (`id`),
  CONSTRAINT `fk_fav_id` FOREIGN KEY (`fav_id`) REFERENCES `favorites` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_comment`
--

DROP TABLE IF EXISTS `customers_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `rating` decimal(3,1) NOT NULL,
  `customer_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customers_comment_customer_id_2dad595b_fk_accounts_customer_id` (`customer_id`),
  KEY `customers_comment_product_id_8e023894_fk_merchants_product_id` (`product_id`),
  CONSTRAINT `customers_comment_customer_id_2dad595b_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `customers_comment_product_id_8e023894_fk_merchants_product_id` FOREIGN KEY (`product_id`) REFERENCES `merchants_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=221 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_comment`
--

LOCK TABLES `customers_comment` WRITE;
/*!40000 ALTER TABLE `customers_comment` DISABLE KEYS */;
INSERT INTO `customers_comment` VALUES (1,'just so so',4.0,1,9),(2,'good food',4.5,2,44),(3,'really good',5.0,2,35),(4,'really good',5.0,2,33),(5,'da',5.0,2,37),(6,'da',5.0,2,38),(7,'da',3.0,2,39),(8,'da',4.0,2,40),(9,'just soso',3.9,2,44),(10,'just soso',4.5,2,42),(11,'normal',3.9,2,11),(12,'great',4.1,2,43),(13,'just soso you know',4.3,1,37),(14,'just soso you know',3.5,1,38),(15,'what?',4.1,1,16),(16,'what?',3.7,1,17),(17,'what?',3.1,1,18),(18,'ha',4.8,1,43),(19,'ha',3.9,1,44),(20,'very bad but good',4.7,4,41),(21,'so small',4.0,4,15),(22,'d',4.7,4,37),(23,'d',3.9,4,38),(24,'what',4.8,4,42),(25,'what',4.2,4,44),(26,'not bad',4.5,2,31),(27,'not bad',3.6,2,30),(28,'not bad',4.1,2,29),(29,'too expensive!',2.8,2,41),(30,'i love it',4.3,1,49),(31,'not bad',4.3,1,37),(32,'not bad',3.8,1,38),(33,'i love PVZ!',5.0,1,45),(34,'i love PVZ!',4.8,1,46),(35,'??S',4.2,1,21),(36,'??S',4.0,1,22),(37,'WOW',4.2,1,42),(38,'WOW',4.0,1,44),(39,'best plants in PVZ',4.9,1,52),(40,'best plants in PVZ',4.5,1,45),(41,'so good, i love this',4.6,1,54),(42,'i dont like this!',2.9,1,11),(43,'i dont like this!',3.0,1,10),(44,'i dont like this!',3.5,1,8),(45,'haha, not bad, i like this favor of uk',4.8,6,19),(46,'haha, not bad, i like this favor of uk',3.9,6,15),(47,'i love beef',4.5,6,36),(48,'i love beef',5.0,6,33),(49,'i love beef',3.9,6,32),(50,'good chinese food',4.1,6,8),(51,'good chinese food',4.3,6,10),(52,'good chinese food',5.0,6,11),(53,'good plant',4.4,2,52),(54,'good plant',4.5,2,46),(55,'?',4.1,2,54),(56,'?',2.5,2,53),(57,'hao chi',4.0,1,33),(58,'hao chi',4.8,1,32),(59,'hao chi',4.6,1,35),(60,'yummy',5.0,7,32),(61,'yummy',4.9,7,33),(62,'yummy',4.8,7,34),(63,'hahahha',4.5,7,55),(64,'delicious dumping',4.3,2,29),(65,'delicious dumping',4.7,2,30),(66,'best chinese food',4.3,2,11),(67,'best chinese food',4.4,2,8),(68,'best chinese food',4.0,2,12),(69,'normal',3.6,1,31),(70,'normal',4.0,1,29),(71,'Rock rock',4.2,2,58),(72,'really good',4.2,4,22),(73,'really good',4.9,4,51),(74,'eeee',3.7,4,31),(75,'great',4.4,4,45),(76,'great',4.6,4,52),(77,'just normal salad',4.1,4,17),(78,'just normal salad',4.0,4,16),(79,'i love all fries',4.8,4,19),(80,'i love all fries',5.0,4,13),(81,'!!!!',4.6,4,39),(82,'!!!!',4.8,4,40),(83,'!!!!',3.8,4,38),(84,'qwq',4.6,4,47),(85,'qwq',2.5,4,41),(86,'crazy',4.5,4,40),(87,'crazy',5.0,4,39),(88,'da',4.1,4,54),(89,'da',3.0,4,53),(90,'i dont like rock',3.0,4,57),(91,'i dont like rock',3.0,4,56),(92,'chinese food',4.0,4,50),(93,'chinese food',4.1,4,20),(94,'dada',4.5,4,36),(95,'dada',4.8,4,32),(96,'just soso',3.9,4,42),(97,'just soso',4.0,4,43),(98,'dawad',3.0,4,53),(99,'dawad',4.5,4,54),(100,'worst',2.8,4,44),(101,'dawq',2.8,4,38),(102,'dawq',2.0,4,37),(103,'dawq',4.5,4,39),(104,'expensive but yummy',4.0,4,59),(105,'expensive but yummy',3.8,4,60),(106,'zc',4.4,7,54),(107,'zc',3.0,7,53),(108,'great beef!!',4.5,7,59),(109,'great beef!!',4.7,7,60),(110,'dsawq',4.6,7,54),(111,'dsawq',3.0,7,53),(112,'dazx',3.6,7,39),(113,'dazx',4.7,7,55),(114,'not good at to make steak',3.8,7,43),(115,'rsg',4.2,7,60),(116,'rsg',4.7,7,59),(117,'dwq',3.6,7,43),(118,'good pizza',4.6,7,21),(119,'good pizza',4.5,7,51),(120,'qwdjkj',4.0,7,30),(121,'qwdjkj',4.1,7,29),(122,'bad rock salad',3.5,7,56),(123,'bad rock salad',3.8,7,57),(124,'bad rock salad',4.0,7,58),(125,'i dont like pvz',3.6,7,45),(126,'i dont like pvz',3.0,7,46),(127,'i dont like pvz',3.5,7,52),(128,'ilke',5.0,6,50),(129,'dasdq',4.5,6,30),(130,'dasdq',5.0,6,29),(131,'dawd',4.6,6,8),(132,'adw',4.5,6,11),(133,'adw',4.5,6,9),(134,'chies',4.1,6,48),(135,'chies',4.0,6,49),(136,'idontlikepizza',3.8,6,21),(137,'idontlike',3.8,6,13),(138,'idontlike',3.9,6,38),(139,'asd',3.4,6,42),(140,'asd',4.4,6,43),(141,'salad i love it',4.8,6,17),(142,'salad i love it',4.6,6,16),(143,'hahahha,PVZ',4.6,6,46),(144,'hahahha,PVZ',4.3,6,45),(145,'hahahha,PVZ',4.4,6,52),(146,'DA',4.0,6,59),(147,'DA',3.6,6,60),(148,'NOT BAD',4.2,6,56),(149,'NOT BAD',4.0,6,57),(150,'NOT BAD',4.6,6,58),(151,'normal salad,but i like rock',4.0,1,56),(152,'normal salad,but i like rock',4.0,1,57),(153,'normal salad,but i like rock',4.1,1,58),(154,'ga',3.8,1,55),(155,'ga',4.2,1,37),(156,'pizza man',4.7,1,51),(157,'pizza man',4.8,1,21),(158,'what can i say',4.6,1,40),(159,'what can i say',4.8,1,39),(160,'good one',4.0,9,62),(161,'good one',4.0,9,63),(162,'das',4.7,9,60),(163,'das',4.0,9,59),(164,'ga',3.7,9,37),(165,'ga',5.0,9,38),(166,'ga',4.1,9,55),(167,'damn',3.0,9,11),(168,'damn',3.0,9,9),(169,'has',4.8,9,58),(170,'has',3.9,9,57),(171,'kj4',4.0,9,51),(172,'kj4',4.0,9,21),(173,'kj4',4.1,9,22),(174,'i love loopy bro',4.5,9,62),(175,'i love loopy bro',4.3,9,63),(176,'great',4.9,9,22),(177,'hahha , i love this',4.8,9,52),(178,'hahha , i love this',4.8,9,45),(179,'great',4.7,9,57),(180,'great',4.5,9,58),(181,'loopy!!!',4.5,9,62),(182,'loopy!!!',4.4,9,63),(183,'dada',4.5,9,58),(184,'dada',4.6,9,56),(185,'eeee,,terrible',3.5,9,35),(186,'eeee,,terrible',3.6,9,32),(187,'eeee,,terrible',3.8,9,33),(188,'bad food i\'ve ever seen',3.0,9,11),(189,'bad food i\'ve ever seen',3.4,9,10),(190,'bad food i\'ve ever seen',3.8,9,9),(191,'bad food i\'ve ever seen',3.7,9,12),(192,'love salad',4.6,9,22),(193,'crazy salad',4.7,9,16),(194,'crazy salad',4.8,9,17),(195,'crazy salad',4.3,9,18),(196,'just soso,u know',3.2,9,43),(197,'just soso,u know',4.0,9,42),(198,'da',3.2,9,11),(199,'da',3.6,9,10),(200,'朱照宇说很好吃',0.0,10,13),(201,'smell good!',4.3,12,11),(202,'smell good!',4.7,12,9),(203,'emmm',4.9,7,43),(204,'emmm',3.5,7,42),(205,'emmm',3.0,7,44),(206,'e',4.7,7,32),(207,'e',4.6,7,33),(208,'e',4.6,7,34),(209,'e',3.8,7,35),(210,'e',3.6,7,36),(211,'hahah, i love beef',4.6,7,59),(212,'hahah, i love beef',4.6,7,60),(213,'i dontlike fries',3.6,7,40),(214,'daq',3.7,7,15),(215,'hahah',4.2,7,53),(216,'hahah',4.9,7,54),(217,'hahah',3.6,7,49),(218,'ooomg',4.8,7,59),(219,'ooomg',4.9,7,60),(220,'good pizza',4.6,7,42);
/*!40000 ALTER TABLE `customers_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_favitem`
--

DROP TABLE IF EXISTS `customers_favitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers_favitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customers_favitem_customer_id_product_id_58adb41e_uniq` (`customer_id`,`product_id`),
  KEY `customers_favitem_product_id_4187b862_fk_merchants_product_id` (`product_id`),
  CONSTRAINT `customers_favitem_customer_id_db237ce3_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `customers_favitem_product_id_4187b862_fk_merchants_product_id` FOREIGN KEY (`product_id`) REFERENCES `merchants_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_favitem`
--

LOCK TABLES `customers_favitem` WRITE;
/*!40000 ALTER TABLE `customers_favitem` DISABLE KEYS */;
INSERT INTO `customers_favitem` VALUES (2,1,9),(6,1,11),(29,1,32),(8,1,37),(7,1,38),(5,1,43),(10,1,46),(9,1,54),(3,2,42),(4,2,43),(20,4,19),(21,4,36),(23,4,39),(24,4,40),(1,4,42),(22,4,47),(28,6,16),(27,6,18),(15,7,32),(14,7,33),(13,7,34),(44,7,42),(12,7,43),(11,7,55),(26,7,59),(25,7,60),(16,8,16),(17,8,17),(18,8,18),(19,8,45),(38,9,16),(40,9,17),(39,9,18),(37,9,22),(32,9,38),(33,9,45),(36,9,52),(35,9,57),(34,9,58),(31,9,63),(41,10,13),(43,12,11),(42,12,13);
/*!40000 ALTER TABLE `customers_favitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'accounts','address'),(11,'accounts','customer'),(8,'accounts','favorite'),(10,'accounts','merchant'),(12,'accounts','shop'),(9,'accounts','shoppingcart'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(18,'cart','cartitem'),(5,'contenttypes','contenttype'),(13,'customers','comment'),(14,'customers','favitem'),(15,'merchants','product'),(16,'merchants','shoprating'),(17,'orders','order'),(19,'orders','orderitem'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-11-15 09:37:16.387711'),(2,'auth','0001_initial','2023-11-15 09:37:16.746239'),(3,'admin','0001_initial','2023-11-15 09:37:16.842131'),(4,'admin','0002_logentry_remove_auto_add','2023-11-15 09:37:16.851140'),(5,'admin','0003_logentry_add_action_flag_choices','2023-11-15 09:37:16.860141'),(6,'contenttypes','0002_remove_content_type_name','2023-11-15 09:37:16.927268'),(7,'auth','0002_alter_permission_name_max_length','2023-11-15 09:37:16.968291'),(8,'auth','0003_alter_user_email_max_length','2023-11-15 09:37:16.990322'),(9,'auth','0004_alter_user_username_opts','2023-11-15 09:37:16.998325'),(10,'auth','0005_alter_user_last_login_null','2023-11-15 09:37:17.038160'),(11,'auth','0006_require_contenttypes_0002','2023-11-15 09:37:17.041159'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-15 09:37:17.051161'),(13,'auth','0008_alter_user_username_max_length','2023-11-15 09:37:17.099172'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-15 09:37:17.142891'),(15,'auth','0010_alter_group_name_max_length','2023-11-15 09:37:17.160796'),(16,'auth','0011_update_proxy_permissions','2023-11-15 09:37:17.170792'),(17,'auth','0012_alter_user_first_name_max_length','2023-11-15 09:37:17.215749'),(18,'sessions','0001_initial','2023-11-15 09:37:17.243747'),(19,'accounts','0001_initial','2024-03-10 06:42:12.388217'),(20,'merchants','0001_initial','2024-03-15 15:47:26.427132'),(21,'customers','0001_initial','2024-03-15 15:47:26.587175'),(22,'customers','0002_initial','2024-03-15 15:47:26.896392'),(23,'orders','0001_initial','2024-03-15 15:47:27.168463'),(24,'cart','0001_initial','2024-03-19 12:57:38.256863'),(25,'accounts','0002_address_city_address_detail_address_district_and_more','2024-03-21 12:21:21.210430'),(26,'orders','0002_order_address_line_order_delivery_status_and_more','2024-03-21 12:21:21.282200'),(27,'orders','0003_remove_order_product_remove_order_product_price_and_more','2024-03-22 14:17:59.362857'),(28,'orders','0004_order_iscomment','2024-03-23 05:09:43.712784'),(29,'merchants','0002_product_average_rate','2024-03-26 10:51:54.291585');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('265gzdvjla8u1zdup0goc9e9tqpkphpn','eyJ1c2VybmFtZSI6InhpYW5nemVxaSIsInVzZXJfdHlwZSI6IjEifQ:1rnCQE:qNo5moQvFJxg1xxPB0ATP6gBzNR44R7I7f9azUQllBM','2024-04-04 07:01:06.008370'),('k1elev1dt0azqsw13atkxjy4zk0zymkl','eyJ1c2VybmFtZSI6IjEzOTk5IiwidXNlcl90eXBlIjoiMiJ9:1rtRoT:IRPdE265fbbwJ-4F8nVtm7gN6tHGu8SnTudn2EPiDe4','2024-04-21 12:39:57.315784'),('ldtvq4fv5ofd876rhj6e3zs1293kg7kx','eyJ1c2VybmFtZSI6Ik1lcmNoYW50RnJpZXMiLCJ1c2VyX3R5cGUiOiIyIn0:1ru7n5:7vjAOfkHBm7GfU5B3tRzbatrzECdhZCefXt06bqeQvE','2024-04-23 09:29:19.959220'),('pgpzo4k5rh39hm8qglmamisam6lw40ti','eyJ1c2VybmFtZSI6ImNhbHZpbiIsInVzZXJfdHlwZSI6IjEifQ:1rnDh7:E-TRQ1RBC_7h7kR0SQWaRXb8LcH_lhsUaBPnxV2sDFs','2024-04-04 08:22:37.787381');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favitems`
--

DROP TABLE IF EXISTS `favitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favitems` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `shop_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_customer_id_favitems` (`customer_id`),
  KEY `fk_shop_id_favitems` (`shop_id`),
  CONSTRAINT `fk_customer_id_favitems` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `fk_shop_id_favitems` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favitems`
--

LOCK TABLES `favitems` WRITE;
/*!40000 ALTER TABLE `favitems` DISABLE KEYS */;
/*!40000 ALTER TABLE `favitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorites` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `shop_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`shop_id`),
  KEY `fk_shop_id_favorites` (`shop_id`),
  CONSTRAINT `fk_shop_id_favorites` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`),
  CONSTRAINT `fk_user_id_favorites` FOREIGN KEY (`user_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `merchants`
--

DROP TABLE IF EXISTS `merchants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `merchants` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `shop_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_shop_id_merchants` (`shop_id`),
  CONSTRAINT `fk_shop_id_merchants` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchants`
--

LOCK TABLES `merchants` WRITE;
/*!40000 ALTER TABLE `merchants` DISABLE KEYS */;
/*!40000 ALTER TABLE `merchants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `merchants_product`
--

DROP TABLE IF EXISTS `merchants_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `merchants_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `category` varchar(255) NOT NULL,
  `discount_price` decimal(10,2) DEFAULT NULL,
  `discount_time` datetime(6) DEFAULT NULL,
  `description` longtext NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `shop_id` bigint NOT NULL,
  `average_rate` decimal(3,1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `merchants_product_shop_id_98919793_fk_accounts_shop_id` (`shop_id`),
  CONSTRAINT `merchants_product_shop_id_98919793_fk_accounts_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `accounts_shop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchants_product`
--

LOCK TABLES `merchants_product` WRITE;
/*!40000 ALTER TABLE `merchants_product` DISABLE KEYS */;
INSERT INTO `merchants_product` VALUES (8,'shrimp dumpling',12.80,'Chinese food',NULL,NULL,'good','Chinese_food\\Products\\shrimp_dumpling\\325914.jpg',6,4.2),(9,'Chive and pork dumplings',11.00,'Chinese food',NULL,NULL,'dafa','Chinese_food\\Products\\Chive_and_pork_dumplings\\3890813.jpg',6,4.0),(10,'Dumplings with crab roe',38.00,'Chinese food',NULL,NULL,'dada','Chinese_food\\Products\\Dumplings_with_crab_roe\\593.jpg',6,3.6),(11,'egg fried rice',18.00,'Chinese food',NULL,NULL,'really good','Chinese_food\\Products\\egg_fried_rice\\108226.jpg',6,3.8),(12,'fried rice with shredded meat',22.00,'Chinese food',NULL,NULL,'yummyyyyyyyyyyy','Chinese_food\\Products\\fried_rice_with_shredded_meat\\1391.jpg',6,3.9),(13,'Extra super big burger',89.00,'Burger',NULL,NULL,'so big!!!','2_fast\\Products\\Extra_super_big_burger\\83196.jpg',7,2.9),(15,'Extra small fish and chips',5.90,'Fries',NULL,NULL,'small','2_fast\\Products\\Extra_small_fish_and_chips\\403380.jpg',7,3.9),(16,'Healthy greek salad',99.00,'Salad',NULL,NULL,'?','2_fast\\Products\\Healthy_greek_salad\\23497.jpg',7,4.4),(17,'Seaweed salad',13.80,'Salad',NULL,NULL,'sae','2_fast\\Products\\Seaweed_salad\\2978247.jpg',7,4.4),(18,'beet salad',108.00,'Salad',NULL,NULL,'expensive','2_fast\\Products\\beet_salad\\173220.jpg',7,3.7),(19,'Fish and chips',8.80,'Fries',NULL,NULL,'da','2_fast\\Products\\Fish_and_chips\\4128.jpg',7,4.8),(20,'Shrimp rice',42.00,'Chinese food',NULL,NULL,'f','Food_canteen\\Products\\Shrimp_rice\\116708.jpg',8,4.1),(21,'Italian pizza',38.80,'Pizza',NULL,NULL,'good','Food_canteen\\Products\\Italian_pizza\\144631.jpg',8,4.3),(22,'Caser salad',88.80,'Salad',NULL,NULL,'da','Food_canteen\\Products\\Caser_salad\\242466.jpg',8,4.4),(28,'Large dumplings stuffed with chives',25.00,'Chinese food',NULL,NULL,'da','Dumpling_store\\Products\\Large_dumplings_stuffed_with_chives\\3890813.jpg',3,0.0),(29,'Extra Large dumplings stuffed with chives',32.00,'Chinese food',NULL,NULL,'too much','Dumpling_store\\Products\\Extra_Large_dumplings_stuffed_with_chives\\3890813.jpg',3,4.3),(30,'Crab Dumplings in Soup',42.00,'Chinese food',NULL,NULL,'yummy yummy','Dumpling_store\\Products\\Crab_Dumplings_in_Soup\\15535.jpg',3,4.2),(31,'It is just a salad',8.00,'Salad',NULL,NULL,'?','Dumpling_store\\Products\\It_is_just_a_salad\\387912.jpg',3,3.9),(32,'ribeye steak',66.00,'Steak',NULL,NULL,'heLLL','Beef_store\\Products\\ribeye_steak\\66183.jpg',4,4.5),(33,'Spicy ribs',50.00,'Steak',NULL,NULL,'12134568','Beef_store\\Products\\Spicy_ribs\\37492.jpg',4,4.6),(34,'filet steak',72.00,'Steak',NULL,NULL,'46653','Beef_store\\Products\\filet_steak\\168551.jpg',4,4.7),(35,'fried rice',34.00,'Chinese food',NULL,NULL,'555','Beef_store\\Products\\fried_rice\\320052.jpg',4,4.2),(36,'MC fish and chips',99.00,'Fries',NULL,NULL,'goddd','Beef_store\\Products\\MC_fish_and_chips\\186030.jpg',4,4.2),(37,'Spicy hell burger package',46.90,'Burger',NULL,NULL,'dm','Big_Buger_city\\Products\\Spicy_hell_burger_package\\2316148.jpg',5,4.0),(38,'Beef sandwich',20.00,'Sandwich',NULL,NULL,'beefff','Big_Buger_city\\Products\\Beef_sandwich\\hamburger-1238246_640.jpg',5,4.0),(39,'Extra big Fish and chips',88.00,'Fries',NULL,NULL,'bigggggggggggggggggggggggggggggggggg','Big_Buger_city\\Products\\Extra_big_Fish_and_chips\\1249038.jpg',5,4.3),(40,'sale Fries',843.00,'Fries',NULL,NULL,'2435','Big_Buger_city\\Products\\sale_Fries\\3194309.jpg',5,4.3),(41,'Big bad nasty burger',9999.00,'Burger',NULL,NULL,'bad','12Food_shop\\Products\\Big_bad_nasty_burger\\2157483.jpg',1,3.3),(42,'Marinara',45.00,'Pizza',NULL,NULL,'da','Pizza_shop\\Products\\Marinara\\124815.jpg',2,4.1),(43,'Ribeyes',32.00,'Steak',NULL,NULL,'good food','Pizza_shop\\Products\\Ribeyes\\56409.jpg',2,4.1),(44,'Food',2.50,'Burger',NULL,NULL,'das','Pizza_shop\\Products\\Food\\418104.jpg',2,3.8),(45,'Bean shooter',250.00,'Salad',NULL,NULL,'awsome!','Crazy_Dave_shop\\Products\\Bean_shooter\\38dbb6fd5266d0166064d984952bd40735fa3518.jpg',9,4.4),(46,'Squash',50.00,'Salad',NULL,NULL,'zombie killer','Crazy_Dave_shop\\Products\\Squash\\t018807cbf4def0749d.jpg',9,4.2),(47,'Fried fish',56.00,'Fries',NULL,NULL,'da','12Food_shop\\Products\\Fried_fish_\\311469.jpg',1,4.6),(48,'A lot of dumplings',98.90,'Chinese food',NULL,NULL,'A lot!!!!!!!!!!!!!!!!!!!!!!!!!1','The_Mystery_Shop\\Products\\A_lot_of_dumplings\\34861.jpg',10,4.1),(49,'Delicious fried rice',17.90,'Chinese food',NULL,NULL,'Delicious and inexpensive fried rice','The_Mystery_Shop\\Products\\Delicious_fried_rice\\3881738.jpg',10,4.0),(50,'Healthy fried egg with fried rice',75.00,'Chinese food',NULL,NULL,'healthy!!!','Food_canteen\\Products\\Healthy_fried_egg_with_fried_rice\\355445.jpg',8,4.5),(51,'Big MAC pizza',99.90,'Pizza',NULL,NULL,'so bigggggggggg','Food_canteen\\Products\\Big_MAC_pizza\\335474.jpg',8,4.5),(52,'Cherry Bomb',50.00,'Salad',NULL,NULL,'bomb!','Crazy_Dave_shop\\Products\\Cherry_Bomb\\t013eb0e86d9ef992b2.jpg',9,4.4),(53,'club_sandwich',8.99,'Sandwich',NULL,NULL,'is that a sandwich?','The_Mystery_Shop\\Products\\club_sandwich\\120348.jpg',10,3.1),(54,'beef_tartare',15.20,'Steak',NULL,NULL,'really good beef tartare','The_Mystery_Shop\\Products\\beef_tartare\\164286.jpg',10,4.5),(55,'bad beef',699.00,'Steak',NULL,NULL,'das','Big_Buger_city\\Products\\bad_beef\\199682.jpg',5,4.3),(56,'Black rock salad',75.00,'Salad',NULL,NULL,'helathy and green','The_rock_official\\Products\\Black_rock_salad\\R-C.jfif',11,3.9),(57,'we love rock salad',333.30,'Salad',NULL,NULL,'you must love this rock!','The_rock_official\\Products\\we_love_rock_salad\\drc.jfif',11,3.9),(58,'random salad',66.50,'Salad',NULL,NULL,'randomly','The_rock_official\\Products\\random_salad\\15514258574374281.jpg',11,4.4),(59,'Crazy mac rib',45.90,'Steak',NULL,NULL,'carzy','Beef_home\\Products\\Crazy_mac_rib\\253653.jpg',12,4.4),(60,'rib and rib',785.00,'Steak',NULL,NULL,'good','Beef_home\\Products\\rib_and_rib\\2948125.jpg',12,4.4),(61,'pulled_pork_sandwich',88.00,'Pizza',NULL,NULL,'pulled_pork_sandwich','12Food_shop\\Products\\pulled_pork_sandwich\\16754.jpg',1,0.0),(62,'zhangxianzhong',86.00,'Chinese food',NULL,NULL,'what','Loopy_canteen_\\Products\\zhangxianzhong\\10B6A29F-545F-4503-A2DA-1355E58D52D2.jpeg',13,4.3),(63,'xiao chao rou',45.00,'Chinese food',NULL,NULL,'delicious ','Loopy_canteen_\\Products\\xiao_chao_rou\\CAFF8DC9-900C-474B-B058-354874E91FC9.jpeg',13,4.2),(64,'prime rib',199.00,'Steak',NULL,NULL,'prime','Chinese_food\\Products\\prime_rib\\126805.jpg',6,0.0),(65,'stir fried ho fun',35.00,'Chinese food',NULL,NULL,'stir fried ho fun','Chinese_food\\Products\\stir_fried_ho_fun\\94744.jpg',6,0.0),(66,'Big max fries',78.00,'Fries',NULL,NULL,'so big','2_fast\\Products\\Big_max_fries\\191085.jpg',7,0.0),(67,'MC fries',9.80,'Fries',NULL,NULL,'you will love it','Fries_home\\Products\\MC_fries\\106608.jpg',14,0.0),(68,'Frech fries',24.00,'Fries',NULL,NULL,'da','Fries_home\\Products\\Frech_fries\\267713.jpg',14,0.0);
/*!40000 ALTER TABLE `merchants_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `merchants_shoprating`
--

DROP TABLE IF EXISTS `merchants_shoprating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `merchants_shoprating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rate` decimal(3,1) NOT NULL,
  `shop_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `merchants_shoprating_shop_id_id_4bc2bdaa_uniq` (`shop_id`,`id`),
  CONSTRAINT `merchants_shoprating_shop_id_a4bddea6_fk_accounts_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `accounts_shop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchants_shoprating`
--

LOCK TABLES `merchants_shoprating` WRITE;
/*!40000 ALTER TABLE `merchants_shoprating` DISABLE KEYS */;
INSERT INTO `merchants_shoprating` VALUES (1,4.5,2),(2,4.2,6),(3,4.1,2),(4,4.2,4),(5,4.3,5),(6,4.5,2),(7,4.5,2),(8,4.5,2),(9,4.6,2),(10,4.1,6),(11,4.4,2),(12,4.7,2),(13,4.3,2),(14,4.6,2),(15,4.5,2),(16,4.2,5),(17,4.1,7),(18,4.7,2),(19,3.9,1),(20,4.3,7),(21,4.7,5),(22,3.9,2),(23,4.9,3),(24,4.4,1),(25,4.7,10),(26,4.5,5),(27,4.7,9),(28,3.9,8),(29,5.0,2),(30,4.4,9),(31,4.5,10),(32,3.8,6),(33,4.5,7),(34,4.3,4),(35,4.0,6),(36,4.2,9),(37,3.8,10),(38,4.3,4),(39,4.3,4),(40,4.6,5),(41,4.2,3),(42,4.7,6),(43,3.8,3),(44,4.1,11),(45,4.5,8),(46,3.8,3),(47,4.6,9),(48,4.1,7),(49,4.5,7),(50,4.4,5),(51,5.0,1),(52,4.1,1),(53,4.6,5),(54,4.0,10),(55,2.8,11),(56,4.0,8),(57,4.4,4),(58,3.9,2),(59,4.0,10),(60,3.0,2),(61,3.5,5),(62,4.1,12),(63,3.8,10),(64,4.6,12),(65,4.1,10),(66,4.0,5),(67,3.9,2),(68,4.8,12),(69,3.9,2),(70,4.6,8),(71,4.0,3),(72,3.5,11),(73,4.0,9),(74,4.6,8),(75,4.2,3),(76,4.1,6),(77,4.5,6),(78,4.5,10),(79,3.5,8),(80,4.0,7),(81,3.6,5),(82,3.9,2),(83,4.8,7),(84,4.2,9),(85,3.8,12),(86,4.0,11),(87,3.9,11),(88,4.5,5),(89,4.7,8),(90,4.6,5),(91,4.1,13),(92,4.1,12),(93,4.0,5),(94,3.0,6),(95,4.5,11),(96,4.2,8),(97,5.0,13),(98,4.2,8),(99,4.6,9),(100,4.6,11),(101,4.3,13),(102,4.6,11),(103,2.7,4),(104,3.6,6),(105,4.2,8),(106,4.5,7),(107,3.0,2),(108,3.3,6),(109,0.0,7),(110,4.5,6),(111,4.0,2),(112,4.4,4),(113,4.4,12),(114,3.8,5),(115,3.8,7),(116,4.7,10),(117,4.4,12),(118,4.5,2);
/*!40000 ALTER TABLE `merchants_shoprating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `merchant_id` int DEFAULT NULL,
  `product_price` decimal(10,2) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `sale_time` datetime DEFAULT NULL,
  `order_type` enum('delivery','pick up') DEFAULT NULL,
  `order_status` enum('Order finished','Order closed','Order in delivery','Wait for picked up') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_customer_id_orders` (`customer_id`),
  KEY `fk_merchant_id_orders` (`merchant_id`),
  KEY `fk_product_id_orders` (`product_id`),
  CONSTRAINT `fk_customer_id_orders` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `fk_merchant_id_orders` FOREIGN KEY (`merchant_id`) REFERENCES `merchants` (`id`),
  CONSTRAINT `fk_product_id_orders` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_order`
--

DROP TABLE IF EXISTS `orders_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total_price` decimal(10,2) NOT NULL,
  `sale_time` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  `merchant_id` bigint NOT NULL,
  `address_line` varchar(255) NOT NULL,
  `delivery_status` tinyint(1) NOT NULL,
  `payment_status` tinyint(1) NOT NULL,
  `shop_id` bigint DEFAULT NULL,
  `isComment` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_order_customer_id_0b76f6a4_fk_accounts_customer_id` (`customer_id`),
  KEY `orders_order_merchant_id_ab634f2d_fk_accounts_merchant_id` (`merchant_id`),
  KEY `orders_order_shop_id_b562fb3d_fk_accounts_shop_id` (`shop_id`),
  CONSTRAINT `orders_order_customer_id_0b76f6a4_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  CONSTRAINT `orders_order_merchant_id_ab634f2d_fk_accounts_merchant_id` FOREIGN KEY (`merchant_id`) REFERENCES `accounts_merchant` (`id`),
  CONSTRAINT `orders_order_shop_id_b562fb3d_fk_accounts_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `accounts_shop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order`
--

LOCK TABLES `orders_order` WRITE;
/*!40000 ALTER TABLE `orders_order` DISABLE KEYS */;
INSERT INTO `orders_order` VALUES (3,100.00,'2024-03-25 18:27:00.000000',1,1,'Test Address',1,1,1,0),(6,79.50,'2024-03-25 11:01:30.890297',1,2,'吉林省-长春市-南关区-fandou st',1,1,2,1),(7,11.00,'2024-03-25 11:01:30.890297',1,6,'吉林省-长春市-南关区-fandou st',1,1,6,1),(8,36.00,'2024-03-25 12:49:25.159933',1,6,'吉林省-长春市-南关区-fandou st',0,0,6,0),(9,25.60,'2024-03-25 12:56:44.735257',1,6,'吉林省-长春市-南关区-fandou st',0,0,6,0),(10,66.50,'2024-03-25 13:13:28.054132',1,2,'浙江省-温州市-鹿城区-whs ',0,0,2,0),(11,951.00,'2024-03-25 13:21:53.365914',1,5,'天津市-天津市-和平区-fandou st',0,0,5,0),(12,220.80,'2024-03-25 13:25:37.547441',1,7,'吉林省-长春市-南关区-fandou st',1,1,7,1),(13,98.50,'2024-03-25 13:35:15.983339',1,2,'浙江省-温州市-鹿城区-whs ',1,1,2,1),(14,66.90,'2024-03-25 13:41:29.854740',1,5,'浙江省-温州市-鹿城区-whs ',1,1,5,1),(15,127.60,'2024-03-25 13:50:29.467914',1,8,'浙江省-温州市-鹿城区-whs ',1,1,8,1),(16,444.00,'2024-03-25 13:50:48.801459',1,8,'天津市-天津市-和平区-fandou st',0,0,8,0),(17,180.70,'2024-03-26 13:40:02.835527',4,5,'山东省-济南市-长清区-sanzhong high school',1,1,5,1),(18,39996.00,'2024-03-26 13:40:02.835527',4,1,'山东省-济南市-长清区-sanzhong high school',1,1,1,1),(19,92.50,'2024-03-26 13:40:02.835527',4,2,'山东省-济南市-长清区-sanzhong high school',1,1,2,1),(20,5.90,'2024-03-26 13:40:02.835527',4,7,'山东省-济南市-长清区-sanzhong high school',1,1,7,1),(21,997.90,'2024-03-28 10:29:14.449237',2,5,'四川省-成都市-成华区-CDUT',1,1,5,1),(22,19998.00,'2024-03-28 10:29:42.698359',2,1,'四川省-成都市-成华区-CDUT',1,1,1,1),(23,64.00,'2024-03-28 10:29:56.110138',2,2,'四川省-成都市-成华区-CDUT',1,1,2,1),(24,47.50,'2024-03-28 10:30:09.153656',2,2,'四川省-成都市-成华区-CDUT',1,1,2,1),(25,180.00,'2024-03-28 10:30:21.257120',2,6,'四川省-成都市-成华区-CDUT',1,1,6,1),(26,84.00,'2024-03-28 10:31:33.566787',2,4,'四川省-成都市-成华区-CDUT',1,1,4,1),(27,17.50,'2024-03-28 10:31:44.594522',2,2,'四川省-成都市-成华区-CDUT',1,1,2,1),(28,47.50,'2024-03-29 03:14:57.691662',1,2,'浙江省-温州市-鹿城区-whs ',1,1,2,1),(29,150.00,'2024-03-29 03:14:57.691662',1,4,'浙江省-温州市-鹿城区-whs ',1,1,4,1),(30,550.00,'2024-03-31 11:50:50.379612',1,9,'浙江省-温州市-鹿城区-whs ',1,1,9,1),(31,53.70,'2024-03-31 11:52:28.461271',1,10,'天津市-天津市-和平区-fandou st',1,1,10,1),(32,82.00,'2024-03-31 12:13:45.056624',2,3,'四川省-成都市-成华区-longguang st.',1,1,3,1),(33,133.80,'2024-03-31 12:17:24.015887',1,5,'四川省-成都市-成华区-铁建',1,1,5,1),(34,68.80,'2024-03-31 12:48:57.857257',1,6,'浙江省-温州市-鹿城区-whs ',1,1,6,1),(35,60.80,'2024-03-31 12:48:57.857257',1,10,'浙江省-温州市-鹿城区-whs ',1,1,10,1),(36,400.00,'2024-03-31 12:49:27.549931',1,9,'浙江省-温州市-鹿城区-whs ',1,1,9,1),(37,112.80,'2024-03-31 12:49:52.296520',4,7,'江苏省-南京市-玄武区-hahha',1,1,7,1),(38,300.00,'2024-03-31 12:49:52.296520',4,9,'江苏省-南京市-玄武区-hahha',1,1,9,1),(39,16.00,'2024-03-31 12:50:26.351219',4,3,'山东省-济南市-长清区-sanzhong high school',1,1,3,1),(40,388.50,'2024-03-31 12:50:26.351219',4,8,'山东省-济南市-长清区-sanzhong high school',1,1,8,1),(41,200.00,'2024-03-31 12:50:47.908900',2,9,'四川省-成都市-成华区-CDUT',1,1,9,1),(42,54.59,'2024-03-31 12:50:57.679477',2,10,'四川省-成都市-成华区-CDUT',1,1,10,1),(43,14.70,'2024-03-31 12:52:17.915115',6,7,'贵州省-六盘水市-六枝特区-where',1,1,7,1),(44,68.80,'2024-03-31 12:52:17.915115',6,6,'贵州省-六盘水市-六枝特区-where',1,1,6,1),(45,215.00,'2024-03-31 12:52:35.853465',6,4,'贵州省-六盘水市-六枝特区-where',1,1,4,1),(46,1398.00,'2024-03-31 12:55:01.402902',7,5,'浙江省-台州市-路桥区-school',1,1,5,1),(47,32.00,'2024-03-31 12:55:01.402902',7,2,'浙江省-台州市-路桥区-school',1,1,2,1),(48,188.00,'2024-03-31 12:55:01.402902',7,4,'浙江省-台州市-路桥区-school',1,1,4,1),(49,332.50,'2024-03-31 13:09:30.067752',2,11,'四川省-成都市-成华区-longguang st.',1,1,11,1),(50,74.00,'2024-03-31 13:09:49.102297',2,3,'四川省-成都市-成华区-CDUT',1,1,3,1),(51,74.80,'2024-03-31 13:10:15.757272',2,6,'四川省-成都市-成华区-longguang st.',1,1,6,1),(52,40.00,'2024-03-31 16:57:00.494876',1,3,'四川省-成都市-成华区-铁建',1,1,3,1),(53,830.90,'2024-03-31 16:58:01.280438',7,12,'浙江省-台州市-路桥区-school',1,1,12,1),(54,474.80,'2024-04-01 03:58:04.347362',1,11,'浙江省-温州市-鹿城区-whs ',1,1,11,1),(55,2143.90,'2024-04-01 03:58:18.738530',1,5,'吉林省-长春市-南关区-fandou st',1,1,5,1),(56,931.00,'2024-04-01 03:58:28.416578',1,5,'四川省-成都市-成华区-铁建',1,1,5,1),(57,177.50,'2024-04-01 04:00:38.339298',1,8,'天津市-天津市-和平区-fandou st',1,1,8,1),(58,314.60,'2024-04-01 04:01:05.013880',6,10,'贵州省-六盘水市-六枝特区-where',1,1,10,1),(59,47.00,'2024-04-01 04:01:19.078434',6,6,'贵州省-六盘水市-六枝特区-where',1,1,6,1),(60,25.60,'2024-04-01 04:01:30.257685',6,6,'贵州省-六盘水市-六枝特区-where',1,1,6,1),(61,148.00,'2024-04-01 04:01:59.562680',6,3,'贵州省-六盘水市-六枝特区-where',1,1,3,1),(62,300.00,'2024-04-01 04:02:14.916371',6,8,'贵州省-六盘水市-六枝特区-where',1,1,8,1),(63,86.90,'2024-04-01 04:03:06.322396',2,5,'四川省-成都市-成华区-longguang st.',1,1,5,0),(64,17.98,'2024-04-01 04:04:04.772289',2,10,'四川省-成都市-成华区-longguang st.',1,1,10,0),(65,50.00,'2024-04-01 04:04:20.953398',2,2,'四川省-成都市-成华区-longguang st.',1,1,2,0),(66,96.00,'2024-04-01 04:04:42.432402',7,2,'浙江省-台州市-路桥区-school',1,1,2,1),(67,787.00,'2024-04-01 04:04:53.074754',7,5,'浙江省-台州市-路桥区-school',1,1,5,1),(68,54.59,'2024-04-01 04:05:10.487109',7,10,'浙江省-台州市-路桥区-school',1,1,10,1),(69,350.00,'2024-04-01 04:06:20.926677',8,9,'青海省-西宁市-城中区-carzy',1,1,9,0),(70,8.99,'2024-04-01 04:11:06.116017',8,10,'青海省-西宁市-城中区-carzy',1,1,10,0),(71,352.50,'2024-04-01 04:11:06.116017',8,8,'青海省-西宁市-城中区-carzy',1,1,8,0),(72,33.00,'2024-04-01 04:12:14.460369',8,3,'青海省-西宁市-城中区-carzy',1,1,3,0),(73,220.80,'2024-04-01 04:12:14.460369',8,7,'青海省-西宁市-城中区-carzy',1,1,7,0),(74,38.00,'2024-04-01 04:12:14.460369',8,6,'青海省-西宁市-城中区-carzy',1,1,6,0),(75,300.00,'2024-04-01 04:12:31.400964',8,9,'青海省-西宁市-城中区-carzy',1,1,9,0),(76,124.20,'2024-04-01 04:31:39.393738',4,7,'辽宁省-大连市-瓦房店市-dog shop',1,1,7,1),(77,42.17,'2024-04-01 04:31:39.393738',4,10,'辽宁省-大连市-瓦房店市-dog shop',1,1,10,1),(78,167.00,'2024-04-01 04:33:32.646121',4,2,'北京市-北京市-朝阳区-jianshe road',1,1,2,1),(79,165.00,'2024-04-01 04:33:32.646121',4,4,'北京市-北京市-朝阳区-jianshe road',1,1,4,1),(80,117.00,'2024-04-01 04:33:32.646121',4,8,'北京市-北京市-朝阳区-jianshe road',1,1,8,1),(81,408.30,'2024-04-01 04:33:57.222985',4,11,'北京市-北京市-朝阳区-jianshe road',1,1,11,1),(82,51.16,'2024-04-01 04:34:22.842819',4,10,'辽宁省-大连市-瓦房店市-dog shop',1,1,10,1),(83,1195.00,'2024-04-01 04:34:22.842819',4,5,'辽宁省-大连市-瓦房店市-dog shop',1,1,5,1),(84,10223.00,'2024-04-01 04:35:04.927319',4,1,'山东省-济南市-长清区-sanzhong high school',1,1,1,1),(85,951.00,'2024-04-01 04:35:04.927319',4,5,'山东省-济南市-长清区-sanzhong high school',1,1,5,1),(86,154.90,'2024-04-01 04:42:14.866098',4,5,'辽宁省-大连市-瓦房店市-dog shop',1,1,5,1),(87,5.00,'2024-04-01 04:42:14.866098',4,2,'辽宁省-大连市-瓦房店市-dog shop',1,1,2,1),(88,876.80,'2024-04-01 04:42:14.866098',4,12,'辽宁省-大连市-瓦房店市-dog shop',1,1,12,1),(89,922.70,'2024-04-01 04:44:33.182702',7,12,'浙江省-台州市-路桥区-school',1,1,12,1),(90,39.39,'2024-04-01 04:44:33.182702',7,10,'浙江省-台州市-路桥区-school',1,1,10,1),(91,474.80,'2024-04-01 04:47:48.575643',7,11,'浙江省-台州市-路桥区-school',1,1,11,1),(92,74.00,'2024-04-01 04:47:48.575643',7,3,'浙江省-台州市-路桥区-school',1,1,3,1),(93,138.70,'2024-04-01 04:47:48.575643',7,8,'浙江省-台州市-路桥区-school',1,1,8,1),(94,400.00,'2024-04-01 04:49:12.993708',7,9,'浙江省-台州市-路桥区-school',1,1,9,1),(95,212.00,'2024-04-01 04:51:47.113813',6,2,'贵州省-六盘水市-六枝特区-where',1,1,2,1),(96,60.00,'2024-04-01 04:51:47.113813',6,5,'贵州省-六盘水市-六枝特区-where',1,1,5,1),(97,89.00,'2024-04-01 04:51:47.113813',6,7,'贵州省-六盘水市-六枝特区-where',1,1,7,1),(98,77.60,'2024-04-01 04:51:47.113813',6,8,'贵州省-六盘水市-六枝特区-where',1,1,8,1),(99,600.00,'2024-04-01 04:53:53.657939',6,9,'贵州省-六盘水市-六枝特区-where',1,1,9,1),(100,225.60,'2024-04-01 04:53:53.657939',6,7,'贵州省-六盘水市-六枝特区-where',1,1,7,1),(101,808.10,'2024-04-01 04:55:23.823554',6,11,'贵州省-六盘水市-六枝特区-where',1,1,11,1),(102,830.90,'2024-04-01 04:55:33.432122',6,12,'贵州省-六盘水市-六枝特区-where',1,1,12,1),(103,47.00,'2024-04-07 14:10:33.959682',9,6,'天津市-天津市-西青区-da st.',1,1,6,1),(104,303.00,'2024-04-07 14:11:04.409786',9,13,'天津市-天津市-西青区-da st.',1,1,13,1),(105,830.90,'2024-04-07 14:11:04.409786',9,12,'天津市-天津市-西青区-da st.',1,1,12,1),(106,765.90,'2024-04-07 14:11:37.756624',9,5,'天津市-天津市-西青区-da st.',1,1,5,1),(107,1465.40,'2024-04-09 07:23:54.294764',9,11,'天津市-天津市-西青区-da st.',1,1,11,1),(108,227.50,'2024-04-09 07:24:21.963204',9,8,'天津市-天津市-西青区-da st.',1,1,8,1),(109,262.00,'2024-04-09 07:33:21.870656',9,13,'天津市-天津市-西青区-da st.',1,1,13,1),(110,416.00,'2024-04-09 07:33:21.870656',9,11,'天津市-天津市-西青区-da st.',1,1,11,1),(111,799.60,'2024-04-09 07:34:39.087451',9,11,'天津市-天津市-西青区-da st.',1,1,11,1),(112,450.00,'2024-04-09 07:34:39.087451',9,9,'天津市-天津市-西青区-da st.',1,1,9,1),(113,444.00,'2024-04-09 07:36:00.843763',9,8,'内蒙古自治区-呼和浩特市-回民区-hui',1,1,8,1),(114,262.00,'2024-04-09 07:36:00.843763',9,13,'内蒙古自治区-呼和浩特市-回民区-hui',1,1,13,1),(115,165.00,'2024-04-09 07:38:25.446479',9,6,'内蒙古自治区-呼和浩特市-回民区-hui',1,1,6,1),(116,150.00,'2024-04-09 07:38:25.446479',9,4,'内蒙古自治区-呼和浩特市-回民区-hui',1,1,4,1),(117,361.20,'2024-04-09 07:40:23.972266',9,7,'天津市-天津市-西青区-da st.',1,1,7,1),(118,177.60,'2024-04-09 07:40:23.972266',9,8,'天津市-天津市-西青区-da st.',1,1,8,1),(119,92.00,'2024-04-09 07:55:43.626325',9,6,'内蒙古自治区-呼和浩特市-回民区-hui',1,1,6,1),(120,173.00,'2024-04-09 07:55:43.626325',9,2,'内蒙古自治区-呼和浩特市-回民区-hui',1,1,2,1),(121,89.00,'2024-04-09 08:20:49.892084',10,7,'山西省-大同市-云冈区-大同大学',1,1,7,1),(122,47.00,'2024-04-09 09:09:55.115905',12,6,'四川省-泸州市-江阳区-damn',1,1,6,1),(123,1707.70,'2024-04-09 09:17:35.033106',7,12,'浙江省-台州市-路桥区-school',1,1,12,1),(124,537.00,'2024-04-09 09:17:35.033106',7,4,'浙江省-台州市-路桥区-school',1,1,4,1),(125,111.50,'2024-04-09 09:17:49.285407',7,2,'浙江省-台州市-路桥区-school',1,1,2,1),(126,3323.60,'2024-04-09 09:20:35.207396',7,12,'浙江省-台州市-路桥区-school',1,1,12,1),(127,51.08,'2024-04-09 09:20:35.207396',7,10,'浙江省-台州市-路桥区-school',1,1,10,1),(128,11.80,'2024-04-09 09:21:05.139047',7,7,'浙江省-台州市-路桥区-school',1,1,7,1),(129,1686.00,'2024-04-09 09:21:05.139047',7,5,'浙江省-台州市-路桥区-school',1,1,5,1),(130,135.00,'2024-04-09 09:24:07.412345',7,2,'浙江省-台州市-路桥区-school',1,1,2,1);
/*!40000 ALTER TABLE `orders_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_orderitem`
--

DROP TABLE IF EXISTS `orders_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` (`order_id`),
  KEY `orders_orderitem_product_id_afe4254a_fk_merchants_product_id` (`product_id`),
  CONSTRAINT `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  CONSTRAINT `orders_orderitem_product_id_afe4254a_fk_merchants_product_id` FOREIGN KEY (`product_id`) REFERENCES `merchants_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_orderitem`
--

LOCK TABLES `orders_orderitem` WRITE;
/*!40000 ALTER TABLE `orders_orderitem` DISABLE KEYS */;
INSERT INTO `orders_orderitem` VALUES (1,45.00,1,6,42),(2,2.50,1,6,44),(3,32.00,1,6,43),(4,11.00,1,7,9),(5,18.00,2,8,11),(6,12.80,2,9,8),(7,32.00,2,10,43),(8,2.50,1,10,44),(9,20.00,1,11,38),(10,88.00,1,11,39),(11,843.00,1,11,40),(12,99.00,1,12,16),(13,13.80,1,12,17),(14,108.00,1,12,18),(15,32.00,3,13,43),(16,2.50,1,13,44),(17,46.90,1,14,37),(18,20.00,1,14,38),(19,38.80,1,15,21),(20,88.80,1,15,22),(21,88.80,5,16,22),(22,46.90,3,17,37),(23,20.00,2,17,38),(24,9999.00,4,18,41),(25,45.00,2,19,42),(26,2.50,1,19,44),(27,5.90,1,20,15),(28,46.90,1,21,37),(29,20.00,1,21,38),(30,88.00,1,21,39),(31,843.00,1,21,40),(32,9999.00,2,22,41),(33,32.00,2,23,43),(34,2.50,1,24,44),(35,45.00,1,24,42),(36,18.00,10,25,11),(37,34.00,1,26,35),(38,50.00,1,26,33),(39,2.50,7,27,44),(40,45.00,1,28,42),(41,2.50,1,28,44),(42,50.00,1,29,33),(43,66.00,1,29,32),(44,34.00,1,29,35),(45,250.00,2,30,45),(46,50.00,1,30,46),(47,17.90,3,31,49),(48,8.00,1,32,31),(49,42.00,1,32,30),(50,32.00,1,32,29),(51,46.90,2,33,37),(52,20.00,2,33,38),(53,18.00,1,34,11),(54,38.00,1,34,10),(55,12.80,1,34,8),(56,15.20,4,35,54),(57,50.00,3,36,52),(58,250.00,1,36,45),(59,13.80,1,37,17),(60,99.00,1,37,16),(61,250.00,1,38,45),(62,50.00,1,38,52),(63,8.00,2,39,31),(64,88.80,1,40,22),(65,99.90,3,40,51),(66,50.00,3,41,52),(67,50.00,1,41,46),(68,15.20,3,42,54),(69,8.99,1,42,53),(70,8.80,1,43,19),(71,5.90,1,43,15),(72,12.80,1,44,8),(73,38.00,1,44,10),(74,18.00,1,44,11),(75,99.00,1,45,36),(76,50.00,1,45,33),(77,66.00,1,45,32),(78,699.00,2,46,55),(79,32.00,1,47,43),(80,66.00,1,48,32),(81,50.00,1,48,33),(82,72.00,1,48,34),(83,66.50,5,49,58),(84,32.00,1,50,29),(85,42.00,1,50,30),(86,18.00,1,51,11),(87,12.80,1,51,8),(88,22.00,2,51,12),(89,8.00,1,52,31),(90,32.00,1,52,29),(91,785.00,1,53,60),(92,45.90,1,53,59),(93,75.00,1,54,56),(94,333.30,1,54,57),(95,66.50,1,54,58),(96,699.00,3,55,55),(97,46.90,1,55,37),(98,843.00,1,56,40),(99,88.00,1,56,39),(100,99.90,1,57,51),(101,38.80,2,57,21),(102,98.90,3,58,48),(103,17.90,1,58,49),(104,18.00,2,59,11),(105,11.00,1,59,9),(106,12.80,2,60,8),(107,42.00,2,61,30),(108,32.00,2,61,29),(109,75.00,4,62,50),(110,20.00,2,63,38),(111,46.90,1,63,37),(112,8.99,2,64,53),(113,2.50,2,65,44),(114,45.00,1,65,42),(115,32.00,3,66,43),(116,88.00,1,67,39),(117,699.00,1,67,55),(118,15.20,3,68,54),(119,8.99,1,68,53),(120,250.00,1,69,45),(121,50.00,1,69,46),(122,50.00,1,69,52),(123,8.99,1,70,53),(124,88.80,2,71,22),(125,99.90,1,71,51),(126,75.00,1,71,50),(127,8.00,1,72,31),(128,25.00,1,72,28),(129,99.00,1,73,16),(130,13.80,1,73,17),(131,108.00,1,73,18),(132,38.00,1,74,10),(133,250.00,1,75,45),(134,50.00,1,75,52),(135,8.80,4,76,19),(136,89.00,1,76,13),(137,8.99,3,77,53),(138,15.20,1,77,54),(139,45.00,3,78,42),(140,32.00,1,78,43),(141,99.00,1,79,36),(142,66.00,1,79,32),(143,75.00,1,80,50),(144,42.00,1,80,20),(145,333.30,1,81,57),(146,75.00,1,81,56),(147,15.20,1,82,54),(148,8.99,4,82,53),(149,843.00,1,83,40),(150,88.00,4,83,39),(151,56.00,4,84,47),(152,9999.00,1,84,41),(153,88.00,1,85,39),(154,843.00,1,85,40),(155,20.00,1,85,38),(156,20.00,1,86,38),(157,46.90,1,86,37),(158,88.00,1,86,39),(159,2.50,2,87,44),(160,45.90,2,88,59),(161,785.00,1,88,60),(162,45.90,3,89,59),(163,785.00,1,89,60),(164,15.20,2,90,54),(165,8.99,1,90,53),(166,75.00,1,91,56),(167,333.30,1,91,57),(168,66.50,1,91,58),(169,42.00,1,92,30),(170,32.00,1,92,29),(171,38.80,1,93,21),(172,99.90,1,93,51),(173,250.00,1,94,45),(174,50.00,1,94,46),(175,50.00,2,94,52),(176,45.00,4,95,42),(177,32.00,1,95,43),(178,20.00,3,96,38),(179,89.00,1,97,13),(180,38.80,2,98,21),(181,50.00,1,99,46),(182,250.00,2,99,45),(183,50.00,1,99,52),(184,13.80,2,100,17),(185,99.00,2,100,16),(186,75.00,1,101,56),(187,333.30,2,101,57),(188,66.50,1,101,58),(189,45.90,1,102,59),(190,785.00,1,102,60),(191,18.00,2,103,11),(192,11.00,1,103,9),(193,86.00,3,104,62),(194,45.00,1,104,63),(195,785.00,1,105,60),(196,45.90,1,105,59),(197,46.90,1,106,37),(198,20.00,1,106,38),(199,699.00,1,106,55),(200,66.50,7,107,58),(201,333.30,3,107,57),(202,99.90,1,108,51),(203,38.80,1,108,21),(204,88.80,1,108,22),(205,86.00,2,109,62),(206,45.00,2,109,63),(207,66.50,4,110,58),(208,75.00,2,110,56),(209,333.30,2,111,57),(210,66.50,2,111,58),(211,50.00,4,112,52),(212,250.00,1,112,45),(213,88.80,5,113,22),(214,86.00,2,114,62),(215,45.00,2,114,63),(216,18.00,1,115,11),(217,38.00,3,115,10),(218,11.00,1,115,9),(219,22.00,1,115,12),(220,34.00,1,116,35),(221,66.00,1,116,32),(222,50.00,1,116,33),(223,99.00,2,117,16),(224,13.80,4,117,17),(225,108.00,1,117,18),(226,88.80,2,118,22),(227,18.00,3,119,11),(228,38.00,1,119,10),(229,32.00,4,120,43),(230,45.00,1,120,42),(231,89.00,1,121,13),(232,18.00,2,122,11),(233,11.00,1,122,9),(234,45.90,3,123,59),(235,785.00,2,123,60),(236,66.00,2,124,32),(237,50.00,4,124,33),(238,72.00,1,124,34),(239,34.00,1,124,35),(240,99.00,1,124,36),(241,32.00,2,125,43),(242,45.00,1,125,42),(243,2.50,1,125,44),(244,45.90,4,126,59),(245,785.00,4,126,60),(246,8.99,2,127,53),(247,15.20,1,127,54),(248,17.90,1,127,49),(249,5.90,2,128,15),(250,843.00,2,129,40),(251,45.00,3,130,42);
/*!40000 ALTER TABLE `orders_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `shop_id` int DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `discount_price` decimal(10,2) DEFAULT NULL,
  `discount_time` datetime DEFAULT NULL,
  `description` text,
  `image_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_shop_id_products` (`shop_id`),
  CONSTRAINT `fk_shop_id_products` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoppingcarts`
--

DROP TABLE IF EXISTS `shoppingcarts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoppingcarts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_customer_id_carts` (`customer_id`),
  CONSTRAINT `fk_customer_id_carts` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `shoppingcarts_chk_1` CHECK ((`quantity` <= 100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppingcarts`
--

LOCK TABLES `shoppingcarts` WRITE;
/*!40000 ALTER TABLE `shoppingcarts` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoppingcarts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopratings`
--

DROP TABLE IF EXISTS `shopratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopratings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `shop_id` int DEFAULT NULL,
  `average_rating` decimal(3,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_shop_id_ratings` (`shop_id`),
  CONSTRAINT `fk_shop_id_ratings` FOREIGN KEY (`shop_id`) REFERENCES `shops` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopratings`
--

LOCK TABLES `shopratings` WRITE;
/*!40000 ALTER TABLE `shopratings` DISABLE KEYS */;
/*!40000 ALTER TABLE `shopratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shops`
--

DROP TABLE IF EXISTS `shops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shops` (
  `id` int NOT NULL AUTO_INCREMENT,
  `merchant_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `total_rating` decimal(3,1) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_merchant_id_shops` (`merchant_id`),
  CONSTRAINT `fk_merchant_id_shops` FOREIGN KEY (`merchant_id`) REFERENCES `merchants` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shops`
--

LOCK TABLES `shops` WRITE;
/*!40000 ALTER TABLE `shops` DISABLE KEYS */;
/*!40000 ALTER TABLE `shops` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-11 16:30:43
