-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               10.0.13-MariaDB - openSUSE package
-- Server OS:                    Linux
-- HeidiSQL Version:             9.1.0.4867
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for CareMeToo
CREATE DATABASE IF NOT EXISTS `CareMeToo` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `CareMeToo`;


-- Dumping structure for table CareMeToo.caregivers
CREATE TABLE IF NOT EXISTS `caregivers` (
  `idcaregivers` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcaregivers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table CareMeToo.data
CREATE TABLE IF NOT EXISTS `data` (
  `iddata` int(11) NOT NULL AUTO_INCREMENT,
  `idcaregiver` int(11) NOT NULL,
  `datatype` varchar(45) DEFAULT NULL,
  `value` varchar(45) DEFAULT NULL,
  `extra` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`iddata`),
  KEY `index_data` (`idcaregiver`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table CareMeToo.event
CREATE TABLE IF NOT EXISTS `event` (
  `idevent` int(11) NOT NULL AUTO_INCREMENT,
  `idcaregiver` int(11) NOT NULL,
  `idmultimedia` int(11) NOT NULL,
  `activity` varchar(250) DEFAULT NULL,
  `mood` varchar(45) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`idevent`),
  KEY `idcaregiver` (`idcaregiver`),
  CONSTRAINT `FK_event_caregivers` FOREIGN KEY (`idcaregiver`) REFERENCES `caregivers` (`idcaregivers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table CareMeToo.multimedia
CREATE TABLE IF NOT EXISTS `multimedia` (
  `idmultimedia` int(11) NOT NULL AUTO_INCREMENT,
  `idcaregiver` int(11) NOT NULL,
  `description` varchar(250) DEFAULT NULL,
  `path` varchar(45) DEFAULT NULL,
  `extra` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idmultimedia`),
  KEY `FK_multimedia_caregivers` (`idcaregiver`),
  CONSTRAINT `FK_multimedia_caregivers` FOREIGN KEY (`idcaregiver`) REFERENCES `caregivers` (`idcaregivers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
