from flask import Flask, render_template, session, redirect, url_for, flash
import flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from pokemon_query import validName, queryPokemon, radar
from nn import prediction, predict_wins, sorted_win_rate, plot_win_rate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# class NameForm(Form):
#     name = StringField('What is your name?', validators=[Required()])
#     submit = SubmitField('Submit')

class QPk1Form(Form):
    name = StringField('', validators=[Required()])
    submit1 = SubmitField('Query')
    add1 = SubmitField('Add')
    del1 = SubmitField("Delete")


class QPk2Form(Form):
    name = StringField('', validators=[Required()])
    submit2 = SubmitField('Query')
    add2 = SubmitField('Add')
    del2 = SubmitField("Delete")

class QPk3Form(Form):
    name = StringField('', validators=[Required()])
    submit3 = SubmitField('Query')
    add3 = SubmitField('Add')
    del3 = SubmitField("Delete")

class QPk4Form(Form):
    name = StringField('', validators=[Required()])
    submit4 = SubmitField('Query')
    add4 = SubmitField('Add')
    del4 = SubmitField("Delete")

class QPk5Form(Form):
    name = StringField('', validators=[Required()])
    submit5 = SubmitField('Query')
    add5 = SubmitField('Add')
    del5 = SubmitField("Delete")

class QPk6Form(Form):
    name = StringField('', validators=[Required()])
    submit6 = SubmitField('Query')
    add6 = SubmitField('Add')
    del6 = SubmitField("Delete")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = QPk1Form()
    form2 = QPk2Form()
    form3 = QPk3Form()
    form4 = QPk4Form()
    form5 = QPk5Form()
    form6 = QPk6Form()

    if form1.submit1.data and form1.validate_on_submit():
        pokemon_name = form1.name.data
        name = validName(pokemon_name)
        if name != 0:
            pk1_info = queryPokemon(name)
            session['pokemonName1'] = name
            session['pk1'] = pk1_info
            radar(pk1_info, 'pk1_radar')
            return redirect(url_for('index'))
        else:
            flash(u'Please enter the correct name', 'error')
            return redirect(url_for('index'))
    if form2.submit2.data and form2.validate_on_submit():
        pokemon_name = form2.name.data
        name = validName(pokemon_name)
        if name != 0:
            pk2_info = queryPokemon(name)
            session['pokemonName2'] = name
            session['pk2'] = pk2_info
            radar(pk2_info, 'pk2_radar')
            return redirect(url_for('index'))
        else:
            flash('Please enter the correct name', 'error')
            return redirect(url_for('index'))
    if form3.submit3.data and form3.validate_on_submit():
        pokemon_name = form3.name.data
        name = validName(pokemon_name)
        if name != 0:
            pk3_info = queryPokemon(name)
            session['pokemonName3'] = name
            session['pk3'] = pk3_info
            radar(pk3_info, 'pk3_radar')
            return redirect(url_for('index'))
        else:
            flash('Please enter the correct name', 'error')
            return redirect(url_for('index'))
    if form4.submit4.data and form4.validate_on_submit():
        pokemon_name = form4.name.data
        name = validName(pokemon_name)
        if name != 0:
            pk4_info = queryPokemon(name)
            session['pokemonName4'] = name
            session['pk4'] = pk4_info
            radar(pk4_info, 'pk4_radar')
            return redirect(url_for('index'))
        else:
            flash('Please enter the correct name', 'error')
            return redirect(url_for('index'))
    if form5.submit5.data and form5.validate_on_submit():
        pokemon_name = form5.name.data
        name = validName(pokemon_name)
        if name != 0:
            pk5_info = queryPokemon(name)
            session['pokemonName5'] = name
            session['pk5'] = pk5_info
            radar(pk5_info, 'pk5_radar')
            return redirect(url_for('index'))
        else:
            flash('Please enter the correct name', 'error')
            return redirect(url_for('index'))
    if form6.submit6.data and form6.validate_on_submit():
        pokemon_name = form6.name.data
        name = validName(pokemon_name)
        if name != 0:
            pk6_info = queryPokemon(name)
            session['pokemonName6'] = name
            session['pk6'] = pk6_info
            radar(pk6_info, 'pk6_radar')
            return redirect(url_for('index'))
        else:
            flash('Please enter the correct name', 'error')
            return redirect(url_for('index'))

    if form1.add1.data and form1.validate_on_submit():
        flash(u'Success', 'success')
        return redirect(url_for('index'))
    if form2.add2.data and form2.validate_on_submit():
        flash(u'Success', 'success')
        return redirect(url_for('index'))
    if form3.add3.data and form3.validate_on_submit():
        flash(u'Success', 'success')
        return redirect(url_for('index'))
    if form4.add4.data and form4.validate_on_submit():
        flash(u'Success', 'success')
        return redirect(url_for('index'))
    if form5.add5.data and form5.validate_on_submit():
        flash(u'Success', 'success')
        return redirect(url_for('index'))
    if form6.add6.data and form6.validate_on_submit():
        flash(u'Success', 'success')
        return redirect(url_for('index'))

    if form1.del1.data and form1.validate_on_submit():
        session.pop('pk1', None)
        flash(u"'{}' deleted".format(session.get('pokemonName1')), 'info')
        session.pop('pokemonName1', None)
        return redirect(url_for('index'))
    if form2.del2.data and form2.validate_on_submit():
        session.pop('pk2', None)
        flash(u"'{}' deleted".format(session.get('pokemonName2')), 'info')
        session.pop('pokemonName2', None)
        return redirect(url_for('index'))
    if form3.del3.data and form3.validate_on_submit():
        session.pop('pk3', None)
        flash(u"'{}' deleted".format(session.get('pokemonName3')), 'info')
        session.pop('pokemonName3', None)
        return redirect(url_for('index'))
    if form4.del4.data and form4.validate_on_submit():
        session.pop('pk4', None)
        flash(u"'{}' deleted".format(session.get('pokemonName4')), 'info')
        session.pop('pokemonName4', None)
        return redirect(url_for('index'))
    if form5.del5.data and form5.validate_on_submit():
        session.pop('pk5', None)
        flash(u"'{}' deleted".format(session.get('pokemonName5')), 'info')
        session.pop('pokemonName5', None)
        return redirect(url_for('index'))
    if form6.del6.data and form6.validate_on_submit():
        session.pop('pk6', None)
        flash(u"'{}' deleted".format(session.get('pokemonName6')), 'info')
        session.pop('pokemonName6', None)
        return redirect(url_for('index'))

    if flask.request.method == 'POST' and flask.request.form.get('battle', None) == ' ':
        return redirect('simpleresult')

    return render_template('index.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6,
                           name1=session.get('pokemonName1'), name2=session.get('pokemonName2'), name3=session.get('pokemonName3'),
                           name4=session.get('pokemonName4'), name5=session.get('pokemonName5'),name6=session.get('pokemonName6'),
                           pk1_info=session.get('pk1'), pk2_info=session.get('pk2'), pk3_info=session.get('pk3'),
                           pk4_info=session.get('pk4'), pk5_info=session.get('pk5'), pk6_info=session.get('pk6'))


