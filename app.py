from flask import ( render_template, request, redirect)
from model import db, Project, app





















if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=800, hose='127.0.0.1')