from app import db
import uuid


def gen_id():
    return uuid.uuid4().hex[:10]

class GoodsInfo(db.Model):
    __tablename__  = 'GoodsInfo'
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    Goodsname = db.Column(db.String(30))
    OrderLimit = db.Column(db.Integer, nullable=False, unique=True)
    OrderLimitPerPerson = db.Column(db.Integer, nullable=False, unique=True)
    DDL = db.Column(db.Date, nullable=False, unique=True)

    def __repr__(self):
        return '<Goods %r>' % self.GoodsName

class OrderInfo(db.Model):
    __tablename__ = 'OrderInfo'
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id')) # The IDNumber of the applicant
    GoodsID = db.Column(db.String(32), db.ForeignKey('GoodsInfo.id'))
    Goodsname = db.Column(db.String(30))
    OrderNum = db.Column(db.Integer, nullable=False)
    CreateTime = db.Column(db.Date, nullable=False)
    DeliveryTime = db.Column(db.Date, nullable=True)
    ReceiveTime = db.Column(db.Date, nullable=True)
    CancelTime = db.Column(db.Date, nullable=True)
    OrderState = db.Column(db.Integer, nullable=False) # 0:等待抽签; 1:未发货; 2:已发货; 3:已送达; 4:已取消 
    def __repr__(self):
        return '<Goods %r>' % self.id

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    pwd = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    college = db.Column(db.String(30))
    idcard = db.Column(db.String(20))
    address = db.Column(db.String(100))

    def __repr__(self):
        return '<user %r>' % self.id

class admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    pwd = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    province = db.Column(db.String(150), nullable=False)
    auth = db.Column(db.Integer, nullable=False)
    system = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<admin %r>' % self.id

class WareHouse(db.Model):
    __tablename__ = 'WareHouse'
    Goodsname = db.Column(db.String(30), primary_key=True, nullable=False, unique=True)
    number = db.Column(db.Integer, nullable=False, unique=False)
    usage = db.Column(db.String(50), nullable=False) 

    def __repr__(self):
        return '<Goods %r>' % self.Goodsname


class Complaint(db.Model):
    __tablename__ = 'Complaint'
    id = db.Column(db.String(20), default=gen_id, primary_key=True)
    Orderid = db.Column(db.String(32), db.ForeignKey('OrderInfo.id'), nullable=False)
    Goodsname = db.Column(db.String(30))
    Content = db.Column(db.Text, nullable=False)
    ComplaintReason = db.Column(db.Integer, nullable=False) #0: 物流问题; 1: 物资问题
    ComplaintState = db.Column(db.Integer, nullable=False) #0: 未处理; 1: 已处理

    def __repr__(self):
        return '<Complaint %r>' % self.id
