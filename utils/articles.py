
class Article:
    '''
    Article object.
    '''
    def __init__(self, alias):
        self.alias = alias

    def load_index_data(self, db):
        c = db.cursor()
        c.execute("SELECT title, author, date, intro FROM articles "\
                "WHERE alias = %s;", self.alias)
        result = c.fetchone()
        self.title = unicode(result[0], "utf8")
        self.author = unicode(result[1], "utf8")
        self.date = result[2]
        self.intro = unicode(result[3], "utf8")
        c.close()

    def load_all_data(self, db):
        self.load_index_data(db)
        c = db.cursor()
        c.execute("SELECT body FROM articles WHERE alias = %s;",
                self.alias)
        result = c.fetchone()
        self.body = unicode(result[0], "utf8")
        c.close()

