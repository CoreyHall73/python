from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/show_ninjas')
def show_ninjas():
    dojos = Dojo.get_all()
    return render_template('show.html', dojos=dojos)

@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('/new.html', dojos=dojos)

@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/show_ninjas')