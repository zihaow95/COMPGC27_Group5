from flask import Flask 
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class Annual_Full_2016(db.Model):
	ID = db.Column(db.Integer(), primary_key=True)
	run_date = db.Column(db.String(50))
	reporting_period = db.Column(db.String(50))
	origin_destination_country = db.Column(db.String(50))
	airline_name = db.Column(db.String(50))
	scheduled_charter = db.Column(db.String(50))
	number_flights_matched = db.Column(db.Integer())
	actual_flights_unmatched = db.Column(db.Integer())
	early_to_15_mins_late_percent = db.Column(db.Float())
	flts_16_to_30_mins_late_percent = db.Column(db.Float())
	flts_31_to_60_mins_late_percent = db.Column(db.Float())
	flts_61_to_180_mins_late_percent = db.Column(db.Float())
	fts_181_to_360_mins_late_percent = db.Column(db.Float())
	more_than_360_mins_late_percent = db.Column(db.Float())
	average_delay_mins = db.Column(db.Float())
	planned_flights_unmatched = db.Column(db.Integer())
	previous_year_month_flights_matched = db.Column(db.Integer())
	previous_year_month_early_to_15_mins_late_percent = db.Column(db.Float())
	previous_year_month_average_delay = db.Column(db.Float())

	def  __init__(self, ID):
		self.ID = ID

	def __repr__(self):
		return "<Annual_Full_2016 `{}`".format(self.ID)


@app.route('/')
def home():
	return '<h1>Hello World!</h1>'

if __name__ == '__main__':
	app.run()

























