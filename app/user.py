from flask import Flask, render_template, url_for,redirect, Blueprint, request, flash
from app import models,db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func

user = Blueprint('user', __name__)


@user.route("/",methods=('GET', 'POST'))
def supply():
    G = models.GoodsInfo.query.filter(models.GoodsInfo.DDL >= datetime.utcnow()).all()
    G_amount = models.GoodsInfo.query.filter(models.GoodsInfo.DDL >= datetime.utcnow()).count()
    if request.method == 'POST':
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
        if models.OrderInfo.query.filter_by(userid=1, GoodsID=goodsid, OrderState=0).first():
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
            return render_template('supply.html', amount=G_amount, goods=G)
        newobj = models.OrderInfo(userid=1, GoodsID=goodsid, Goodsname=orders.Goodsname, idcards=idcards, username=name,
                                  address=address, OrderNum=sums, CreateTime=datetime.utcnow(), OrderState=0)
=======
        if models.OrderInfo.query.filter_by(idcards=idcards, GoodsID=goodsid).first():
            flash("该身份证持有者已申领过同类物品，不可重复申领")
            return render_template('supply.html', amount=G_amount, goods=G)
        newobj = models.OrderInfo(userid=1, GoodsID=goodsid, Goodsname=orders.Goodsname, idcards=idcards, username=name, address=address, OrderNum=sums, CreateTime = datetime.utcnow(), OrderState=0)
>>>>>>> d53ea7a016feaafb45a489b717c0152b2a7b08fd
        db.session.add(newobj)
        db.session.commit()
        return render_template('supply.html', amount=G_amount, goods=G)
    return render_template('supply.html', amount=G_amount, goods=G)
    

@user.route("/received", methods=('GET', 'POST'))
def received():
    user_orders = models.OrderInfo.query.filter_by(userid=1, OrderState=3).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1, OrderState=3).count()
    if request.method == 'POST':
        order_id = request.form['order_id']
        order_name = request.form['order_name']
        reason = 0
        if request.form.get('reason1'):
            reason = reason + 1
        if request.form.get('reason2'):
            reason = reason + 1
        if request.form.get('reason3'):
            reason = reason + 1
        if request.form.get('reason4'):
            reason = reason + 1
        if reason==0:
            flash("请至少选择一个投诉内容")
            return render_template('received.html', amount=user_orders_sum, orders=user_orders)
        text = request.form['text']
        if len(text)==0:
            flash("请描述出现的问题，以便我们为您解决")
            return render_template('received.html', amount=user_orders_sum, orders=user_orders)
        if len(text)>20000:
            flash("过长的问题描述，请简要描述")
            return render_template('received.html', amount=user_orders_sum, orders=user_orders)
        newobj = models.Complaint(Orderid=order_id, Goodsname=order_name, Content=text, ComplaintReason=reason,
                                  ComplaintState=0)
        db.session.add(newobj)
        db.session.commit()
        return render_template('received.html', amount=user_orders_sum, orders=user_orders)
    return render_template('received.html', amount=user_orders_sum, orders=user_orders)


@user.route("/can_require",methods=('GET', 'POST'))
def can_require():
    G = models.GoodsInfo.query.filter(models.GoodsInfo.DDL >= datetime.utcnow()).all()
    G_amount = models.GoodsInfo.query.filter(models.GoodsInfo.DDL >= datetime.utcnow()).count()
    if request.method == 'POST':
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
            return render_template('supply.html', amount=G_amount, goods=G)
        newobj = models.OrderInfo(userid=1, GoodsID=goodsid, Goodsname=orders.Goodsname, idcards=idcards, username=name,
                                  address=address, OrderNum=sums, CreateTime=datetime.utcnow(), OrderState=0)
=======
        if models.OrderInfo.query.filter_by(idcards=idcards, GoodsID=goodsid).first():
            flash("该身份证持有者已申领过同类物品，不可重复申领")
            return render_template('supply.html', amount=G_amount, goods=G)
        newobj = models.OrderInfo(userid=1, GoodsID=goodsid, Goodsname=orders.Goodsname, idcards=idcards, username=name, address=address, OrderNum=sums, CreateTime = datetime.utcnow(), OrderState=0)
>>>>>>> d53ea7a016feaafb45a489b717c0152b2a7b08fd
        db.session.add(newobj)
        db.session.commit()
        flash("提交申领成功")
        return render_template('supply.html', amount=G_amount, goods=G)
    return render_template('supply.html', amount=G_amount, goods=G)

@user.route("/required")
def required():
    user_orders = models.OrderInfo.query.filter_by(userid=1).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1).count()
    return render_template('required.html', amount=user_orders_sum, orders=user_orders)

@user.route("/deleteorder/<orderid>", methods=('POST', 'GET'))
def delete(orderid):
    g = models.OrderInfo.query.filter_by(id=orderid).first()
    if g:
        db.session.delete(g)
        db.session.commit()
        flash("取消申领成功")
        return redirect(url_for('user.required'))
    return redirect(url_for('user.required'))

@user.route("/win")
def win():
    user_orders = models.OrderInfo.query.filter_by(userid=1, OrderState=1).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1, OrderState=1).count()
    return render_template('win.html', amount=user_orders_sum, orders=user_orders)


@user.route("/wait_receive", methods=('GET', 'POST'))
def wait_receive():
    user_orders = models.OrderInfo.query.filter_by(userid=1, OrderState=2).all()
    user_orders_sum = models.OrderInfo.query.filter_by(userid=1, OrderState=2).count()
    if request.method == 'POST':
        if request.form['id']:
            order_id = request.form['id']
            order = models.OrderInfo.query.filter_by(id=order_id).first()
            order.OrderState = 4
            order.CancelTime = datetime.utcnow()
            db.session.commit()
            user_orders = models.OrderInfo.query.filter_by(userid=1, OrderState=2).all()
            user_orders_sum = models.OrderInfo.query.filter_by(userid=1, OrderState=2).count()
        else:
            order_id = request.form['-id']
            order = models.OrderInfo.query.filter_by(id=order_id).first()
            order.OrderState = 3
            order.ReceiveTime = datetime.utcnow()
            db.session.commit()
            user_orders = models.OrderInfo.query.filter_by(userid=1, OrderState=2).all()
            user_orders_sum = models.OrderInfo.query.filter_by(userid=1, OrderState=2).count()
        return render_template('wait_receive.html', amount=user_orders_sum, orders=user_orders)
    return render_template('wait_receive.html', amount=user_orders_sum, orders=user_orders)