@app.route('/simpleresult', methods=['GET', 'POST'])
def simpleresult():
    predicts = []
    predict1 = prediction(session.get('pk1'), session.get('pk4'))
    predicts.append(predict1)
    if predict1 == 'win':
        winner1 = session.get('pk1')['Name']
    else:
        winner1 = session.get('pk4')['Name']
    predict2 = prediction(session.get('pk2'), session.get('pk5'))
    predicts.append(predict2)
    if predict2 == 'win':
        winner2 = session.get('pk2')['Name']
    else:
        winner2 = session.get('pk5')['Name']
    predict3 = prediction(session.get('pk3'), session.get('pk6'))
    predicts.append(predict3)
    if predict3 == 'win':
        winner3 = session.get('pk3')['Name']
    else:
        winner3 = session.get('pk6')['Name']

    if predicts.count('win') >= 2:
        win_lose = "You win the game!"
    else:
        win_lose = "You lose the game"

    return render_template('simpleresult.html', win_lose=win_lose, winner_1=winner1, winner_2=winner2,winner_3=winner3,
                           pk1_info=session.get('pk1'), pk2_info=session.get('pk2'), pk3_info=session.get('pk3'),
                           pk4_info=session.get('pk4'), pk5_info=session.get('pk5'), pk6_info=session.get('pk6'))

@app.route('/withOrders', methods=['GET', 'POST'])
def withOrders():
    teams, win_rates = predict_wins(session.get('pk1'),session.get('pk2'),session.get('pk3'),
                                    session.get('pk4'),session.get('pk5'),session.get('pk6'))
    teams, win_rates = sorted_win_rate(teams, win_rates)
    session['team_orders'] = teams
    session['win_rates'] = win_rates
    plot_win_rate(win_rates)

    return render_template('withOrders.html', team_orders=session.get('team_orders'), win_rates=session.get('win_rates'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4501)
    # manager.run()
