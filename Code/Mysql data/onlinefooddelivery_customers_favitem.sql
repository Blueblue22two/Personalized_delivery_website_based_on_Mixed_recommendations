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
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_favitem`
--

LOCK TABLES `customers_favitem` WRITE;
/*!40000 ALTER TABLE `customers_favitem` DISABLE KEYS */;
INSERT INTO `customers_favitem` VALUES (2,1,9),(6,1,11),(29,1,32),(8,1,37),(7,1,38),(5,1,43),(10,1,46),(9,1,54),(4,2,43),(65,2,67),(62,2,68),(64,2,71),(79,3,21),(75,3,38),(76,3,53),(78,3,61),(74,3,70),(77,3,73),(20,4,19),(21,4,36),(23,4,39),(24,4,40),(22,4,47),(59,4,49),(58,4,50),(56,4,62),(57,4,65),(73,4,67),(28,6,16),(27,6,18),(70,6,20),(66,6,48),(67,6,50),(68,6,63),(69,6,69),(15,7,32),(14,7,33),(13,7,34),(44,7,42),(12,7,43),(11,7,55),(26,7,59),(25,7,60),(71,7,64),(72,7,71),(49,8,8),(16,8,16),(17,8,17),(18,8,18),(50,8,22),(45,8,31),(19,8,45),(47,8,46),(48,8,53),(38,9,16),(40,9,17),(39,9,18),(37,9,22),(32,9,38),(33,9,45),(36,9,52),(35,9,57),(34,9,58),(31,9,63),(41,10,13),(43,12,11),(42,12,13),(55,13,13),(51,13,21),(52,13,42),(53,13,51),(54,13,61),(61,13,72),(60,13,73);
/*!40000 ALTER TABLE `customers_favitem` ENABLE KEYS */;
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
