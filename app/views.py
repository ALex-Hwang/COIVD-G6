from . import app
from .admin import admin
from .user import user
import flask_excel as excel

app.register_blueprint(goods_admin,url_prefix='/goods_admin')
app.register_blueprint(goods_user, url_prefix='/goods_user')
