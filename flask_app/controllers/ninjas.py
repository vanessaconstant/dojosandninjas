from crypt import methods
from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas')
def addNinjaform():

    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', all_dojos=dojos)


@app.route('/processone', methods=['POST'])
def addNinja():

    if (not Ninja.validate_ninja(request.form)):
        return redirect('/ninjas')

    newNinja = {

        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo']
    }

    Ninja.save(newNinja)

    return redirect('/ninjas')
