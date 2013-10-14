import sqlite3
from flask import Flask, url_for, redirect, render_template, g

# config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'pw'

app = Flask(__name__)

@app.route("/")
def homepage():
    title = "Periodico Intag"
    return render_template("homepage.html", title = title)

@app.route("/articulos")
def articulos():
    title = "Periodico Intag | Articulos"
    articles = "articles object"
    return render_template("article_list.html", title = title, articles = articles)

@app.route("/archivo")
def archivo():
    title = "Periodico Intag | Archivo"
    archivo = "archivo object"
    return render_template("homepage.html", title = title, archivo = archivo)

@app.route("/articulos/<article_title>")
def root(article_title):
    title = "Periodico Intag | " + article_title
    article = "article object"
    return render_template("article_single.html", title = title , article = article)

if __name__ == "__main__":
    app.run(debug=True)