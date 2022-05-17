from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # instantiating the application
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1111@localhost:5432/myordersystemdb"
# the format for the database uri is as seen below
# Dialect://username:password@url:port/database_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = "persons"  # this line gives the name to our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        """this method is created to help us modify the output of 
        our query. it helps during debuging
        """
        return f"<person| id:{self.id}, name:{self.name}"
    
# clinton = Person(id=1,name="clinton")
# db.session.add(clinton)
# db.session.commit()

# the lines of code commented out just above this were
# used to insert values into the persons table of the database
# they are commented out to avoid getting error for trying to 
# insert duplicate values into the table.
# if its the first time running this script please undo the comment.

db.create_all()
# this ensures the database is created


person = Person.query.first()


@app.route('/')
def index():
    return "Hello " + person.name

if __name__ == '__main__':
    app.run()