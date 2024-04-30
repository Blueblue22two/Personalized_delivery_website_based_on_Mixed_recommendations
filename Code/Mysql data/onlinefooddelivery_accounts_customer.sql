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
-- Table structure for table `accounts_customer`
--

DROP TABLE IF EXISTS `accounts_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_customer_username_ef0a2dad` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer`
--

LOCK TABLES `accounts_customer` WRITE;
/*!40000 ALTER TABLE `accounts_customer` DISABLE KEYS */;
INSERT INTO `accounts_customer` VALUES (1,'calvin','pbkdf2_sha256$600000$LvxmenPqeKfeumuX8H4kk9$P5CzWTbougvGNxrdnhcQOkkGeHcVj6v0XiJ2ifylRqw=','12345678911'),(2,'bob','bae5e3208a3c700e3db642b6631e95b9','12345678911'),(3,'James','pbkdf2_sha256$600000$QmPkC7j7LA5ZslKYNSKcdw$7P2OfIA6MadQG2sy2x/dbfZIBWiX8cV68Gv9EfQl91k=','22345678988'),(4,'Customer4','fbe82b93c071bedda31afded400cca52','12345678911'),(5,'xiangzeqi','25d55ad283aa400af464c76d713c07ad','13808243006'),(6,'reginacustomer','pbkdf2_sha256$600000$Uut60Bs83sFu2g6oBp8JfF$Txivr2IJOcvzk/oicUQYzzI0HgR+2l/d2Mz5W8qhukM=','33345678965'),(7,'beeflover','60d6ea68bdf457e10a3a18ba34974917','78345678910'),(8,'saladman','f98aa3ec36a5b5086c1a93f689259060','17645676035'),(9,'Customer666','eb0b5599e67e299755bda83b862b23dd','22345678910'),(10,'Zhuzhaoyu','0229c73541dbf156680cb8e3b0cf0fb5','12345678910'),(11,'Ethan Zhu','0229c73541dbf156680cb8e3b0cf0fb5','12345678910'),(12,'Liu金雨','b64f1a77b1b317d347f5cb79332c86d2','14345878913'),(13,'DontchineseButPizza','2569d419bfea999ff13fd1f7f4498b89','13345678924');
/*!40000 ALTER TABLE `accounts_customer` ENABLE KEYS */;
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
