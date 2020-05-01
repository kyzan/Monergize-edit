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
-- Table structure for table `bank_customer`
--

DROP TABLE IF EXISTS `bank_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bank_customer` (
  `Name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Customer_ID` int(11) NOT NULL,
  `Bank_ID` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `Age` int(11) NOT NULL,
  `Account_No` int(11) NOT NULL,
  `Govt_ID` int(11) NOT NULL,
  `Account_Type` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Profession` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Contact_No` int(11) NOT NULL,
  `State` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Branch_ID` int(11) NOT NULL,
  `Latest_Transaction` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Fixed_Deposit` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Bank_Balance` int(11) NOT NULL,
  `Monthly_Salary` int(11) NOT NULL,
  `Username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Email_ID` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Tax_Bracket` int(11) NOT NULL,
  `Loan_EMI` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `Account_Opening_Date` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Customer_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank_customer`
--

LOCK TABLES `bank_customer` WRITE;
/*!40000 ALTER TABLE `bank_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `bank_customer` ENABLE KEYS */;
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
