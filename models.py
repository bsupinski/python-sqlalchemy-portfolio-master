from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
