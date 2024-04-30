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
-- Table structure for table `accounts_merchant`
--

DROP TABLE IF EXISTS `accounts_merchant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_merchant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `shop_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_merchant_shop_id_e1444cf9_fk_accounts_shop_id` (`shop_id`),
  KEY `accounts_merchant_username_4e3ac5a6` (`username`),
  CONSTRAINT `accounts_merchant_shop_id_e1444cf9_fk_accounts_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `accounts_shop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_merchant`
--

LOCK TABLES `accounts_merchant` WRITE;
/*!40000 ALTER TABLE `accounts_merchant` DISABLE KEYS */;
INSERT INTO `accounts_merchant` VALUES (1,'calvin','1bbd886460827015e5d605ed44252251','12345678911',1),(2,'damn','25d55ad283aa400af464c76d713c07ad','22345678910',2),(3,'Dumpling','bae5e3208a3c700e3db642b6631e95b9','22345678910',3),(4,'Beef','d27d320c27c3033b7883347d8beca317','33345678999',4),(5,'Hambuger','b857eed5c9405c1f2b98048aae506792','12345678911',5),(6,'ChinaTown','6ebe76c9fb411be97b3b0d48b791a7c9','98765678911',6),(7,'Fast','d1b2cc725d846f0460ff290c60925070','22345678910',7),(8,'FoodCanteen','25f9e794323b453885f5181f1b624d0b','17711475039',8),(9,'Merchant5','1bbd886460827015e5d605ed44252251','12345678911',9),(10,'Merchant6','d1b2cc725d846f0460ff290c60925070','22345678910',10),(11,'RockRockMerchant','b2023820a60123ef4e6869bacaf7d90c','74345678915',11),(12,'BeefMerchant','22d7fe8c185003c98f97e5d6ced420c7','51365678911',12),(13,'13999','f5c7e3b79fd8c720826692b17eefb4c6','24708045743',13),(14,'MerchantFries','9ae2be73b58b565bce3e47493a56e26a','14765646915',14),(15,'TestMerchant','pbkdf2_sha256$600000$9timy85IzhlJiwSRVyaAdy$2+ZrkpMNhql6XX/GsKkeGQ1fXC5zpkbUvCpLv8jCWSk=','22345678910',15);
/*!40000 ALTER TABLE `accounts_merchant` ENABLE KEYS */;
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
