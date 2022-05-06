import query as q


def test():
    query = q.Select()\
        .fields('FLD1', 'FLD2', 'FLD3')\
        .from_table('THE_TABLE')\
        .where(q.And(
            q.Or(q.Equals('FLD1', 100),
                 q.GreaterThen('FLD1', 500),
                 q.LesserThen('FLD1', 50)),
            q.Or(q.Like('FLD3', '%val%'),
                 q.GreaterOrEqualThen('FLD2', 600),
                 q.LesserOrEqualThen('FLD2', 60))
        )).limit(5)

    assert str(query) == ('SELECT FLD1, FLD2, FLD3 '
                          'FROM THE_TABLE '
                          'WHERE ((FLD1 = ? OR FLD1 > ? OR FLD1 < ?) '
                          'AND (FLD3 LIKE ? OR FLD2 >= ? OR FLD2 <= ?)) '
                          'LIMIT 5')

    assert query.values == [100, 500, 50, '%val%', 600, 60]
