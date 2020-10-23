class Fields:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        value = obj.__dict__.get(self.name)
        if value is None or len(value) == 0:
            return ""
        return ",".join(obj.__dict__.get(self.name))

    def __set__(self, obj, value) -> None:
        if value is None:
            obj.__dict__[self.name] = []
        if isinstance(value, list):
            for item in value:
                obj.__dict__[self.name].append(item)
        if isinstance(value, str):
            obj.__dict__[self.name].append(value)
        if isinstance(value, object):
            raise ValueError(f"expected string or list, type {type(value)} is invalid")


class Conditions:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        value = obj.__dict__.get(self.name)
        if value is None or len(value) == 0:
            return ""
        return ",".join(obj.__dict__.get(self.name))

    def __set__(self, obj, value) -> None:
        if value is None:
            obj.__dict__[self.name] = []
        if isinstance(value, list):
            for item in value:
                obj.__dict__[self.name].append(item)
        if isinstance(value, str):
            obj.__dict__[self.name].append(value)
        if isinstance(value, object):
            raise ValueError(f"expected string or list, type {type(value)} is invalid")


class QueryBuilder:

    def __init__(self):
        self._table = None
        self._where = []
        self._fields = []
        self._order_by = []
        self._limit = None

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, table):
        self._table = table

    @property
    def where(self):
        if len(self._where) == 0:
            return ""
        return f"WHERE {' AND '.join(self._where)}"

    @where.setter
    def where(self, conditions=None):
        if conditions is None:
            self._where = []
        else:
            for condition in conditions:
                self._where.append(condition)

    @property
    def fields(self):
        if len(self._fields) == 0:
            return " * "
        return ",".join(self._fields)

    @fields.setter
    def fields(self, field_names=None):
        if field_names is None:
            self._fields = []
        else:
            for field in field_names:
                self._fields.append(field)

    @property
    def order_by(self):
        if len(self._order_by) == 0:
            return ""
        return f"ORDER BY {' and '.join(self._order_by)}"

    @order_by.setter
    def order_by(self, conditions):
        if conditions is None:
            self._order_by = []
        else:
            for condition in conditions:
                self._order_by.append(condition)

    def limit(self, limit):
        self._limit = limit

    def build(self):
        return f"SELECT {self.fields} FROM {self.table} {self.where} {self.order_by}"


if __name__ == "__main__":
    x = QueryBuilder()
    x.table = "default_table"
    x.fields = ['one', 'two', 'three']
    x.where = ["a==b", "c==d"]
    x.order_by = ["a DESC"]
    print(x.build())
