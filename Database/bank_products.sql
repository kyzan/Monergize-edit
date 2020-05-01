-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `seller_id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `product_id` int(11) NOT NULL,
  `product_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `category` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sold` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('COMP100001',100,'Dodge','Books','10','10'),('COMP100002',101,'BMW','Health','10','10'),('COMP100003',102,'Ford','Fashion','10','10'),('COMP100004',103,'Porsche','Electronics','10','10'),('COMP100005',104,'Volkswagen','Books','20','20'),('COMP100006',105,'Daihatsu','Health','20','20'),('COMP100007',106,'Daimler','Fashion','20','20'),('COMP100008',107,'Subaru','Electronics','20','20'),('COMP100009',108,'Hyundai Motors','Books','30','30'),('COMP100010',109,'Vauxhall','Health','30','30'),('STUP100001',110,'Mitsubishi Motors','Fashion','30','30'),('STUP100002',111,'Toyota','Electronics','30','30'),('STUP100003',112,'Daihatsu','Books','40','40'),('STUP100004',113,'Mahindra and Mahindra','Health','40','40'),('STUP100005',114,'General Motors','Fashion','40','40'),('STUP100006',115,'Isuzu','Electronics','40','40'),('STUP100007',116,'Porsche','Books','50','50'),('STUP100008',117,'Renault','Health','50','50'),('STUP100009',118,'MINI','Fashion','50','50'),('STUP100010',119,'Cadillac','Electronics','50','50');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-01 16:26:59
