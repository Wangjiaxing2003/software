from extension import db
class Deposit(db.Model):
    __tablename__ = 'deposit'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    deposit_time=db.Column(db.Float(255),nullable=False)
    deposit_rate=db.Column(db.Float(255),nullable=False)

    @staticmethod
    def init_db():
        rets = [
            (1,0.25,2.85),
            (2,0.5,3.05),
            (3,1,3.25),
            (4,2,4.15),
            (5,3,4.75),
            (6,5,5.25),
            (7,0,0.5)
        ]
        for ret in rets:
            deposit = Deposit()
            deposit.id=ret[0]
            deposit.deposit_time=ret[1]
            deposit.deposit_rate=ret[2]
            db.session.add(deposit)
        db.session.commit()

class Loan(db.Model):
    __tablename__ = 'loan'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    loan_time=db.Column(db.String(255),nullable=False)
    loan_rate=db.Column(db.Float(255),nullable=False)

    @staticmethod
    def init_db():
        rets = [
            (1,'0.5',5.85),
            (2,'1',6.31),
            (3,'1-3',6.40),
            (4,'3-5',6.65),
            (5,'5',6.80),
        ]
        for ret in rets:
            loan = Loan()
            loan.id=ret[0]
            loan.loan_time=ret[1]
            loan.loan_rate=ret[2]
            db.session.add(loan)
        db.session.commit()

class Cal(db.Model):
    __tablename__ = 'cal'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    exp=db.Column(db.String(255),nullable=False)
    ans=db.Column(db.String(255),nullable=False)


    @staticmethod
    def init_db():
        rets = [
        ]
        for ret in rets:
            cal = Cal()
            cal.id=ret[0]
            cal.exp=ret[1]
            cal.ans=ret[2]
            db.session.add(cal)
        db.session.commit()