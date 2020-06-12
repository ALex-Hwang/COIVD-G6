from flask import Flask, render_template, url_for,redirect, Blueprint, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '123456'
db = SQLAlchemy(app)


from app import models, views

@app.route('/', methods=['GET', 'POST'])
def test():
    G = models.GoodsInfo.query.all()
    G_amount = models.GoodsInfo.query.count()
    O = models.WareHouse.query.all()
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
        newobj = models.OrderInfo(userid=1, GoodsID=goodsid, Goodsname=orders.Goodsname, idcards=idcards, username=name, address=address, OrderNum=sums, CreateTime = datetime.utcnow(), OrderState=0)
        db.session.add(newobj)
        orders.OrderLimit -= int(sums)
        db.session.commit()
        return render_template('supply.html', amount=G_amount, goods=G)
    return render_template('supply.html', amount=G_amount, goods=G)
