from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, querytype = All()):
        self.querytype = querytype

    def build(self):
        return self.querytype

    def plays_in(self, team):
        return QueryBuilder(And(self.querytype,PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.querytype,HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.querytype,HasFewerThan(value, attr)))

    def one_of(self, m1, m2):
        return QueryBuilder(Or(m1,m2))
