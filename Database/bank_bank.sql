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
-- Table structure for table `bank`
--

DROP TABLE IF EXISTS `bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bank` (
  `Universal_id` char(5) COLLATE utf8_unicode_ci NOT NULL,
  `bank_id` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `bank_name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `branch_id` int(11) NOT NULL,
  `branch_name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `branch_contact_number` int(11) DEFAULT NULL,
  `number_of_customer` int(11) DEFAULT NULL,
  `total_assets` float DEFAULT NULL,
  `ROI_for_loans` float DEFAULT NULL,
  `ROI_for_savings` float DEFAULT NULL,
  `ROI_for_current` float DEFAULT NULL,
  `no_of_fds` int(11) DEFAULT NULL,
  `min_acc_balance` int(11) DEFAULT NULL,
  `annual_share_govt` float DEFAULT NULL,
  `loan_taken` int(11) DEFAULT NULL,
  `money_lent` int(11) NOT NULL,
  PRIMARY KEY (`bank_id`,`Universal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank`
--

LOCK TABLES `bank` WRITE;
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
INSERT INTO `bank` VALUES ('B102','BANK100001','SBI',100001,'Okhla',1234567890,0,7700000,15,4,10,0,10000,770000,0,0),('B104','BANK100002','UBI',100001,'Vasant Kunj',1234567891,0,9800000,13.5,4.5,11,0,10000,980000,0,0),('B106','BANK100003','BOB',100001,'Vasant Kunj',1234567892,0,11900000,14,6,11,0,0,1190000,0,0),('B108','BANK100004','HDFC',100001,'Kalkaji',1234567893,0,14000000,12.5,7,11,0,0,1400000,0,0),('B110','BANK100005','HSBC',100001,'Nehru Place',1234567894,0,161000000,12,4,10.5,0,0,16100000,0,0),('B112','BANK100006','PNB',100001,'Nehru Place',1234567895,0,182000,12,5.5,10,0,5000,18200,0,0);
/*!40000 ALTER TABLE `bank` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-01 16:26:58
