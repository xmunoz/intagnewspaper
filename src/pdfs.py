
class PDF:
    '''
    Pdf object.
    '''
    def __init__(self, issue):
        self.issue = issue

    def load_index_data(self, db):
        c = db.cursor()
        c.execute("SELECT headline, filename, thumbnail, date FROM pdfs WHERE issue_number = %d;" % self.issue)
        result = c.fetchone()
        self.headline = result[0]
        self.filename = result[1]
        self.thumbnail_filename = result[2]
        self.date = result[3]
        c.close()


