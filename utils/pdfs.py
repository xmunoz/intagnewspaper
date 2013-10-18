#! /usr/bin/emv python

from pprint import pprint
from MySQLdb import connect

def get_db():
    '''
    Return db object.
    '''
    db = connect(host="localhost", db="intagdb", user='intag', read_default_file="/home/intag/.my.cnf")
    db.set_character_set('utf8')
    return db


def get_all_pdfs():
    '''
    Return all pdfs.
    '''
    db = get_db()
    c = db.cursor()
    c.execute("SELECT issue_number FROM pdfs;")
    pdf_issues = [i[0] for i in c.fetchall()]
    c.close()

    pdfs_by_year = {}

    for issue in pdf_issues:
        pdf = PDF(issue)
        pdf.load_data(db)
        if pdf.date.year in pdfs_by_year.keys():
            pdfs_by_year[pdf.date.year].append(pdf)
        else:
            pdfs_by_year[pdf.date.year] = [pdf]

    db.commit()
    return pdfs_by_year

class PDF:
    '''
    Pdf object.
    '''
    def __init__(self, issue):
        self.issue = issue

    def load_data(self, db):
        c = db.cursor()
        c.execute("SELECT headline, filename, thumbnail, date FROM pdfs "\
                "WHERE issue_number = %s;", self.issue)
        result = c.fetchone()
        self.headline = unicode(result[0], "utf8")
        self.filename = result[1]
        self.thumbnail_filename = result[2]
        self.date = result[3]
        c.close()

def main():
    '''
    Poor man's unit test.
    '''
    pprint(get_all_pdfs())

if __name__ == "__main__":
    main()

