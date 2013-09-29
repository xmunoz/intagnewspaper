import sqlite3
from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def root():
    # return render_template("adios.html")
    return redirect( url_for ("static", filename="content/2012/1/adios.html") )

if __name__ == "__main__":
    app.run(debug=True)