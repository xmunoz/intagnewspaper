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


def get_all_articles_summary():
    '''
    Return all article summaries.
    '''
    db = get_db()
    c = db.cursor()
    c.execute("SELECT alias FROM articles ORDER BY date;")
    aliases = [a[0] for a in c.fetchall()]
    c.close()

    articles_by_year = {}

    for alias in aliases:
        article = Article(alias)
        article.load_summary_data(db)
        if article.date.year in articles_by_year.keys():
            articles_by_year[article.date.year].append(article)
        else:
            articles_by_year[article.date.year] = [article]

    db.commit()
    return articles_by_year

def get_article_full(alias):
    '''
    Return full article contents.
    '''
    db = get_db()
    article = Article(alias)
    article.load_all_data(db)
    db.commit()
    return article

class Article:
    '''
    Article object.
    '''
    def __init__(self, alias):
        self.alias = alias

    def load_summary_data(self, db):
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
        c = db.cursor()
        c.execute("SELECT title, author, date, intro, body FROM "\
                "articles WHERE alias = %s;",
                self.alias)
        result = c.fetchone()
        self.title = result[0]
        self.author = result[1]
        self.date = result[2]
        self.intro = result[3]
        self.body = result[4]
        c.close()

def main():
    '''
    Poor man's unit test.
    '''
    pprint(get_all_articles_summary())

if __name__ == "__main__":
    main()

