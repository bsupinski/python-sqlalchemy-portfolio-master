from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)


app.config['SQLACLEHMY_DATABASE_URI'] = 'sqlite:///projects.db'


db = SQLAlchemy(app)


class Project(db.mdoel):
    id = db.Column(db.Integer, primary_keyt = True)
    title = db.Column("Title", db.String())
    date = db.Column("Date Created", db.DateTime)
    description = db.Column("Description", db.String())
    skills_practiced = db.Column("Skills", db.String())
    project_url = db.Column("URL", db.String())


def __repr__(self):
    return f'''
    Title: {self.title}
    Date: {self.date}
    Description: {self.description}
    Skills: {self.skills_practiced}
    URL: {self.project_url}
'''
