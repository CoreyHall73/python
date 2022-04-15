from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/2')
def up2():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 2
    return render_template("index.html")

@app.route('/d')
def down():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] -= 1
    return render_template("index.html")


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)