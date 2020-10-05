
class Article:
    '''
    Article object.
    '''
    def __init__(self, alias):
        self.alias = alias

    def load_index_data(self, db):
        c = db.cursor()
        c.execute("SELECT title, author, date, intro FROM articles WHERE alias LIKE '%s';" % self.alias)
        result = c.fetchone()
        self.title = result[0]
        self.author =result[1]
        self.date = result[2]
        self.intro = result[3]
        c.close()

    def load_all_data(self, db):
        self.load_index_data(db)
        c = db.cursor()
        c.execute("SELECT body FROM articles WHERE alias LIKE '%s';" % self.alias)
        result = c.fetchone()
        self.body = result[0]
        c.close()

