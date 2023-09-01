import re
import os
from models.models import FieldInfo, TableInfo, AutoField


def parse_sql(sql_content):
    # 將每個sql語句分開 (以CREATE跟分號分隔)
    sql_statements = separate_sql(sql_content)
    # 取得AutoIncrement的部分
    auto_fields = find_auto_increment(sql_content)
    print(auto_fields[1].table_name)
    print(auto_fields[1].field_name)
    # 將每個table的欄位抓出
    tables = []
    for sql_statement in sql_statements:
        tables.append(parse_table(sql_statement))
    # 將auto_increment的欄位設為True
    for table in tables:
        for field in table.fields:
            for auto_field in auto_fields:

                if table.name == auto_field.table_name and field.name == auto_field.field_name:
                    print('find auto increment: ' + table.name + '.' + field.name)
                    field.auto_increment = True
    return tables


def separate_sql(sql_content):
    # print(sql_content)
    # 將每個sql語句抓出 (以CREATE跟分號分隔)
    match_pattern = re.compile(r'CREATE\s+TABLE\s+`.*?`\s+\(.*?\)*;', re.DOTALL)
    match_result = match_pattern.findall(sql_content)
    return match_result


def parse_table(table_content):
    # 將table name抓出
    table_name = table_content.split(' ')[2]
    # 去除頓點
    table_name = table_name.replace('`', '')
    #print(table_name)
    # 將括號中內容抓出 找第一個左括號 及 最後一個右括號
    left_bracket_index = table_content.find('(')
    right_bracket_index = table_content.rfind(')')
    # 將括號中內容抓出
    parameters = table_content[left_bracket_index + 1:right_bracket_index]
    # 以逗號分隔
    parameters = parameters.split(',')
    fields = []
    # 將每個欄位的名稱及型態抓出
    for parameter in parameters:
        parameter = parameter.strip()
        # 將欄位名稱抓出
        parameter_name = parameter.split(' ')[0]
        # 將錯誤欄位排除 含有左右括號
        if '(' in parameter_name or ')' in parameter_name:
            continue
        # 去除頓點
        parameter_name = remove_backticks(parameter_name)
        # 將欄位型態抓出
        parameter_type = parameter.split(' ')[1]
        # 去除括號後面的內容
        parameter_type = parameter_type.split('(')[0]
        #print(parameter_name, parameter_type)
        fields.append(FieldInfo(parameter_name, covert_type(parameter_type)))
    return TableInfo(table_name, fields)


def covert_type(parameter_type):
    if parameter_type == 'bigint':
        return 'long'
    elif parameter_type == 'varchar':
        return 'String'
    elif parameter_type == 'decimal':
        return 'BigDecimal'
    elif parameter_type == 'datetime':
        return 'String'
    elif parameter_type == 'int':
        return 'int'
    elif parameter_type == 'tinyint':
        return 'boolean'
    elif parameter_type == 'text':
        return 'String'
    elif parameter_type == 'smallint':
        return 'int'
    else:
        raise Exception('unknown type: ' + parameter_type)


def covert_naming_rule(parameter_name, capital=False):
    # 分隔線轉駝峰
    if '_' in parameter_name:
        parameter_name = parameter_name.replace('_', ' ')
        parameter_name = parameter_name.title()
        parameter_name = parameter_name.replace(' ', '')
        # 首字大寫
        if not capital:
            parameter_name = parameter_name[0].lower() + parameter_name[1:]
    return parameter_name


def find_auto_increment(sql_content):
    # 將每個sql語句抓出 (以ALTER TABLE跟AUTO_INCREMENT;分隔)
    match_pattern = re.compile(r'ALTER TABLE `[^`]+` MODIFY `[^`]+`[^;]+;', re.DOTALL)
    try:
        match_result = match_pattern.findall(sql_content)
        auto_fields = []
        for match in match_result:
            # 第三個是table name
            table_name = match.split(' ')[2]
            # 第五個是欄位名稱
            field_name = match.split(' ')[4]
            # 去除頓點
            auto_fields.append(AutoField(remove_backticks(table_name), remove_backticks(field_name)))
        return auto_fields
    except TypeError as e:
        print('no auto increment')
        return []


def remove_comments(lines):
    cleaned_lines = []
    for line in lines:
        if not line.strip().startswith('--') and not line.strip().startswith('/*'):
            cleaned_lines.append(line)
    return cleaned_lines


def build_java_entity(tables, saved_path, package_name):

    # 如果package name不是entity結尾就加上
    if not package_name.endswith('.entity'):
        package_name += '.entity'
    # 根據package name建立資料夾
    package_name = package_name.replace('.', '/')
    saved_path += package_name + '/'
    # 如果沒有資料夾就建立
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    # 根據table name建立java entity file
    for table in tables:
        file_name = covert_naming_rule(table.name, True) + '.java'
        file_name = saved_path + file_name
        with open(file_name, 'w') as file:
            # 寫入package name
            file.write('package ' + package_name + ';\n')
            file.write('import lombok.Data;\n')
            file.write('import javax.persistence.*;\n')
            if 'BigDecimal' in [field.field_type for field in table.fields]:
                file.write('import java.math.BigDecimal;\n')
            file.write('\n')
            file.write('@Data\n')
            file.write('@Entity\n')
            file.write('@Table(name = "' + table.name + '")\n')
            file.write('public class ' + covert_naming_rule(table.name, True) + ' {\n')
            for field in table.fields:
                # 第一個加id
                if field == table.fields[0]:
                    file.write('    @Id\n')
                if field.auto_increment:
                    file.write('    @GeneratedValue(strategy = GenerationType.IDENTITY)\n')
                file.write('    @Column(name = "' + field.name + '")\n')
                file.write('    private ' + field.field_type + ' ' + covert_naming_rule(field.name, False) + ';\n')
            file.write('}\n')
            # 存檔
            file.close()


# 去除頓點
def remove_backticks(text):
    return text.replace('`', '')
