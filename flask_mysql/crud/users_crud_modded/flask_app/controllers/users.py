from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User


@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", users=users)

@app.route('/add')
def add():
    return render_template("create.html")

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/update_user',methods=['POST'])
def update():
    print(request.form)
    User.update(request.form)
    return redirect('/')

@app.route('/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("read(one).html",user=User.get_one(data))

@app.route('/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/')

