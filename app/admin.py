from flask import Flask, render_template, url_for,redirect, Blueprint, request, flash
from app import db
import time
from app.models import WareHouse
from app.models import GoodsInfo
from app.models import OrderInfo
from app.models import Complaint

admin = Blueprint('admin', __name__)


@admin.route("/")
def adminfirst():
    return render_template('admin/admin_open.html')


@admin.route("/admin_open", methods=('GET', 'POST'))
def admin_open():
    goods = WareHouse.query.filter(WareHouse.number > 0);
    if request.method=='POST':
        Sum = request.form['sum']
        number = request.form['number']
        goodsname = request.form['goodsname']
        deadline = request.form['deadline']
        g = GoodsInfo.query.filter(GoodsInfo.Goodsname==goodsname).first()
        o = WareHouse.query.filter(WareHouse.Goodsname==goodsname).first()
        if int(Sum) > o.number:
            flash("数量大于库存量，请重新输入!")
            return render_template('admin/admin_open.html', goods=goods)
        if int(Sum) < int(number):
            flash("个人申领数量大于可申领总数，请重新输入！")
            return render_template('admin/admin_open.html', goods=goods)
        if g:
            flash("该物资已经发布，添加数量成功！")
            g.OrderLimit += int(Sum)
            o.number -= int(Sum)
            if o.number == 0: # when the number is zero.
                db.session.delete(o)
            db.session.commit()
            return render_template('admin/admin_open.html', goods=goods)
        newObj = GoodsInfo(Goodsname=goodsname, OrderLimit=Sum, OrderLimitPerPerson = number, DDL=deadline)
        db.session.add(newObj)
        o.number -= int(Sum)
        db.session.commit()
        return render_template('admin/admin_open.html', goods=goods)
    return render_template('admin/admin_open.html', goods=goods)

@admin.route("/view_win")
def view_win():
    goods = GoodsInfo.query.all();
    return render_template('admin/view_win.html', goods=goods)

@admin.route("/deleteWare/<goodsname>", methods=('POST', 'GET'))
def delete(goodsname):
    g = GoodsInfo.query.filter(GoodsInfo.Goodsname==goodsname).first()
    if g:
        flash("该物资已经发布，无法删除！", category='warning')
        return redirect(url_for('admin.admin_open'))
    d = WareHouse.query.filter(WareHouse.Goodsname==goodsname).first()
    db.session.delete(d)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for('admin.admin_open'))


@admin.route("/deleteGoodsInfo/<goodsname>", methods=('POST', 'GET'))
def deleteGoodsInfo(goodsname):
    g = GoodsInfo.query.filter(GoodsInfo.Goodsname==goodsname).first()
    p = WareHouse.query.filter(WareHouse.Goodsname==goodsname).first()
    p.number += g.OrderLimit
    db.session.delete(g)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for('admin.view_win'))


@admin.route("/complain_deal") # 投诉处理
def complain_deal():
    complaints = Complaint.query.filter(Complaint.ComplaintState==0)
    return render_template('admin/complain_deal.html', complaints=complaints)

@admin.route("/putin", methods=('GET', 'POST'))
def putin():
    if request.method == 'POST':
        name = request.form['goodsname']
        number = request.form['number']
        usage = request.form['usage']
        
        q_id = WareHouse.query.filter(WareHouse.Goodsname==name).first()
        if not q_id:
            newObj = WareHouse(Goodsname=name, number=number, usage=usage)
            db.session.add(newObj)
            db.session.commit()
            flash('提交成功')
        else:
            q_id.number += number
            db.session.commit()
            flash('该物资存在，已经更新数量')
    return render_template('admin/putin.html')

@admin.route("/sent_deal") # 订单提交成功界面
def sent_deal():
    orders = OrderInfo.query.filter(OrderInfo.OrderState==1)
    return render_template('admin/sent_deal.html', orders=orders)

@admin.route("/sending") # 订单运输中界面
def sending():
    orders = OrderInfo.query.filter(OrderInfo.OrderState==2)
    return render_template('admin/sending.html', orders=orders)

@admin.route("/completed") # 订单完成界面 
def completed():
    orders = OrderInfo.query.filter(OrderInfo.OrderState==3)
    return render_template('admin/completed.html', orders=orders)

@admin.route("/send/<orderid>") # 进行发货操作
def send(orderid):
    order = OrderInfo.query.filter(OrderInfo.id==orderid).first()
    order.OrderState = 2
    order.DeliveryTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db.session.commit()
    return redirect(url_for('admin.sent_deal'))

@admin.route("/processComplaint/<complaintid>") #  处理投诉
def processComplaint(complaintid):
    complaint = Complaint.query.filter(Complaint.id==complaintid).first()
    complaint.ComplaintState = 1
    db.session.commit()
    return redirect(url_for('admin.complain_deal')) 