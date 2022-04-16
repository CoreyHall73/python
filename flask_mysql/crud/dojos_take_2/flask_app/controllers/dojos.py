from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/show_ninjas/<int:id>')
def show_ninjas(id):
    data = {'id' : id}
    ninjas = Dojo.get_dojo_with_ninjas(data)
    return render_template('show.html', ninjas=ninjas)

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
    return redirect('/')