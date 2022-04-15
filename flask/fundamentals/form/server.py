from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form



@app.route('/')
def index():
    return render_template("index.html")


from flask import Flask, render_template, request, redirect # added request
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Here we add two properties to session to store the name and email
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/show')


@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html', name_on_template=session['name'], 
    email_on_template=session['email'])

if __name__ == "__main__":
    app.run(debug=True)

