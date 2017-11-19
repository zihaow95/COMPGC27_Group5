from flask import render_template, flash
# 导入蓝本 main
from . import main
from .forms import UserForm
from ..models import User
from app import db

# @main.route('/')
# def index():
#     return render_template('index.html')

@main.route('/', methods=["GET", "POST"])
def signin():
    form = UserForm()
    if form is None:
        flash('Please input username and information')
    elif form.validate_on_submit():
        user = User(username=form.username.data,
                    flight_date = form.flight_date.data,
                    target_airport = form.target_airport.data,
                    target_country = form.target_country.data,
                    destination = form.destination.data,
                    airline_name = form.airline_name.data)
        db.session.add(user)
        try:
            db.session.commit()
            flash('Information collected!')
        except:
            db.session.rollback()
            flash('Information collection failed')
    return render_template('index.html', form=form)
