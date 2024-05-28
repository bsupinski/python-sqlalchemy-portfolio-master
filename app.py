from flask import (  render_template, url_for, request, redirect)
from models import app, db, Project
from datetime import datetime


@app.context_processor
def inject_user():
    projects = Project.query.all()
    return dict(projects=projects)


@app.route("/")
def index():
    
    return render_template('index.html')


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
def detail(id):
    project = Project.query.get_or_404(id)
    skills = project.skills_practiced.split(", ")
    date = datetime.strftime(project.date, "%B %y")
    return render_template('detail.html', project=project, skills=skills, date=date)


@app.route("/projects/<id>/edit", methods=["POST", "GET"])
def editproject(id):
    project = Project.query.get_or_404(id)
    date = project.date.strftime("%Y-%m")
    if request.form:
        project.title = request.form['title']
        date = request.form['date']
        project.skills_practiced = request.form['skills']
        project.project_url = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editprojectform.html', project=project, date=date)


@app.route("/projects/<id>/delete")
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=800, host='127.0.0.1')
    