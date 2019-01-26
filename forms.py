# forms.py

from wtforms import Form, StringField, SelectField

class CompanySearchForm(Form):
	choices = [('Company', 'Company'), ('Stats', 'Stats'), ('Board', 'Board')]
	select = SelectField("Search for a company:", choices=choices)
	search = StringField('')