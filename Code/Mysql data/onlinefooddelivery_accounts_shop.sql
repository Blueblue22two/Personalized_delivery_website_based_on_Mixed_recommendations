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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_shop`
--

LOCK TABLES `accounts_shop` WRITE;
/*!40000 ALTER TABLE `accounts_shop` DISABLE KEYS */;
INSERT INTO `accounts_shop` VALUES (1,'12Food_shop','四川省-成都市-武侯区-52 st',4.2,'12Food_shop\\LOGO\\baozou.png',1,'成都市','52 st','武侯区','四川省'),(2,'Pizza_shop','四川省-成都市-成华区-erxian bridge',4.3,'Pizza_shop\\LOGO\\22489.jpg',2,'成都市','erxian bridge','成华区','四川省'),(3,'Dumpling_store','四川省-成都市-金牛区-haha st',4.1,'Dumpling_store\\LOGO\\62969.jpg',3,'成都市','haha st','金牛区','四川省'),(4,'Beef_store','四川省-成都市-高新区-haha st',4.0,'Beef_store\\LOGO\\118395.jpg',4,'成都市','haha st','高新区','四川省'),(5,'Big_Buger_city','四川省-成都市-金牛区-jianshe road',4.0,'Big_Buger_city\\LOGO\\hamburger-1238246_640.jpg',5,'成都市','jinshan road','金牛区','四川省'),(6,'Chinese_food','四川省-成都市-成华区-erxian bridge',3.8,'Chinese_food\\LOGO\\3046wh300.jpg',6,'成都市','erxian bridge','成华区','四川省'),(7,'2 fast','四川省-成都市-成华区-CDUT',3.9,'2_fast\\LOGO\\1188.jpg_wh300.jpg',7,'成都市','CDUT','成华区','四川省'),(8,'Food canteen','四川省-宜宾市-叙州区-55 st',4.3,'Food_canteen\\LOGO\\109357.jpg',8,'宜宾市','55 st','叙州区','四川省'),(9,'Crazy_Dave_shop','四川省-宜宾市-屏山县-junshan road',4.4,'Crazy_Dave_shop\\LOGO\\img.png',9,'宜宾市','junshan road','屏山县','四川省'),(10,'The Mystery Shop','四川省-乐山市-沐川县-have a guess',4.1,'The_Mystery_Shop\\LOGO\\58582c1cf034562c58220600.png',10,'乐山市','have a guess','沐川县','四川省'),(11,'The rock official','上海市-上海市-黄浦区-Rock st.',3.9,'The_rock_official\\LOGO\\R-C.jfif',11,'上海市','Rock st.','黄浦区','上海市'),(12,'Beef home','吉林省-长春市-宽城区-cow st.',4.3,'Beef_home\\LOGO\\677746.jpg',12,'长春市','cow st.','宽城区','吉林省'),(13,'Loopy canteen ','重庆市-重庆市-城口县-hongya ',4.5,'Loopy_canteen_\\LOGO\\CC1774B4-6AFE-4B78-955A-EA6ED22597D0.jpeg',13,'重庆市','hongya ','城口县','重庆市'),(14,'Fries home','四川省-泸州市-合江县-idk',4.0,'Fries_home\\LOGO\\106608.jpg',14,'泸州市','idk','合江县','四川省'),(15,'Test_shop1','吉林省-长春市-宽城区-idk st.',0.0,'Test_product1\\LOGO\\25564.jpg',15,'长春市','idk st.','宽城区','吉林省');
/*!40000 ALTER TABLE `accounts_shop` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 18:27:47
