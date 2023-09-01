-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： local-mysql:3306
-- 產生時間： 2023 年 08 月 29 日 10:39
-- 伺服器版本： 5.7.41
-- PHP 版本： 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `texas_poker_local`
--

-- --------------------------------------------------------

--
-- 資料表結構 `record_app_login`
--

CREATE TABLE `record_app_login` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(14) NOT NULL COMMENT '會員id',
  `login_at` datetime NOT NULL COMMENT '登入時間',
  `logout_at` datetime DEFAULT NULL COMMENT '登出時間',
  `login_ip` varchar(128) NOT NULL COMMENT '登入ip',
  `gps` varchar(64) NOT NULL COMMENT '定位',
  `gps_address` varchar(255) NOT NULL COMMENT '定位地址',
  `device_id` varchar(255) NOT NULL COMMENT '裝置識別碼',
  `device_name` varchar(64) NOT NULL COMMENT '裝置名稱',
  `device_os` varchar(64) NOT NULL COMMENT '裝置系統',
  `updated_at` datetime NOT NULL COMMENT '更新時間'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `user_app`
--

CREATE TABLE `user_app` (
  `id` bigint(14) NOT NULL COMMENT '會員id',
  `register_type` varchar(32) NOT NULL COMMENT '註冊類型',
  `type` varchar(32) NOT NULL COMMENT '帳號類型',
  `account` varchar(64) NOT NULL COMMENT '帳號',
  `email` varchar(64) DEFAULT NULL COMMENT '信箱',
  `password` varchar(255) NOT NULL COMMENT '密碼',
  `salt` varchar(255) NOT NULL COMMENT '鹽巴',
  `nickname` varchar(64) NOT NULL COMMENT '暱稱',
  `avatar` varchar(256) NOT NULL DEFAULT '',
  `gender` varchar(16) NOT NULL DEFAULT 'male' COMMENT '性別',
  `status` varchar(32) NOT NULL COMMENT '狀態',
  `register_ip` varchar(128) NOT NULL COMMENT '註冊ip',
  `last_login_ip` varchar(128) DEFAULT NULL COMMENT '最後登入ip',
  `user_level` smallint(2) NOT NULL COMMENT '等級',
  `vip_level` smallint(2) NOT NULL COMMENT 'vip等級',
  `country` varchar(32) DEFAULT NULL COMMENT '國家',
  `phone` varchar(32) DEFAULT NULL COMMENT '電話',
  `google_auth` varchar(256) DEFAULT '' COMMENT '二步驗証',
  `payment_psw` varchar(256) NOT NULL DEFAULT '' COMMENT '支付密碼',
  `register_at` datetime NOT NULL,
  `last_login_at` datetime DEFAULT NULL,
  `likes` bigint(20) NOT NULL DEFAULT '0' COMMENT '獲讚數',
  `follower_count` bigint(20) NOT NULL DEFAULT '0' COMMENT '粉絲數',
  `follow_count` bigint(20) NOT NULL DEFAULT '0' COMMENT '關注數'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `user_app_ledger`
--

CREATE TABLE `user_app_ledger` (
  `id` bigint(14) NOT NULL,
  `order_id` varchar(255) NOT NULL DEFAULT '' COMMENT '訂單號',
  `user_id` bigint(14) NOT NULL COMMENT '會員id',
  `currency` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '幣種',
  `trade_type` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '交易類型',
  `amount` decimal(28,16) NOT NULL COMMENT '數量',
  `balance_after` decimal(28,16) NOT NULL COMMENT '變動後餘額',
  `memo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `user_app_wallet`
--

CREATE TABLE `user_app_wallet` (
  `id` bigint(14) NOT NULL,
  `user_id` bigint(14) NOT NULL COMMENT '會員id',
  `currency` varchar(32) NOT NULL COMMENT '幣種',
  `balance` decimal(28,16) NOT NULL COMMENT '餘額',
  `frozen` decimal(28,16) NOT NULL COMMENT '凍結'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `record_app_login`
--
ALTER TABLE `record_app_login`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `user_app`
--
ALTER TABLE `user_app`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account` (`account`),
  ADD UNIQUE KEY `nickname` (`nickname`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `country` (`country`,`phone`);

--
-- 資料表索引 `user_app_ledger`
--
ALTER TABLE `user_app_ledger`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `user_app_wallet`
--
ALTER TABLE `user_app_wallet`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `record_app_login`
--
ALTER TABLE `record_app_login`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user_app`
--
ALTER TABLE `user_app`
  MODIFY `id` bigint(14) NOT NULL AUTO_INCREMENT COMMENT '會員id';

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user_app_ledger`
--
ALTER TABLE `user_app_ledger`
  MODIFY `id` bigint(14) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user_app_wallet`
--
ALTER TABLE `user_app_wallet`
  MODIFY `id` bigint(14) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
