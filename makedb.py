# db_creator.py
 
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///thecompanies.db', echo=True)
Base = declarative_base()
 
 
class Company(Base):
    __tablename__ = "companies"
 
    id = Column(Integer, primary_key=True)
    name = Column(String) # name not ticker

    def __init__(self, name):
        """"""
        self.name = name
 
    def __repr__(self):
        return "<Company: {}>".format(self.name)
 
class Stats(Base):
    """"""
    __tablename__ = "stats"
 
    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    board = Column(Integer)
    #fraud = Column(Boolean)

    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", backref=backref("stats"), order_by=id)
 
    def __init__(self, ticker, board):
        """"""
        self.ticker = ticker
        self.board = board
 
# create tables
Base.metadata.create_all(engine)











