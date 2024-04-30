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
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_favorite`
--

LOCK TABLES `accounts_favorite` WRITE;
/*!40000 ALTER TABLE `accounts_favorite` DISABLE KEYS */;
INSERT INTO `accounts_favorite` VALUES (4,3,1),(7,4,1),(1,5,1),(2,7,1),(36,11,1),(50,1,2),(6,2,2),(9,3,2),(13,9,2),(49,14,2),(53,1,3),(52,2,3),(10,3,4),(48,6,4),(5,7,4),(12,8,4),(47,13,4),(51,14,4),(16,6,6),(15,7,6),(23,8,6),(14,9,6),(22,10,6),(35,11,6),(19,2,7),(20,4,7),(18,5,7),(34,8,7),(32,10,7),(21,12,7),(26,6,8),(25,7,8),(24,9,8),(43,13,8),(41,11,9),(38,13,9),(42,6,12),(46,1,13),(45,2,13),(44,8,13);
/*!40000 ALTER TABLE `accounts_favorite` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 18:27:48
