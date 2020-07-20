-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 20, 2020 at 11:10 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookmgmt`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `bid` int(20) NOT NULL,
  `bookname` varchar(50) NOT NULL,
  `bookprice` int(20) NOT NULL,
  `bookauthor` varchar(50) NOT NULL,
  `bookpublishyear` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`bid`, `bookname`, `bookprice`, `bookauthor`, `bookpublishyear`) VALUES
(1, 'As a Man Thinketh', 2500, 'James Allen', 1903),
(2, 'The Power of Positive Thinking', 1500, ' Norman Vincent Peale', 1952),
(3, 'Pride and Prejudice', 2000, ' Jane Austen', 1813),
(4, 'A Passage to India', 1300, ' E. M. Forster', 1924);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
