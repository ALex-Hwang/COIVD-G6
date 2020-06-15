from flask import Flask, render_template, url_for,redirect, Blueprint, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import flask_excel as excel

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '123456'
db = SQLAlchemy(app)
excel.init_excel(app)

from app import models, views

@app.route('/', methods=['GET', 'POST'])
def test():
    G = models.GoodsInfo.query.filter(models.GoodsInfo.DDL >= datetime.utcnow()).all()
    G_amount = models.GoodsInfo.query.filter(models.GoodsInfo.DDL >= datetime.utcnow()).count()
    if request.method=='POST':
        goodsid = request.form['goods_id']
        name = request.form['name']
        idcards = request.form['id']
        address = request.form['address']
        sums = request.form['sum']
        orders = models.GoodsInfo.query.filter_by(id=goodsid).first()
        if orders.OrderLimitPerPerson < int(sums):
            flash("申领数量超过每人限制！")
            return render_template('supply.html', amount=G_amount, goods=G)
        if int(sums) > orders.OrderLimit:
            flash("剩余数量不足！")
            return render_template('supply.html', amount=G_amount, goods=G)
<<<<<<< HEAD
        if models.OrderInfo.query.filter_by(userid=1, GoodsID=goodsid,OrderState=0).first():
            flash("您已申领过该物资，不可重复申领")
            return render_template('supply.html', amount=G_amount, goods=G)
        if not models.user.query.filter_by(id=1, idcard=idcards).first():
            flash("身份证号错误")
            return render_template('supply.html', amount=G_amount, goods=G)
        if not models.user.query.filter_by(id=1, name=name).first():
            flash("姓名错误")
            return render_template('supply.html', amount=G_amount, goods=G)
        if len(address) > 30:
            flash("过长的地址输入！")
            return render_template('supply.html', amount=G_amount, goods=G)
        if int(sums) <= 0:
            flash("申领数量应该为正整数")
=======
        if models.OrderInfo.query.filter_by(idcards=idcards, GoodsID=goodsid).first():
            flash("该身份证持有者已申领过同类物品，不可重复申领")
>>>>>>> d53ea7a016feaafb45a489b717c0152b2a7b08fd
            return render_template('supply.html', amount=G_amount, goods=G)
        newobj = models.OrderInfo(userid=1, GoodsID=goodsid, Goodsname=orders.Goodsname, idcards=idcards, username=name, address=address, OrderNum=sums, CreateTime = datetime.utcnow(), OrderState=0)
        db.session.add(newobj)
        db.session.commit()
        return render_template('supply.html', amount=G_amount, goods=G)
    return render_template('supply.html', amount=G_amount, goods=G)