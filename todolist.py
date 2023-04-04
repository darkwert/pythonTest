from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
with app.app_context():
    db = SQLAlchemy(app)

class toDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128),nullable=False)
    detail = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default = datetime.now)

    def __repr__(self):
        return '<Task %r>' %self.id

@app.route('/',methods=[ 'POST','GET'])
def index():
    if request.method == 'POST':
        task_title = request.form['title']
        task_detail = request.form['detail']
        new_task = toDoList(title=task_title,detail=task_detail)
        try:
            db.session.add(new_task)
            db.session.commit() 
            return redirect('/')
        except :
            return 'Issue adding your task'
    else:
        tasks = toDoList.query.order_by(toDoList.date_created).all()
        return render_template('index.html',tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = toDoList.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except :
        return 'have problem deleting'

@app.route('/update/<int:id>',methods=[ 'GET','POST'])
def update(id):
    task = toDoList.query.get_or_404(id)
    if request.method == 'POST':
        task.title =request.form['title']
        task.detail =request.form['detail']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'have problem Updating'
    else:
        return render_template('update.html',task = task)
if __name__ == "__main__":
    app.run(debug=True)