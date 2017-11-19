from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired

class UserForm(Form):
    username = StringField('Input your username', validators=[DataRequired()])
    flight_date = StringField('Input your flight date', validators=[DataRequired()])
    target_airport = StringField('Input your preference airport', validators=[DataRequired()])
    target_country = StringField('Input your target country', validators=[DataRequired()])
    destination = StringField('Input your target destination', validators=[DataRequired()])
    airline_name = StringField('Input your preference airline', validators=[DataRequired()])

    submit = SubmitField('Submit')
