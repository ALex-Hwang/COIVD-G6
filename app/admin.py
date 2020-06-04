from flask import Flask, render_template, url_for,redirect, Blueprint

admin = Blueprint('admin', __name__)


@admin.route("/")
def adminfirst():
    return render_template('admin_open.html')

@admin.route("/admin_open")
def admin_open():
    return render_template('admin_open.html')

@admin.route("/view_win")
def view_win():
    return render_template('view_win.html')

@admin.route("/complain_deal")
def complain_deal():
    return render_template('complain_deal.html')

@admin.route("/putin")
def putin():
    return render_template('putin.html')

@admin.route("/sent_deal")
def sent_deal():
    return render_template('sent_deal.html')

