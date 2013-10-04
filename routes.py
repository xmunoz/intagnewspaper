import sqlite3
from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/<int:year>/<int:month>/<title>")
def root(year, month, title):
    # return render_template("adios.html")
    # return redirect( url_for ("static", filename= "content/2012/1/%s" %static_file  )
    # static_file = static_file + ".html"
    filepath = "static/content/%d/%d/%s.html" % (year, month, title)
    return redirect(filepath)
    # return redirect( filepath )

if __name__ == "__main__":
    app.run(debug=True)