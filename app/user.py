from flask import Flask, render_template, url_for,redirect, Blueprint

user = Blueprint('user', __name__)

@user.route("/")
def supply():
    return render_template('supply.html')

@user.route("/received")
def received():
    return render_template('received.html')

@user.route("/can_require")
def can_require():
    return render_template('supply.html')

@user.route("/required")
def required():
    return render_template('required.html')

@user.route("/norequire")
def norequire():
    return render_template('norequired.html')

@user.route("/win")
def win():
    return render_template('win.html')

@user.route("/wait_receive")
def wait_receive():
    return render_template('wait_receive.html')

