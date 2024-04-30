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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_address`
--

LOCK TABLES `accounts_address` WRITE;
/*!40000 ALTER TABLE `accounts_address` DISABLE KEYS */;
INSERT INTO `accounts_address` VALUES (3,'四川省-成都市-成华区-CDUT songlin120',4,'成都市','CDUT songlin120','成华区','四川省'),(4,'江苏省-南京市-玄武区-hahha',4,'南京市','hahha','玄武区','江苏省'),(5,'北京市-北京市-朝阳区-jianshe road',4,'北京市','jianshe road','朝阳区','北京市'),(6,'辽宁省-大连市-瓦房店市-dog shop',4,'大连市','dog shop','瓦房店市','辽宁省'),(7,'山东省-济南市-长清区-sanzhong high school',4,'济南市','sanzhong high school','长清区','山东省'),(8,'天津市-天津市-和平区-fandou st',1,'天津市','fandou st','和平区','天津市'),(11,'吉林省-长春市-南关区-fandou st',1,'长春市','fandou st','南关区','吉林省'),(12,'浙江省-温州市-鹿城区-whs ',1,'温州市','whs ','鹿城区','浙江省'),(14,'四川省-成都市-成华区-CDUT',2,'成都市','CDUT','成华区','四川省'),(15,'四川省-成都市-成华区-longguang st.',2,'成都市','longguang st.','成华区','四川省'),(16,'四川省-成都市-成华区-铁建',1,'成都市','铁建','成华区','四川省'),(17,'贵州省-六盘水市-六枝特区-where',6,'六盘水市','where','六枝特区','贵州省'),(18,'浙江省-台州市-路桥区-school',7,'台州市','school','路桥区','浙江省'),(19,'青海省-西宁市-城中区-carzy',8,'西宁市','carzy','城中区','青海省'),(20,'天津市-天津市-西青区-da st.',9,'天津市','da st.','西青区','天津市'),(21,'内蒙古自治区-呼和浩特市-回民区-hui',9,'呼和浩特市','hui','回民区','内蒙古自治区'),(22,'山西省-大同市-云冈区-大同大学',10,'大同市','大同大学','云冈区','山西省'),(23,'四川省-泸州市-江阳区-damn',12,'泸州市','damn','江阳区','四川省'),(24,'台湾省-台中市-台中市-guess',8,'台中市','guess','台中市','台湾省'),(25,'四川省-自贡市-大安区-primary school',13,'自贡市','primary school','大安区','四川省'),(26,'北京市-北京市-朝阳区-what st.',3,'北京市','what st.','朝阳区','北京市');
/*!40000 ALTER TABLE `accounts_address` ENABLE KEYS */;
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
