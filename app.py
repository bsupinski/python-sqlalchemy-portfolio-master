from flask import (  render_template, url_for, request, redirect)
from models import app, db, Project
from datetime import datetime




@app.route("/")
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects/new", methods=["GET", "POST"])
def addprojects():
    if request.form:
        new_project = Project(
            title=request.form['title'],
            date=datetime.strptime(request.form['date'], '%Y-%m'),
            description=request.form['desc'],
            skills_practiced=request.form['skills'],
            project_url=request.form['github'],
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
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
    