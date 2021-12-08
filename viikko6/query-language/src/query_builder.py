from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query = And):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr))

    def build(self):
        return self.query