-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 24, 2016 at 06:17 PM
-- Server version: 5.5.46-0ubuntu0.14.04.2
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Sim`
--

-- --------------------------------------------------------

--
-- Table structure for table `Job`
--

CREATE TABLE IF NOT EXISTS `Job` (
  `job_id` int(10) NOT NULL AUTO_INCREMENT,
  `id` varchar(100) DEFAULT NULL,
  `name` varchar(10) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `client` varchar(100) DEFAULT NULL,
  `comment` text,
  `checker_name` varchar(100) DEFAULT NULL,
  `engineer_name` varchar(100) DEFAULT NULL,
  `approved_name` varchar(100) DEFAULT NULL,
  `checker_date` varchar(10) DEFAULT NULL,
  `ref` varchar(100) DEFAULT NULL,
  `part` varchar(100) DEFAULT NULL,
  `rev` varchar(100) DEFAULT NULL,
  `approved_date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `Job_material`
--

CREATE TABLE IF NOT EXISTS `Job_material` (
  `job_id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `E` double DEFAULT NULL,
  `poisson` double DEFAULT NULL,
  `density` double DEFAULT NULL,
  `damp` double DEFAULT NULL,
  `alpha` double DEFAULT NULL,
  `G` double DEFAULT NULL,
  `strength` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`name`,`job_id`),
  KEY `fk_job_id` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Joint`
--

CREATE TABLE IF NOT EXISTS `Joint` (
  `job_id` int(10) NOT NULL,
  `id` int(10) NOT NULL,
  `x` double NOT NULL,
  `y` double NOT NULL,
  `z` double DEFAULT NULL,
  `support` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`,`job_id`),
  KEY `fk_job_id2` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Table structure for table `Member`
--

CREATE TABLE IF NOT EXISTS `Member` (
  `job_id` int(10) NOT NULL,
  `member_id` int(10) NOT NULL DEFAULT '0',
  `member_property` int(10) DEFAULT NULL,
  PRIMARY KEY (`member_id`,`job_id`),
  KEY `fk_job_id1` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Table structure for table `Member_incidence`
--

CREATE TABLE IF NOT EXISTS `Member_incidence` (
  `job_id` int(10) NOT NULL,
  `member_id` int(10) NOT NULL DEFAULT '0',
  `joint_id` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`job_id`,`member_id`,`joint_id`),
  KEY `fk_member_id` (`member_id`),
  KEY `fk_joint_id` (`joint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Member_property`
--

CREATE TABLE IF NOT EXISTS `Member_property` (
  `job_id` int(10) NOT NULL,
  `id` int(10) NOT NULL,
  `type` varchar(100) NOT NULL,
  `YD` float DEFAULT NULL,
  `ZD` float DEFAULT NULL,
  PRIMARY KEY (`id`,`job_id`),
  KEY `fk_job_id4` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Constraints for table `Job_material`
--
ALTER TABLE `Job_material`
  ADD CONSTRAINT `fk_job_id` FOREIGN KEY (`job_id`) REFERENCES `Job` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Joint`
--
ALTER TABLE `Joint`
  ADD CONSTRAINT `fk_job_id2` FOREIGN KEY (`job_id`) REFERENCES `Job` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Member`
--
ALTER TABLE `Member`
  ADD CONSTRAINT `fk_job_id1` FOREIGN KEY (`job_id`) REFERENCES `Job` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Member_incidence`
--
ALTER TABLE `Member_incidence`
  ADD CONSTRAINT `fk_joint_id` FOREIGN KEY (`joint_id`) REFERENCES `Joint` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_job_id3` FOREIGN KEY (`job_id`) REFERENCES `Joint` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_member_id` FOREIGN KEY (`member_id`) REFERENCES `Member` (`member_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Member_property`
--
ALTER TABLE `Member_property`
  ADD CONSTRAINT `fk_job_id4` FOREIGN KEY (`job_id`) REFERENCES `Job` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE;
  


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
