# Query for sqlite

Build queries for sqlite. This is kind of useful when you need 
to build the query at runtime.


## Installation

```shell
python3.10 -m venv venv
source venv\bin\activate

pip install --upgrade pip
pip install git+https://github.com/OnoArnaldo/py-query.git
```

## Usage

```python
from sqlite3 import Connection
import query as q

query = (q.Select()
         .fields('field1', 'field2')
         .from_table('tablename')
         .where(q.And(
            q.Equals('field1', 900), 
            q.Like('field2', '%value%')
        )))

conn = Connection('data.db')
with conn:
    result = conn.execute(str(query), query.values)
    for row in result:
        print(row)
```
