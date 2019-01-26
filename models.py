# models.py 
 
from app import db
 
 
class Company(db.Model):
    __tablename__ = "companies"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
 
    def __init__(self, name):
        """"""
        self.name = name
 
    def __repr__(self):
        return "<Company: {}>".format(self.name)
 
 
class Stats(db.Model):
    """"""
    __tablename__ = "stats"
 
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String)
    board = db.Column(db.Integer)
 
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    company = db.relationship("Company", backref=db.backref(
        "companies", order_by=id), lazy=True)
 
    def __init__(self, ticker, board):
        """"""
        self.ticker = ticker
        self.board = board