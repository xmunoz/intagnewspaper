#! /usr/bin/env python

from MySQLdb import connect
from pprint import pprint
import os.path, inspect

from app.articles import Article
from app.pdfs import PDF


def get_db():
    """
    Return db object.
    """
    project_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    )
    cnf_file = os.path.join(project_dir, ".my.cnf")
    db = connect(
        host="localhost", db="intagdb", user="intag", read_default_file=cnf_file
    )
    db.set_character_set("utf8")
    return db


def table_and_pk_lookup(class_name):
    classes = {
        "Article": {"table": "articles", "pk": "alias"},
        "PDF": {"table": "pdfs", "pk": "issue_number"},
    }
    # TODO: error handling here.
    return classes[class_name]["table"], classes[class_name]["pk"]


def get_index_data(object_type):
    """
    Return all object summary data for index page.
    """
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

    sort_objects(objects_by_year)

    return objects_by_year


def sort_objects(objects):
    """
    Sort items by date.
    """
    for k, v in objects.iteritems():
        objects[k] = sorted(v, key=lambda x: x.date)


def get_article_full(alias):
    """
    Return full article contents.
    """
    db = get_db()
    article = Article(alias)
    article.load_all_data(db)
    db.commit()
    return article


def main():
    # debugging
    pprint(get_index_data("PDF"))
    pprint(get_index_data("Article"))


if __name__ == "__main__":
    main()
