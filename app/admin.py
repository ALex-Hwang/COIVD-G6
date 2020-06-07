from flask import Flask, render_template, url_for,redirect, Blueprint, request, flash
from app import db
from app.models import WareHouse
from app.models import GoodsInfo

admin = Blueprint('admin', __name__)


@admin.route("/")
def adminfirst():
    return render_template('admin_open.html')


@admin.route("/admin_open", methods=('GET', 'POST'))
def admin_open():
    goods = WareHouse.query.all();
    if request.method=='POST':
        number = request.form['number']
        goodsname = request.form['goodsname']
        deadline = request.form['deadline']
        newObj = GoodsInfo(Goodsname=goodsname, OrderLimit=number, DDL=deadline)
        db.session.add(newObj)
        db.session.commit()
        return render_template('admin_open.html', goods=goods)
    return render_template('admin_open.html', goods=goods)

@admin.route("/view_win")
def view_win():
    goods = GoodsInfo.query.all();
    return render_template('view_win.html', goods=goods)

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
    db.session.delete(g)
    db.session.commit()
    flash("删除成功")
    return redirect(url_for('admin.view_win'))


@admin.route("/complain_deal")
def complain_deal():
    return render_template('complain_deal.html')

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
    return render_template('putin.html')

@admin.route("/sent_deal")
def sent_deal():
    return render_template('sent_deal.html')

