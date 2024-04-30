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
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchants_product`
--

LOCK TABLES `merchants_product` WRITE;
/*!40000 ALTER TABLE `merchants_product` DISABLE KEYS */;
INSERT INTO `merchants_product` VALUES (8,'shrimp dumpling',12.80,'Chinese food',NULL,NULL,'good','Chinese_food\\Products\\shrimp_dumpling\\325914.jpg',6,4.0),(9,'Chive and pork dumplings',11.00,'Chinese food',NULL,NULL,'dafa','Chinese_food\\Products\\Chive_and_pork_dumplings\\3890813.jpg',6,3.9),(10,'Dumplings with crab roe',38.00,'Chinese food',NULL,NULL,'dada','Chinese_food\\Products\\Dumplings_with_crab_roe\\593.jpg',6,3.7),(11,'egg fried rice',18.00,'Chinese food',NULL,NULL,'really good','Chinese_food\\Products\\egg_fried_rice\\108226.jpg',6,3.8),(12,'fried rice with shredded meat',22.00,'Chinese food',NULL,NULL,'yummyyyyyyyyyyy','Chinese_food\\Products\\fried_rice_with_shredded_meat\\1391.jpg',6,3.9),(13,'Extra super big burger',89.00,'Burger',NULL,NULL,'so big!!!','2_fast\\Products\\Extra_super_big_burger\\83196.jpg',7,3.4),(15,'Extra small fish and chips',5.90,'Fries',NULL,NULL,'small','2_fast\\Products\\Extra_small_fish_and_chips\\403380.jpg',7,3.7),(16,'Healthy greek salad',99.00,'Salad',NULL,NULL,'?','2_fast\\Products\\Healthy_greek_salad\\23497.jpg',7,4.4),(17,'Seaweed salad',13.80,'Salad',NULL,NULL,'sae','2_fast\\Products\\Seaweed_salad\\2978247.jpg',7,4.3),(18,'beet salad',108.00,'Salad',NULL,NULL,'expensive','2_fast\\Products\\beet_salad\\173220.jpg',7,4.0),(19,'Fish and chips',8.80,'Fries',NULL,NULL,'da','2_fast\\Products\\Fish_and_chips\\4128.jpg',7,4.1),(20,'Shrimp rice',42.00,'Chinese food',NULL,NULL,'f','Food_canteen\\Products\\Shrimp_rice\\116708.jpg',8,4.5),(21,'Italian pizza',38.80,'Pizza',NULL,NULL,'good','Food_canteen\\Products\\Italian_pizza\\144631.jpg',8,4.4),(22,'Caser salad',88.80,'Salad',NULL,NULL,'da','Food_canteen\\Products\\Caser_salad\\242466.jpg',8,4.3),(28,'Large dumplings stuffed with chives',25.00,'Chinese food',NULL,NULL,'da','Dumpling_store\\Products\\Large_dumplings_stuffed_with_chives\\3890813.jpg',3,3.7),(29,'Extra Large dumplings stuffed with chives',32.00,'Chinese food',NULL,NULL,'too much','Dumpling_store\\Products\\Extra_Large_dumplings_stuffed_with_chives\\3890813.jpg',3,4.3),(30,'Crab Dumplings in Soup',42.00,'Chinese food',NULL,NULL,'yummy yummy','Dumpling_store\\Products\\Crab_Dumplings_in_Soup\\15535.jpg',3,4.2),(31,'It is just a salad',8.00,'Salad',NULL,NULL,'?','Dumpling_store\\Products\\It_is_just_a_salad\\387912.jpg',3,4.1),(32,'ribeye steak',66.00,'Steak',NULL,NULL,'heLLL','Beef_store\\Products\\ribeye_steak\\66183.jpg',4,4.5),(33,'Spicy ribs',50.00,'Steak',NULL,NULL,'12134568','Beef_store\\Products\\Spicy_ribs\\37492.jpg',4,4.6),(34,'filet steak',72.00,'Steak',NULL,NULL,'46653','Beef_store\\Products\\filet_steak\\168551.jpg',4,4.2),(35,'fried rice',34.00,'Chinese food',NULL,NULL,'555','Beef_store\\Products\\fried_rice\\320052.jpg',4,4.2),(36,'MC fish and chips',99.00,'Fries',NULL,NULL,'goddd','Beef_store\\Products\\MC_fish_and_chips\\186030.jpg',4,4.0),(37,'Spicy hell burger package',46.90,'Burger',NULL,NULL,'dm','Big_Buger_city\\Products\\Spicy_hell_burger_package\\2316148.jpg',5,3.9),(38,'Beef sandwich',20.00,'Sandwich',NULL,NULL,'beefff','Big_Buger_city\\Products\\Beef_sandwich\\hamburger-1238246_640.jpg',5,4.0),(39,'Extra big Fish and chips',88.00,'Fries',NULL,NULL,'bigggggggggggggggggggggggggggggggggg','Big_Buger_city\\Products\\Extra_big_Fish_and_chips\\1249038.jpg',5,4.1),(40,'sale Fries',843.00,'Fries',NULL,NULL,'2435','Big_Buger_city\\Products\\sale_Fries\\3194309.jpg',5,4.1),(41,'Big bad nasty burger',9999.00,'Burger',NULL,NULL,'bad','12Food_shop\\Products\\Big_bad_nasty_burger\\2157483.jpg',1,3.7),(42,'Marinara',45.00,'Pizza',NULL,NULL,'da','Pizza_shop\\Products\\Marinara\\124815.jpg',2,4.3),(43,'Ribeyes',32.00,'Steak',NULL,NULL,'good food','Pizza_shop\\Products\\Ribeyes\\56409.jpg',2,4.1),(44,'Food',2.50,'Burger',NULL,NULL,'das','Pizza_shop\\Products\\Food\\418104.jpg',2,3.8),(45,'Bean shooter',250.00,'Salad',NULL,NULL,'awsome!','Crazy_Dave_shop\\Products\\Bean_shooter\\38dbb6fd5266d0166064d984952bd40735fa3518.jpg',9,4.5),(46,'Squash',50.00,'Salad',NULL,NULL,'zombie killer','Crazy_Dave_shop\\Products\\Squash\\t018807cbf4def0749d.jpg',9,4.3),(47,'Fried fish',56.00,'Fries',NULL,NULL,'da','12Food_shop\\Products\\Fried_fish_\\311469.jpg',1,4.0),(48,'A lot of dumplings',98.90,'Chinese food',NULL,NULL,'A lot!!!!!!!!!!!!!!!!!!!!!!!!!1','The_Mystery_Shop\\Products\\A_lot_of_dumplings\\34861.jpg',10,3.8),(49,'Delicious fried rice',17.90,'Chinese food',NULL,NULL,'Delicious and inexpensive fried rice','The_Mystery_Shop\\Products\\Delicious_fried_rice\\3881738.jpg',10,4.1),(50,'Healthy fried egg with fried rice',75.00,'Chinese food',NULL,NULL,'healthy!!!','Food_canteen\\Products\\Healthy_fried_egg_with_fried_rice\\355445.jpg',8,4.2),(51,'Big MAC pizza',99.90,'Pizza',NULL,NULL,'so bigggggggggg','Food_canteen\\Products\\Big_MAC_pizza\\335474.jpg',8,4.4),(52,'Cherry Bomb',50.00,'Salad',NULL,NULL,'bomb!','Crazy_Dave_shop\\Products\\Cherry_Bomb\\t013eb0e86d9ef992b2.jpg',9,4.5),(53,'club_sandwich',8.99,'Sandwich',NULL,NULL,'is that a sandwich?','The_Mystery_Shop\\Products\\club_sandwich\\120348.jpg',10,3.5),(54,'beef_tartare',15.20,'Steak',NULL,NULL,'really good beef tartare','The_Mystery_Shop\\Products\\beef_tartare\\164286.jpg',10,4.2),(55,'bad beef',699.00,'Steak',NULL,NULL,'das','Big_Buger_city\\Products\\bad_beef\\199682.jpg',5,4.0),(56,'Black rock salad',75.00,'Salad',NULL,NULL,'helathy and green','The_rock_official\\Products\\Black_rock_salad\\R-C.jfif',11,3.8),(57,'we love rock salad',333.30,'Salad',NULL,NULL,'you must love this rock!','The_rock_official\\Products\\we_love_rock_salad\\drc.jfif',11,3.8),(58,'random salad',66.50,'Salad',NULL,NULL,'randomly','The_rock_official\\Products\\random_salad\\15514258574374281.jpg',11,4.2),(59,'Crazy mac rib',45.90,'Steak',NULL,NULL,'carzy','Beef_home\\Products\\Crazy_mac_rib\\253653.jpg',12,4.4),(60,'rib and rib',785.00,'Steak',NULL,NULL,'good','Beef_home\\Products\\rib_and_rib\\2948125.jpg',12,4.4),(61,'pulled_pork_sandwich',88.00,'Pizza',NULL,NULL,'pulled_pork_sandwich','12Food_shop\\Products\\pulled_pork_sandwich\\16754.jpg',1,4.7),(62,'zhangxianzhong',86.00,'Chinese food',NULL,NULL,'what','Loopy_canteen_\\Products\\zhangxianzhong\\10B6A29F-545F-4503-A2DA-1355E58D52D2.jpeg',13,4.5),(63,'xiao chao rou',45.00,'Chinese food',NULL,NULL,'delicious ','Loopy_canteen_\\Products\\xiao_chao_rou\\CAFF8DC9-900C-474B-B058-354874E91FC9.jpeg',13,4.4),(64,'prime rib',199.00,'Steak',NULL,NULL,'prime','Chinese_food\\Products\\prime_rib\\126805.jpg',6,3.9),(65,'stir fried ho fun',35.00,'Chinese food',NULL,NULL,'stir fried ho fun','Chinese_food\\Products\\stir_fried_ho_fun\\94744.jpg',6,4.2),(66,'Big max fries',78.00,'Fries',NULL,NULL,'so big','2_fast\\Products\\Big_max_fries\\191085.jpg',7,4.0),(67,'MC fries',9.80,'Fries',NULL,NULL,'you will love it','Fries_home\\Products\\MC_fries\\106608.jpg',14,4.0),(68,'Frech fries',24.00,'Fries',NULL,NULL,'da','Fries_home\\Products\\Frech_fries\\267713.jpg',14,4.1),(69,'Greek Salad',18.90,'Salad',NULL,NULL,'so greek, really greek, the most greek  salad you have ever seen!!!!! let\'s try it','12Food_shop\\Products\\Greek_Salad\\120656.jpg',1,4.2),(70,'Healthy Club sandwich',20.00,'Sandwich',NULL,NULL,'so club bro','12Food_shop\\Products\\Club_sandwich\\141676.jpg',1,4.1),(71,'Double Cheeseburger',12.90,'Burger',NULL,NULL,'You will love it, because it\'s double cheese','12Food_shop\\Products\\Double_Cheeseburger\\3867148.jpg',1,3.9),(72,'The ultimate pizza',188.00,'Pizza',NULL,NULL,'hahahaha, you will love it','Pizza_shop\\Products\\The_ultimate_pizza\\3845083.jpg',2,4.5),(73,'Weird looking pizza',0.99,'Pizza',NULL,NULL,'what? is that a pizza?','Pizza_shop\\Products\\Weird_looking_pizza\\2521769.jpg',2,4.6);
/*!40000 ALTER TABLE `merchants_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 18:27:46
