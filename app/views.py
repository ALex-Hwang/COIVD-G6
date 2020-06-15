from app import app
from .admin import admin
from .user import user
import flask_excel as excel

app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
