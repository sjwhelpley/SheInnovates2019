from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/companies.db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class companies(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr, pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

@app.route("/")
def home():
	return render_template('main.html', companies = companies.query.all())

if __name__ == "__main__":
	db.create_all()
	app.run(debug = True)