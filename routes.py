from flask import Flask, url_for, redirect, render_template, g
from utils.articles import get_all_articles_summary, get_article_full

app = Flask(__name__)

@app.route("/")
def homepage():
    title = "Periodico Intag"
    return render_template("homepage.html", title=title)

@app.route("/articulos")
def articulos():
    articles = get_all_articles_summary()
    return render_template("article_list.html", articles=articles)

@app.route("/archivo")
def archivo():
    title = "Periodico Intag | Archivo"
    archivo = "archivo object"
    return render_template("homepage.html", title=title, archivo=archivo)

@app.route("/articulos/<article_alias>")
def root(article_alias):
    title = "Periodico Intag | " + article_alias
    article = get_article_full(article_alias)
    return render_template("article_single.html", title=title , article=article)

if __name__ == "__main__":
    app.run(debug=True)
