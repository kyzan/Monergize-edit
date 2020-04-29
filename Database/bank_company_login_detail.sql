CREATE DATABASE  IF NOT EXISTS `bank` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bank`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `company_login_detail`
--

DROP TABLE IF EXISTS `company_login_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_login_detail` (
  `company_id` varchar(10) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_login_detail`
--

LOCK TABLES `company_login_detail` WRITE;
/*!40000 ALTER TABLE `company_login_detail` DISABLE KEYS */;
INSERT INTO `company_login_detail` VALUES ('COMP100001','1234567'),('COMP100002','1234567'),('COMP100003','1234567'),('COMP100004','1234567'),('COMP100005','1234567'),('COMP100006','1234567'),('COMP100007','1234567'),('COMP100008','1234567'),('COMP100009','1234567'),('COMP100010','1234567'),('COMP100011','1234567'),('COMP100012','1234567'),('COMP100013','1234567'),('COMP100014','1234567'),('COMP100015','1234567'),('COMP100016','1234567'),('COMP100017','1234567'),('COMP100018','1234567'),('COMP100019','1234567'),('COMP100020','1234567'),('COMP100021','1234567'),('COMP100022','1234567'),('COMP100023','1234567'),('COMP100024','1234567'),('COMP100025','1234567'),('COMP100026','1234567'),('COMP100027','1234567'),('COMP100028','1234567'),('COMP100029','1234567'),('COMP100030','1234567'),('COMP100031','1234567'),('COMP100032','1234567'),('COMP100033','1234567'),('COMP100034','1234567'),('COMP100035','1234567'),('COMP100036','1234567'),('COMP100037','1234567'),('COMP100038','1234567'),('COMP100039','1234567'),('COMP100040','1234567');
/*!40000 ALTER TABLE `company_login_detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-28 12:13:52