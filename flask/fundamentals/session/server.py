from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    session['form_data'] = request.form['data']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)