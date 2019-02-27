import os
import datetime
import random
import requests
from flask import Flask, render_template, request
from flask_migrate import Migrate

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
migrate=Migrate(app,db)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'
        
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port='8080',debug=True)