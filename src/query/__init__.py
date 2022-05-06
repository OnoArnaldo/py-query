import typing as _

Criteria = _.TypeVar('Criteria')


class Select:
    def __init__(self):
        self._table_name = ''
        self._limit: int = None
        self._fields = []
        self._where: Criteria = ''

    def __str__(self) -> str:
        fields = ', '.join(self._fields)
        where = str(self._where)
        limit = '' if self._limit is None else f' LIMIT {self._limit}'
        if len(where) != 0:
            where = f' WHERE {where}'
        return f'SELECT {fields} FROM {self._table_name}{where}{limit}'

    @property
    def values(self) -> list:
        return self._where.values

    def from_table(self, table_name: str) -> 'Select':
        self._table_name = table_name
        return self

    def fields(self, *fields: str) -> 'Select':
        self._fields = fields
        return self

    def where(self, criteria: Criteria) -> 'Select':
        self._where = criteria
        return self

    def limit(self, value: int) -> 'Select':
        self._limit = value
        return self


class _Operation:
    operation = ''

    def __init__(self, field_name: str, value: _.Any):
        self.field_name = field_name
        self.value = value

    def __str__(self) -> str:
        return f'{self.field_name} {self.operation} ?'

    @property
    def values(self):
        return [self.value]


class Equals(_Operation):
    operation = '='


class Like(_Operation):
    operation = 'LIKE'


class GreaterThen(_Operation):
    operation = '>'


class GreaterOrEqualThen(_Operation):
    operation = '>='


class LesserThen(_Operation):
    operation = '<'


class LesserOrEqualThen(_Operation):
    operation = '<='


class _Logical:
    operation = ''

    def __init__(self, *criteria: Criteria):
        self.criteria = criteria

    def __str__(self) -> str:
        operation = f' {self.operation} '
        ret = operation.join(str(c) for c in self.criteria)
        return f'({ret})'

    @property
    def values(self):
        ret = []
        for c in self.criteria:
            ret += c.values
        return ret


class Or(_Logical):
    operation = 'OR'


class And(_Logical):
    operation = 'AND'
