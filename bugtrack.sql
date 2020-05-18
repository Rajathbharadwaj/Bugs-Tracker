-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 18, 2020 at 07:08 PM
-- Server version: 5.7.24
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bugtrack`
--

-- --------------------------------------------------------

--
-- Table structure for table `buginfo`
--

DROP TABLE IF EXISTS `buginfo`;
CREATE TABLE IF NOT EXISTS `buginfo` (
  `bugid` int(5) NOT NULL,
  `tob` text NOT NULL,
  `description` text NOT NULL,
  `priority` int(3) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` text NOT NULL,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`bugid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `buginfo`
--

INSERT INTO `buginfo` (`bugid`, `tob`, `description`, `priority`, `time`, `status`, `name`) VALUES
(2197, 'reas', 'fsasdasd', 2, '2020-05-18 17:18:52', 'In process', 'rajath'),
(2856, 'reas', 'fsasdasd', 2, '2020-05-18 17:20:15', 'In process', 'rajath'),
(3046, 'reas', 'fsasdasd', 2, '2020-05-18 17:20:39', 'Fixed', 'rajath'),
(3390, 'reas', 'fsasdasd', 2, '2020-05-18 18:12:13', 'In process', 'rajath'),
(4117, 'reas', 'fsasdasd', 2, '2020-05-18 17:22:16', 'Fixed', 'rajath'),
(6240, '', '', 1, '2020-05-18 18:19:59', 'Not yet Assigned', ''),
(8638, 'easd', 'asdas', 3, '2020-05-18 17:23:13', 'In process', 'RajathDB'),
(9413, '', '', 1, '2020-05-18 18:20:39', 'Not yet Assigned', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
