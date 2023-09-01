import unittest
from scripts.parse_sql import parse_sql, build_java_entity, covert_naming_rule, find_auto_increment, remove_comments


class MyTestCase(unittest.TestCase):
    def test_sql_parse(self):
        with open('test/conquer_world_local.sql', 'r') as file:
            sql_content = file.read()

        lines = sql_content.split('\n')
        cleaned_lines = remove_comments(lines)
        cleaned_sql = '\n'.join(cleaned_lines)
        tables = parse_sql(cleaned_sql)
        for table in tables:
            print('---------------------' + table.name + ' Starts' + '---------------------')
            for field in table.fields:
                print('Column Name: ' + field.name)
                print('Column Type: ' + field.field_type)
                print('Is AI: ' + str(field.auto_increment))
            print('---------------------' + table.name + ' Ends' + '---------------------')
            print('\n')
        # build_java_entity(tables, 'output/', 'com.example.demo')



    def test_name(self):
        name = "user_app_ledger"
        t = covert_naming_rule(name, True)
        f = covert_naming_rule(name, False)
        print(t)
        print(f)
        name = "item"
        t = covert_naming_rule(name, True)
        f = covert_naming_rule(name, False)
        print(t)
        print(f)


    def test_find_auto_increment(self):
        with open('test/conquer_world_local.sql', 'r') as file:
            sql_content = file.read()

        lines = sql_content.split('\n')
        cleaned_lines = remove_comments(lines)
        cleaned_sql = '\n'.join(cleaned_lines)

        auto_fields = find_auto_increment(cleaned_sql)
        # print(cleaned_sql)
        for auto_field in auto_fields:
            print(auto_field.table_name)
            print(auto_field.field_name)
