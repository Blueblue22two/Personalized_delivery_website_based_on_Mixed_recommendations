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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-11-15 09:37:16.387711'),(2,'auth','0001_initial','2023-11-15 09:37:16.746239'),(3,'admin','0001_initial','2023-11-15 09:37:16.842131'),(4,'admin','0002_logentry_remove_auto_add','2023-11-15 09:37:16.851140'),(5,'admin','0003_logentry_add_action_flag_choices','2023-11-15 09:37:16.860141'),(6,'contenttypes','0002_remove_content_type_name','2023-11-15 09:37:16.927268'),(7,'auth','0002_alter_permission_name_max_length','2023-11-15 09:37:16.968291'),(8,'auth','0003_alter_user_email_max_length','2023-11-15 09:37:16.990322'),(9,'auth','0004_alter_user_username_opts','2023-11-15 09:37:16.998325'),(10,'auth','0005_alter_user_last_login_null','2023-11-15 09:37:17.038160'),(11,'auth','0006_require_contenttypes_0002','2023-11-15 09:37:17.041159'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-15 09:37:17.051161'),(13,'auth','0008_alter_user_username_max_length','2023-11-15 09:37:17.099172'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-15 09:37:17.142891'),(15,'auth','0010_alter_group_name_max_length','2023-11-15 09:37:17.160796'),(16,'auth','0011_update_proxy_permissions','2023-11-15 09:37:17.170792'),(17,'auth','0012_alter_user_first_name_max_length','2023-11-15 09:37:17.215749'),(18,'sessions','0001_initial','2023-11-15 09:37:17.243747'),(19,'accounts','0001_initial','2024-03-10 06:42:12.388217'),(20,'merchants','0001_initial','2024-03-15 15:47:26.427132'),(21,'customers','0001_initial','2024-03-15 15:47:26.587175'),(22,'customers','0002_initial','2024-03-15 15:47:26.896392'),(23,'orders','0001_initial','2024-03-15 15:47:27.168463'),(24,'cart','0001_initial','2024-03-19 12:57:38.256863'),(25,'accounts','0002_address_city_address_detail_address_district_and_more','2024-03-21 12:21:21.210430'),(26,'orders','0002_order_address_line_order_delivery_status_and_more','2024-03-21 12:21:21.282200'),(27,'orders','0003_remove_order_product_remove_order_product_price_and_more','2024-03-22 14:17:59.362857'),(28,'orders','0004_order_iscomment','2024-03-23 05:09:43.712784'),(29,'merchants','0002_product_average_rate','2024-03-26 10:51:54.291585'),(30,'cart','0002_alter_cartitem_quantity','2024-04-15 14:28:15.714372'),(31,'accounts','0003_alter_shop_total_rating','2024-04-17 18:17:06.419565'),(32,'accounts','0004_remove_shoppingcart_quantity','2024-04-24 05:54:57.191296'),(33,'accounts','0005_shoppingcart_quantity','2024-04-24 06:34:58.010978'),(34,'orders','0005_alter_order_address_line','2024-04-24 16:41:30.368311'),(35,'orders','0006_alter_order_sale_time','2024-04-24 16:47:27.031727'),(36,'accounts','0006_alter_customer_password_alter_customer_username_and_more','2024-04-26 18:55:15.854479');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
