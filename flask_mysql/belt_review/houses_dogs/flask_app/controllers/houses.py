from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.house import House
from flask_app.models.dog import Dog

@app.route('/')
def houses():
    return render_template('index.html', houses=House.get_all())

@app.route('/new_house', methods=['POST'])
def new_house():
    House.save(request.form)
    return redirect('/')

@app.route('/new_dog')
def new_dog():
    houses = House.get_all()
    return render_template('new.html', houses=houses)

@app.route('/create_dog', methods=['POST'])
def create_dog():
    Dog.save(request.form)
    return redirect('/')

@app.route('/show_houses/<int:id>')
def show_dogs(id):
    data = {'id' : id}
    dogs = House.get_house_with_dogs(data)
    return render_template('show.html', dogs=dogs)