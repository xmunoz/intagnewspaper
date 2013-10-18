from flask import Flask, url_for, redirect, render_template, g
from utils.common import get_index_data, get_article_full

app = Flask(__name__)

@app.route("/")
def homepage():
    title = "Periodico Intag"
    return render_template("homepage.html", title=title)

@app.route("/articulos")
def articulos():
    articles = get_index_data('Article')
    title = 'Articulos'
    return render_template("index_page.html", type='article',
            title=title, items=articles)

@app.route("/archivo")
def archivo():
    title = "Archivo"
    pdfs = get_index_data('PDF')
    return render_template("index_page.html", type='pdf', title=title,
            items=pdfs)

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
