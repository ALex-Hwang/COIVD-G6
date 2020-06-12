from flask import Flask, render_template, url_for,redirect, Blueprint, request, flash
from app import models,db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

user = Blueprint('user', __name__)

@user.route("/",methods=('GET', 'POST'))
def supply():
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
    

@user.route("/received", methods=('GET', 'POST'))
def received():
    user_orders = models.OrderInfo.query.filter_by(userid=1,OrderState=3).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1,OrderState=3).count()
    if request.method=='POST':
        order_id = request.form['order_id']
        if models.Complaint.query.filter_by(Orderid=order_id).first():
            flash("该订单已投诉")
            return render_template('received.html', amount=user_orders_sum, orders=user_orders)
        order_name = request.form['order_name']
        reason = 0
        if request.form.get('reason1'):
            reason = reason+1
        reason = reason*2
        if request.form.get('reason2'):
            reason = reason+1
        reason = reason*2
        if request.form.get('reason3'):
            reason = reason+1
        reason = reason*2
        if request.form.get('reason4'):
            reason = reason+1
        text = request.form['text']
        newobj = models.Complaint(Orderid=order_id, Goodsname=order_name, Content=text, ComplaintReason=reason, ComplaintState=0)    
        db.session.add(newobj)
        db.session.commit()
        return render_template('received.html', amount=user_orders_sum, orders=user_orders)
    return render_template('received.html', amount=user_orders_sum, orders=user_orders)


@user.route("/can_require",methods=('GET', 'POST'))
def can_require():
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

@user.route("/required")
def required():
    user_orders = models.OrderInfo.query.filter_by(userid=1).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1).count()
    return render_template('required.html', amount=user_orders_sum, orders=user_orders)

@user.route("/win")
def win():
    user_orders = models.OrderInfo.query.filter_by(userid=1, OrderState=1).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1, OrderState=1).count()
    return render_template('win.html', amount=user_orders_sum, orders=user_orders)

@user.route("/wait_receive", methods=('GET', 'POST'))
def wait_receive():
    user_orders = models.OrderInfo.query.filter_by(userid=1,OrderState=2).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1,OrderState=2).count()
    if request.method=='POST':
        if request.form['id']:
            order_id = request.form['id']
            order = models.OrderInfo.query.filter_by(id=order_id).first()
            order.OrderState = 4
            order.CancelTime = datetime.utcnow()
            db.session.commit()
        else:
            order_id = request.form['-id']
            order = models.OrderInfo.query.filter_by(id=order_id).first()
            order.OrderState = 3
            order.ReceiveTime = datetime.utcnow()
            db.session.commit()
        return render_template('wait_receive.html', amount=user_orders_sum, orders=user_orders)
    return render_template('wait_receive.html', amount=user_orders_sum, orders=user_orders)

