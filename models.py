#from app import app, db
from db import db
#with app.app_context():
    #db.create_all()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return f'{self.title} created on {self.date}'
    