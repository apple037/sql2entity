class TableInfo:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields


class FieldInfo:
    def __init__(self, name, field_type, auto_increment=False):
        self.name = name
        self.field_type = field_type
        self.auto_increment = False


class AutoField:
    def __init__(self, table_name, field_name):
        self.table_name = table_name
        self.field_name = field_name
