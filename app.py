from flask import (  render_template, request, redirect)
from models import db, Project, app




@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects/new")
def addprojects():
    return render_template('projectform.html')


@app.route("/projects/<id>")
def viewproject(id):
    return render_template('detail.html')


@app.route("/projects/<id>/edit")
def editproject(id):
    return render_template('')


@app.route("/projects/<id>/delete")
def deleteproject(id):
    return render_template('index.html')


















if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=800, host='127.0.0.1')