from email.policy import default
from flask import Flask, jsonify,render_template, request,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import sys
from flask_migrate import Migrate
from sqlalchemy import false

load_dotenv()

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("database_details")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = "todos1"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean,nullable=False,default=False)
    
    def __repr__(self):
        return f"<Todo id:{self.id} description:{self.description}>"
    


@app.route('/')
def index():
    return render_template('index.html',data = Todo.query.all())

@app.route('/todos/create', methods=['post'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        # the description above is gotten this way because we would
        # receive a json object which would come in the form of a dictionary
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
        # the body is created to ensure that we get the todo.description
        # before the session is closed. if we return it directly after
        # everything the session would be closed and we won't be able to get it
    except:
        error = True
        db.session.rollback()
        # rollback ensures that if an error occurs it doesn't get saved in
        # our database
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(404)
    else:
        return jsonify(body)    
    

if __name__ == '__main__':
    app.debug = True
    app.run()