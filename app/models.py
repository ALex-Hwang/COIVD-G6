from app import db

class GoodsInfo(db.Model):
    __tablename__  = 'GoodsInfo'
    id = db.Column(db.String(10), primary_key=True, nullable=False, unique=True)
    AdminID = db.Column(db.String(18), nullable=False, unique=True)
    GoodsName = db.Column(db.String(30), nullable=False, unique=True)
    GoodsSepc = db.Column(db.String(100), nullable=False, unique=True)
    Stock = db.Column(db.Integer, nullable=False, unique=True)
    OrderLimit = db.Column(db.Integer, nullable=False, unique=True)
    DDL = db.Column(db.Date, nullable=False, unique=True)

    def __repr__(self):
        return '<Goods %r>' % self.GoodsName

class OrderInfo(db.Model):
    __tablename__ = 'OrderInfo'
    id = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    IDNumber = db.Column(db.String(18), primary_key=False, nullable=False, unique=True) # The IDNumber of the applicant
    GoodsID = db.Column(db.String(10), db.ForeignKey('GoodsInfo.id'), unique=True)
    OrderNum = db.Column(db.Integer, nullable=False, unique=True)
    CreateTime = db.Column(db.Date, nullable=False, unique=True)
    OrderToken = db.Column(db.String(8), nullable=False, unique=True)

    def __repr__(self):
        return '<Goods %r>' % self.id

class OrderProcess(db.Model):
    __tablename__ = 'OrderProcess'
    id = db.Column(db.String(20), db.ForeignKey('OrderInfo.id'), nullable=False, primary_key=True)
    IDNumber = db.Column(db.String(18), db.ForeignKey('Admin.id'), nullable=False)
    ProcessTime = db.Column(db.Date, nullable=False)
    DeliveryTime = db.Column(db.Date, nullable=True)
    ReceiveTime = db.Column(db.Date, nullable=True)
    CancelTime = db.Column(db.Date, nullable=True)
    OrderState = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<OrderProcess %r>' % self.id

class Complaint(db.Model):
    __tablename__ = 'Complaint'
    id = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    IDNumber = db.Column(db.String(18), db.ForeignKey('User.id'), nullable=False)
    CreateTime = db.Column(db.Date, nullable=True)
    ComplaintReason = db.Column(db.Integer, nullable=False)
    Content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Complaint %r>' % self.id

class ComplaintProcess(db.Model):
    id = db.Column(db.String(20), db.ForeignKey('Complaint.id'), primary_key=True, nullable=False, unique=True)
    IDNumber = db.Column(db.String(18), db.ForeignKey('Admin.id'), nullable=False)
    ProcessTime = db.Column(db.Date, nullable=False)
    CancelTime = db.Column(db.Date, nullable=True)
    ComplaintState = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<ComplaintProcess %r>' % self.id
