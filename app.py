from asyncio import tasks
import os
from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
Bootstrap(app)

# database setup.
basedir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'todo.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


 
    

# routes and handlers.


@app.route('/', methods=['GET', 'POST'])
def index():
    """root route"""
    if request.method == 'POST':
        # codigo original
        # task = Task(description=request.form['description'])
        task = Task()
        task.description = request.form['description']
        task.time_estimated = request.form['time_estimated']
        task.category = request.form['category']
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/')
        except:
            return "Houve um erro, ao inserir a tarefa"
        
    else:
        tasks = Task.query.order_by(Task.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    """delete a task"""
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "Houve um erro, ao inserir a tarefa"


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    """update route"""
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.description = request.form['description']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Houve um erro, ao atualizar a tarefa"
    else:
        return render_template('update.html', task=task)
    
    

@app.route('/start/<int:id>')
def start(id):
    """start route"""
    task = Task.query.get_or_404(id)
    task.status = "Doing"
    task.date_doing = datetime.now()
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "Houve um erro, ao atualizar a tarefa"
    
@app.route('/done/<int:id>')
def done(id):
    """start route"""
    task = Task.query.get_or_404(id)
    task.status = "Done"
    task.date_done = datetime.now()
    time = task.date_done - task.date_doing
    
    time2 = str(time)
    task.time_spend = time2[0:7]
    
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "Houve um erro, ao atualizar a tarefa"

    