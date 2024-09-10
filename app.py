# creating a Todo App and performing CRUD operations

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sfdc@localhost:5432/flask_db' 

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'Todo_app'
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno}. {self.title} = {self.date}" 
    
with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def task():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if (title=="" or desc==""):
            return "Enter Todo task's title and description Both !!"
        else:
            new_todo = Todo(title=title, desc=desc)
            db.session.add(new_todo)
            db.session.commit()

    todo_list = Todo.query.all()
    return render_template("home.html", todo_list=todo_list)


@app.route("/delete/<int:sno>")
def delete(sno):
    task = Todo.query.filter_by(sno=sno).first()
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        
        if (title=="" or desc==""):
            return "Enter Todo task's title and description Both !!"
        else:
            task = Todo.query.filter_by(sno=sno).first()
            task.title = title
            task.desc = desc
            db.session.add(task)
            db.session.commit()
            return redirect("/")

    task = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", task=task)

@app.route("/show")
def show():
    tasks = Todo.query.all()
    print(tasks)
    return "all records are shown on the terminal"

if __name__ == "__main__":
    app.run(debug=True)
   