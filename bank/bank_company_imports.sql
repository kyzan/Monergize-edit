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
-- Table structure for table `company_imports`
--

DROP TABLE IF EXISTS `company_imports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_imports` (
  `comp_id` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `branches_in_india` int NOT NULL,
  `importers_id` int NOT NULL,
  `raw_material` float NOT NULL,
  `finished_product` float NOT NULL,
  `custom_duty` float NOT NULL,
  `relaxation_limit` float NOT NULL,
  `gst` float NOT NULL,
  PRIMARY KEY (`comp_id`),
  CONSTRAINT `company_imports_ibfk_1` FOREIGN KEY (`comp_id`) REFERENCES `company_market_detail` (`comp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_imports`
--

LOCK TABLES `company_imports` WRITE;
/*!40000 ALTER TABLE `company_imports` DISABLE KEYS */;
INSERT INTO `company_imports` VALUES ('COMP100001',2,12345,21797.1,4738.92,40,10,17),('COMP100002',3,12045,89840.2,22916.6,30,11,16),('COMP100003',4,11745,38630.1,18349,50,12,15),('COMP100004',5,11445,70572.4,71814.9,40,10,17),('COMP100005',6,11145,3953.47,79466.6,30,11,16),('COMP100006',7,10845,34826.4,47828.3,50,12,15),('COMP100007',8,10545,31705.8,26361.8,40,10,17),('COMP100008',9,10245,23634.9,19907.3,30,11,16),('COMP100009',10,99451,73220.3,40328.9,50,12,15),('COMP100010',11,96451,4960.24,58962.1,40,10,17),('COMP100011',12,93451,90775.1,2412.89,30,11,16),('COMP100012',13,90451,42090.8,57680.4,50,12,15),('COMP100013',14,87451,66914.3,77531.5,40,10,17),('COMP100014',15,84451,74694.9,82962.9,30,11,16),('COMP100015',16,81451,37811.7,71127.9,50,12,15),('COMP100016',17,78451,90501.8,49320.6,40,10,17),('COMP100017',18,75451,90998,18816.5,30,11,16),('COMP100018',19,72451,25441.9,37223.9,50,12,15),('COMP100019',20,69451,60454.1,50444,40,12,17),('COMP100020',21,66451,80568.5,31664.2,30,11,16);
/*!40000 ALTER TABLE `company_imports` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-03  0:30:00
