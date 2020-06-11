from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import flask_excel as excel

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '123456'
db = SQLAlchemy(app)


from app import models, views

excel.init_excel(app)
