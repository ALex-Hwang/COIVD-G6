from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '123456'
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def test():
    return render_template('supply.html')

from app import models, views
