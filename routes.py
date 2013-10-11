import sqlite3
from flask import Flask, url_for, redirect, render_template, g

# config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'pw'

app = Flask(__name__)

# connect to db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# initialize db
def init_db():
    with closing (connect_db() ) as db:
        with app.open_resource("schema.sql", mode = "r") as f:
            db.cursor().executescript(f.read())
        db.commit()

# current db connection is stored in "g" object
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, "db", None)
    if db is not None:
        db.close()

###

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/articulos")
def homepage():
    return render_template("homepage.html")

@app.route("/archivo")
def homepage():
    return render_template("homepage.html")

@app.route("/articulos/<int:year>/<int:month>/<title>")
def root(year, month, title):
    # return render_template("adios.html")
    # return redirect( url_for ("static", filename= "content/2012/1/%s" %static_file  )
    # static_file = static_file + ".html"
    filepath = "static/content/%d/%d/%s.html" % (year, month, title)
    return redirect(filepath)
    # return redirect( filepath )

if __name__ == "__main__":
    app.run(debug=True)