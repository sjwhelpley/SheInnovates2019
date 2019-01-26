
import os

from app import app
from db_setup import init_db, db_session
from forms import CompanySearchForm
from flask import flash, render_template, request, redirect
from models import Stats
#from flask import Flask, render_template, request, redirect
#from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_TRACK_MODIFICATIONS = False

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
  search = CompanySearchForm(request.form)
  if request.method == "POST":
    return search_results(search)
  return render_template("index.html", form=search)

@app.route("/results")
def search_results(search):
  results = []
  search_string = search.data['search']

  if search.data["search"] == "":
    qry = db_session.query(Stats)
    results = qry.all()
  if not results:
    flash("No results found")
    return redirect("/")
  else:
    return render_template("results.html", results=results)

if __name__ == "__main__": #for debugging
    app.run(debug=True)





