-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2019 at 09:38 AM
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
-- Database: `j1`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `std_id` varchar(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `phone` bigint(10) NOT NULL,
  `email` varchar(25) NOT NULL,
  `roll_no` int(5) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`fname`, `lname`, `std_id`, `gender`, `dob`, `phone`, `email`, `roll_no`, `address`) VALUES
('janmejay', 'patil', 'TU039', '   MALE   ', '2001-01-26', 9820401124, 'janmejay@gmail.com', 18, '02-Shivkrupa CHS\n'),
('Gauresh', 'Rane', 'TU069', '   MALE   ', '1999-12-22', 9876543210, 'gau@rane.com', 19, 'Kalpaturu Complex\n'),
('shivani', 'shinde', 'TU49', '   FEMALE ', '2001-02-12', 9730389077, 'shivanishinde@gmail.com', 18, 'Kulgaon,Badlapur\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
