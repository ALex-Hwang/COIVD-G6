from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
 return render_template('received.html')

from app import models
