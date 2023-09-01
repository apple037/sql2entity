import unittest
from scripts.parse_sql import parse_sql, build_java_entity, covert_naming_rule, find_auto_increment


class MyTestCase(unittest.TestCase):
    def test_sql_parse(self):
        test_sql = ("CREATE TABLE `user_app_ledger` (   `id` bigint(14) NOT NULL,   `order_id` varchar(255) NOT NULL "
                    "DEFAULT '' COMMENT '訂單號',   `user_id` bigint(14) NOT NULL COMMENT '會員id',   `currency` varchar("
                    "32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '幣種',   `trade_type` "
                    "varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '交易類型',   "
                    "`amount` decimal(28,16) NOT NULL COMMENT '數量',   `balance_after` decimal(28,16) NOT NULL COMMENT "
                    "'變動後餘額',   `memo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,   "
                    "`created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ) ENGINE=InnoDB DEFAULT "
                    "CHARSET=utf8mb4;   CREATE TABLE `user_app_wallet` (   `id` bigint(14) NOT NULL,   "
                    "`user_id` bigint(14) NOT NULL COMMENT '會員id',   `currency` varchar(32) NOT NULL COMMENT '幣種',   "
                    "`balance` decimal(28,16) NOT NULL COMMENT '餘額',   `frozen` decimal(28,16) NOT NULL COMMENT '凍結' "
                    ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; ALTER TABLE `record_app_login` MODIFY `id` bigint(20) "
                    "NOT NULL AUTO_INCREMENT; ALTER TABLE `user_app_ledger` MODIFY `id` bigint(14) NOT NULL "
                    "AUTO_INCREMENT;")
        tables = parse_sql(test_sql)
        build_java_entity(tables, 'output/', 'com.example.demo')



    def test_name(self):
        name = "user_app_ledger"
        t = covert_naming_rule(name, True)
        f = covert_naming_rule(name, False)
        print(t)
        print(f)


    def test_find_auto_increment(self):
        test_sql = ("CREATE TABLE `user_app_ledger` (   `id` bigint(14) NOT NULL,   `order_id` varchar(255) NOT NULL "
                    "DEFAULT '' COMMENT '訂單號',   `user_id` bigint(14) NOT NULL COMMENT '會員id',   `currency` varchar("
                    "32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '幣種',   `trade_type` "
                    "varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '交易類型',   "
                    "`amount` decimal(28,16) NOT NULL COMMENT '數量',   `balance_after` decimal(28,16) NOT NULL COMMENT "
                    "'變動後餘額',   `memo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,   "
                    "`created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ) ENGINE=InnoDB DEFAULT "
                    "CHARSET=utf8mb4;   CREATE TABLE `user_app_wallet` (   `id` bigint(14) NOT NULL,   "
                    "`user_id` bigint(14) NOT NULL COMMENT '會員id',   `currency` varchar(32) NOT NULL COMMENT '幣種',   "
                    "`balance` decimal(28,16) NOT NULL COMMENT '餘額',   `frozen` decimal(28,16) NOT NULL COMMENT '凍結' "
                    ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; ALTER TABLE `record_app_login` MODIFY `id` bigint(20) "
                    "NOT NULL AUTO_INCREMENT; ALTER TABLE `user_app_ledger` MODIFY `id` bigint(14) NOT NULL "
                    "AUTO_INCREMENT;")
        auto_fields = find_auto_increment(test_sql)
        print(test_sql)
        for auto_field in auto_fields:
            print(auto_field.table_name)
            print(auto_field.field_name)
