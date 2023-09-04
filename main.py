from scripts.parse_sql import parse_sql, build_java_entity,remove_comments


def main():
    with open('test/record_user_app_exp.sql', 'r') as file:
        sql_content = file.read()

    lines = sql_content.split('\n')
    cleaned_lines = remove_comments(lines)
    cleaned_sql = '\n'.join(cleaned_lines)
    tables = parse_sql(cleaned_sql)
    # 存檔位置
    saved_path = 'output/'
    package_name = 'com.locas.conquerworld.core'
    build_java_entity(tables, saved_path, package_name)


if __name__ == "__main__":
    main()
