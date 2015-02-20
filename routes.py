from flask import Flask, render_template, request
from flask.ext.babel import Babel, gettext, format_date
from config import LANGUAGES
from src.common import get_index_data, get_article_full

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.route("/")
def homepage():
    title = "Periodico Intag"
    return render_template("homepage.html", title=title)

@app.route("/archive")
def archive():
    title = gettext("Archive")
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
        title = gettext('Articles')
        return render_template("index_page.html", type='article',
                title=title, items=articles)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def site_down(e):
    return render_template('500.html', error=e), 500

@app.template_filter('month')
def format_as_month(value):
    form="MMMM"
    return format_date(value, form).capitalize()

if __name__ == "__main__":
    app.run(debug=True)
