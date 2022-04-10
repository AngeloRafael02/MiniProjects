#requires environment with flask and SQLAlchemy

from flask import Flask, redirect, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model): #delcaring the table/format of the database used
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow) #new todo, date created will be set the the current time

    def __repr__(self): #returns a string when you make a new element
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET']) #CREATE
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task) #adds new task
            db.session.commit() #commits changes
            return redirect('/') # redirected to the main page
        except:
            return 'There was an issue adding your task.' 
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # display all tasks in order of date_created 
        return render_template('index.html', tasks = tasks) # calls tasks from the line up,

@app.route('/delete/<int:id>') #DELETE
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your task.'

@app.route('/update/<int:id>', methods=['POST','GET']) #UPDATE
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task.'
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)