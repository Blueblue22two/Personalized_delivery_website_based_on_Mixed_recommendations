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
) ENGINE=InnoDB AUTO_INCREMENT=204 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchants_shoprating`
--

LOCK TABLES `merchants_shoprating` WRITE;
/*!40000 ALTER TABLE `merchants_shoprating` DISABLE KEYS */;
INSERT INTO `merchants_shoprating` VALUES (1,4.5,2),(2,4.2,6),(3,4.1,2),(4,4.2,4),(5,4.3,5),(6,4.5,2),(7,4.5,2),(8,4.5,2),(9,4.6,2),(10,4.1,6),(11,4.4,2),(12,4.7,2),(13,4.3,2),(14,4.6,2),(15,4.5,2),(16,4.2,5),(17,4.1,7),(18,4.7,2),(19,3.9,1),(20,4.3,7),(21,4.7,5),(22,3.9,2),(23,4.9,3),(24,4.4,1),(25,4.7,10),(26,4.5,5),(27,4.7,9),(28,3.9,8),(29,5.0,2),(30,4.4,9),(31,4.5,10),(32,3.8,6),(33,4.5,7),(34,4.3,4),(35,4.0,6),(36,4.2,9),(37,3.8,10),(38,4.3,4),(39,4.3,4),(40,4.6,5),(41,4.2,3),(42,4.7,6),(43,3.8,3),(44,4.1,11),(45,4.5,8),(46,3.8,3),(47,4.6,9),(48,4.1,7),(49,4.5,7),(50,4.4,5),(51,5.0,1),(52,4.1,1),(53,4.6,5),(54,4.0,10),(55,2.8,11),(56,4.0,8),(57,4.4,4),(58,3.9,2),(59,4.0,10),(60,3.0,2),(61,3.5,5),(62,4.1,12),(63,3.8,10),(64,4.6,12),(65,4.1,10),(66,4.0,5),(67,3.9,2),(68,4.8,12),(69,3.9,2),(70,4.6,8),(71,4.0,3),(72,3.5,11),(73,4.0,9),(74,4.6,8),(75,4.2,3),(76,4.1,6),(77,4.5,6),(78,4.5,10),(79,3.5,8),(80,4.0,7),(81,3.6,5),(82,3.9,2),(83,4.8,7),(84,4.2,9),(85,3.8,12),(86,4.0,11),(87,3.9,11),(88,4.5,5),(89,4.7,8),(90,4.6,5),(91,4.1,13),(92,4.1,12),(93,4.0,5),(94,3.0,6),(95,4.5,11),(96,4.2,8),(97,5.0,13),(98,4.2,8),(99,4.6,9),(100,4.6,11),(101,4.3,13),(102,4.6,11),(103,2.7,4),(104,3.6,6),(105,4.2,8),(106,4.5,7),(107,3.0,2),(108,3.3,6),(109,0.0,7),(110,4.5,6),(111,4.0,2),(112,4.4,4),(113,4.4,12),(114,3.8,5),(115,3.8,7),(116,4.7,10),(117,4.4,12),(118,4.5,2),(119,4.6,9),(120,4.1,10),(121,4.2,7),(122,4.8,6),(123,4.0,8),(124,4.0,3),(125,4.4,9),(126,3.9,7),(127,4.0,14),(128,3.9,8),(129,3.7,13),(130,3.5,10),(131,3.5,6),(132,4.6,2),(133,4.3,8),(134,4.8,1),(135,4.3,8),(136,3.2,3),(137,3.2,6),(138,4.0,7),(139,3.8,11),(140,4.7,2),(141,4.3,8),(142,3.2,6),(143,4.7,1),(144,4.5,8),(145,3.0,6),(146,4.5,8),(147,4.0,7),(148,3.2,6),(149,4.0,1),(150,3.5,7),(151,4.6,6),(152,4.7,13),(153,4.5,13),(154,4.2,10),(155,4.3,8),(156,3.4,5),(157,3.4,10),(158,3.6,6),(159,4.1,8),(160,4.6,2),(161,4.6,2),(162,3.9,2),(163,4.6,1),(164,3.9,2),(165,4.1,14),(166,4.1,14),(167,3.9,10),(168,3.6,4),(169,3.7,7),(170,4.2,1),(171,4.7,13),(172,4.4,8),(173,3.8,4),(174,4.8,13),(175,2.8,5),(176,3.9,1),(177,4.3,8),(178,3.4,4),(179,4.7,7),(180,4.8,8),(181,4.6,13),(182,4.1,1),(183,4.2,6),(184,4.8,4),(185,2.6,5),(186,2.8,1),(187,4.2,13),(188,4.5,9),(189,3.0,6),(190,3.1,5),(191,3.1,10),(192,3.5,7),(193,3.4,14),(194,3.3,11),(195,4.5,14),(196,4.4,8),(197,4.5,2),(198,4.6,10),(199,4.5,5),(200,4.4,1),(201,4.0,10),(202,4.2,8),(203,4.4,3);
/*!40000 ALTER TABLE `merchants_shoprating` ENABLE KEYS */;
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
