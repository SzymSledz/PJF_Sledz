from flask import Flask #redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "@$FA@Tzw$t@^BBsehwy23626g"
app.permanent_session_lifetime = timedelta(hours = 2)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)

from pjf.main.routes import main
from pjf.user.routes import user
from pjf.collection.routes import collection
from pjf.practice.routes import practice

app.register_blueprint(user)
app.register_blueprint(main)
app.register_blueprint(collection)
app.register_blueprint(practice)
