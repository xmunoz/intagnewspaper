#! /usr/bin/env python

from articles import Article
from pdfs import PDF
from MySQLdb import connect
from pprint import pprint

def get_db():
    '''
    Return db object.
    '''
    db = connect(host="localhost", db="intagdb", user='intag', read_default_file="/home/intag/.my.cnf")
    db.set_character_set('utf8')
    return db

def table_and_pk_lookup(class_name):
    classes = {
        'Article':
            {'table': 'articles',
            'pk':'alias'},
        'PDF':
            {'table': 'pdfs',
            'pk':'issue_number'},
        }
    #TODO: error handling here.
    return classes[class_name]['table'], classes[class_name]['pk']


def get_index_data(object_type):
    '''
    Return all object summary data for index page.
    '''
    db = get_db()
    c = db.cursor()
    table, primary_key = table_and_pk_lookup(object_type)
    c.execute("SELECT %s FROM %s;" % (primary_key, table))
    keys = [k[0] for k in c.fetchall()]
    c.close()

    objects_by_year = {}

    for key in keys:
        ob = eval(object_type)(key)
        ob.load_index_data(db)
        if ob.date.year in objects_by_year.keys():
            objects_by_year[ob.date.year].append(ob)
        else:
            objects_by_year[ob.date.year] = [ob]

    db.commit()
    return objects_by_year


def get_article_full(alias):
    '''
    Return full article contents.
    '''
    db = get_db()
    article = Article(alias)
    article.load_all_data(db)
    db.commit()
    return article

def main():
    pprint(get_index_data('Article'))

if __name__ == '__main__':
    main()
