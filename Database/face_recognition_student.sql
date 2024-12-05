-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: face_recognition
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Student_ID` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Department` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Year` varchar(10) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `DOB` varchar(10) DEFAULT NULL,
  `Mobile_No` bigint DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Roll_No` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Teacher_name` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'raj','Data Science','MSc','2020','Semester-2','Full Time','Male','20/09/2001',7359857317,'surat','12','rajpatel@gmail.com','ML','Yes'),(2,'Puneetha','Data Science','MSc','2022','Semester-2','Full Time','Female','27/12/2002',8971158142,'m\'lore','puneetha26','puneetha@gmail.com','ml','Yes'),(3,'Meghna','Data Science','MSc','2021','Semester-2','Part Time','Female','20/05/2002',9632689622,'malpe','28','mj@gmail.com','ML','Yes'),(4,'Sushantha','Data Science','MSc','2020','Semester-4','Full Time','Male','13/08/2001',5598567136,'m\'lore','29','sh@gmail.com','ML','Yes'),(5,'Deepika','Data Science','BSc','2023','Semester-3','Part Time','Female','13/12/2002',3597145968,'bglor','34','dd@gmail.com','ML','Yes'),(6,'Rakshith','Data Science','MSc','2023','Semester-5','Part Time','Male','26/12/2002',896416579,'blore','19','rv@gmail.com','ML','Yes'),(7,'Gaurang','Data Science','BSc','2022','Semester-1','Full Time','Male','10/05/2002',98753215874,'mumbai','15','gs@gmail.com','ML','Yes'),(8,'Deeksha','Data Science','BSc','2022','Semester-4','Part Time','Female','09/05/2001',1354796582,'blore','04','rs@gmail.com','ML','Yes'),(9,'Raj','Data Science','BSc','2022','Semester-3','Full Time','Male','01/01/2002',6351578684,'surat','12','rp@gmail.com','ML','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-16 10:49:40
