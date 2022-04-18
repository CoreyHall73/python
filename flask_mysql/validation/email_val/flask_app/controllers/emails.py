from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def make():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('show.html', emails=Email.get_all())

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {"id": id}
    Email.destroy(data)
    return redirect('/show')