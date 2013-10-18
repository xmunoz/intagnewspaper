from flask import Flask, url_for, redirect, render_template, g
from utils.articles import get_all_articles_summary, get_article_full
from utils.pdfs import get_all_pdfs

app = Flask(__name__)

@app.route("/")
def homepage():
    title = "Periodico Intag"
    return render_template("homepage.html", title=title)

@app.route("/articulos")
def articulos():
    articles = get_all_articles_summary()
    title = 'Articulos | Periodico Intag'
    return render_template("article_list.html", title=title,
            articles=articles)

@app.route("/archivo")
def archivo():
    title = "Archivo | Periodico Intag"
    pdf_archive = get_all_pdfs()
    return render_template("archivo.html", title=title,
            pdfs=pdf_archive)

@app.route("/articulos/<article_alias>")
def single_article(article_alias):
    article = get_article_full(article_alias)
    title = article.title + ' | Periodico Intag'
    return render_template("article_single.html", title=title,
            article=article)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def site_down(e):
    return render_template('500.html', error=e), 500

if __name__ == "__main__":
    app.run(debug=True)
