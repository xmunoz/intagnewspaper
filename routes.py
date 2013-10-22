from flask import Flask, url_for, redirect, render_template, g, request
from flask.ext.babel import Babel
from src.common import get_index_data, get_article_full

app = Flask(__name__)
babel = Babel(app)

@app.route("/")
def homepage():
    title = "Periodico Intag"
    return render_template("homepage.html", title=title)

@app.route("/archive")
def archive():
    title = "Archive"
    pdfs = get_index_data('PDF')
    body_class = "article-list"
    return render_template("index_page.html", type='pdf', title=title,
            items=pdfs, body_class=body_class)

@app.route("/articles")
@app.route("/articles/<article_alias>")
def articles(article_alias=None):
    if article_alias:
        article = get_article_full(article_alias)
        title = article.title + ' | Periodico Intag'
        return render_template("article_single.html", title=title,
                article=article)
    else:
        articles = get_index_data('Article')
        title = 'Articles'
        return render_template("index_page.html", type='article',
                title=title, items=articles)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def site_down(e):
    return render_template('500.html', error=e), 500

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es'])

if __name__ == "__main__":
    app.run(debug=True)
