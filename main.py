
import os

from app import app
from db_setup import init_db, db_session
from forms import CompanySearchForm, StatsForm
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
  else: #show the results
    return render_template("results.html", table=table)
    #return render_template("results.html", results=results)

@app.route("/new_company", methods=["GET", "POST"])
def new_company():
  form = StatsForm(request.form)

  if request.method == "POST" and form.validate():
    stats = Stats()
    save_changes(stats, form, new=True)
    flash("Company created!")
    return redirect("/")
  return render_template("new_company.html", form=form)

def save_changes(stats, form, new=False):
  company = Company()
  company.name = form.company.data

  stats.company = company
  stats.board = form.board.data
  stats.ticker = form.ticker.data #Name
  if new:
    db_session.add(stats)

  db_session.commit()


if __name__ == "__main__": #for debugging
    app.run(debug=True)

