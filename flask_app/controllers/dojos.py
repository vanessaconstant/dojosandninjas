from crypt import methods
from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojo import Dojo


@app.route('/dojos')
def addDojopage():

    dojos = Dojo.get_all_dojos()

    return render_template('dojo.html', all_dojos=dojos)


@app.route('/processtwo', methods=['POST'])
def addDojo():

    if not Dojo.validate_dojo(request.form):
        return redirect('/dojos')
    data = {
        'name': request.form['name']
    }

    Dojo.save(data)

    return redirect('/dojos')


@app.route('/dojos/<id>')
def dojos_and_ninjas(id):

    dojosninjas = Dojo.get_dojos_and_ninjas(id)
    dojo_name = dojosninjas[0]['dojo_name']
    print(dojo_name)

    return render_template('dojosandninjas.html', dojos_with_ninjas=dojosninjas, dojo_name=dojo_name)
