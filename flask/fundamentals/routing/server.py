from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    return (word * num)

if __name__=="__main__":
    app.run(debug=True)