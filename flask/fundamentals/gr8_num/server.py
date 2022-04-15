from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
import random

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def user_guess():
    session['guess'] = int(request.form['guess'])
    if session['guess'] < session['num']:
        return redirect('/low')
    elif session['guess'] > session['num']:
        return redirect('/high')
    else:
        return redirect('/win')

@app.route('/low')
def low():
    return render_template('low.html')

@app.route('/high')
def high():
    return render_template('high.html')

@app.route('/win')
def win():
    return render_template('win.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)