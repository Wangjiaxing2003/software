import requests
from flask import Flask, request
from flask.views import MethodView
from extension import db,cors
from models import Deposit,Loan,Cal
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources=r'/*')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///deposits.sqlite'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///loans.sqlite'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///cals.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
cors.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Deposit.init_db()
    Loan.init_db()
    Cal.init_db()

class DepositApi(MethodView):
    def get(self,deposit_id):
        if not deposit_id:
            deposits: [Deposit] = Deposit.query.all()
            results=[
                {
                    'id':deposit.id,
                    'deposit_time':deposit.deposit_time,
                    'deposit_rate':deposit.deposit_rate,
                }for deposit in deposits
            ]
            return {
                'results':results
            }
        deposit:[Deposit] = Deposit.query.get(deposit_id)
        return {
            'result':{
                'id':deposit.id,
                'deposit_time':deposit.deposit_time,
                'deposit_rate':deposit.deposit_rate
            }
        }
    def post(self):
        form = request.json
        deposit=Deposit()
        deposit.deposit_time=form.get('deposit_time')
        deposit.deposit_rate = form.get('deposit_rate')
        db.session.add(deposit)
        db.session.commit()
        return{
            'status':'success',
            'message':'数据添加成功'
        }
    def delete(self,deposit_id):
        deposit = Deposit.query.get(deposit_id)
        db.session.delete(deposit)
        db.session.commit()
        return{
            'status':'success',
            'message':'数据删除成功'
        }
    def put(self,deposit_id):
        deposit: Deposit = Deposit.query.get(deposit_id)
        deposit.deposit_time=request.json.get('deposit_time')
        deposit.deposit_rate=request.json.get('deposit_rate')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }


class LoanApi(MethodView):
    def get(self,loan_id):
        if not loan_id:
            loans: [Loan] = Loan.query.all()
            results=[
                {
                    'id':loan.id,
                    'loan_time':loan.loan_time,
                    'loan_rate':loan.loan_rate,
                }for loan in loans
            ]
            return {
                'results':results
            }
        loan:[Loan] = Loan.query.get(loan_id)
        return {
            'result':{
                'id':loan.id,
                'loan_time':loan.loan_time,
                'loan_rate':loan.loan_rate
            }
        }
    def post(self):
        form = request.json
        loan=Loan()
        loan.loan_time=form.get('loan_time')
        loan.loan_rate = form.get('loan_rate')
        db.session.add(loan)
        db.session.commit()
        return{
            'status':'success',
            'message':'数据添加成功'
        }
    def delete(self,loan_id):
        loan = Loan.query.get(loan_id)
        db.session.delete(loan)
        db.session.commit()
        return{
            'status':'success',
            'message':'数据删除成功'
        }
    def put(self,loan_id):
        loan: Loan = Loan.query.get(loan_id)
        loan.loan_time=request.json.get('loan_time')
        loan.loan_rate=request.json.get('loan_rate')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }


class CalApi(MethodView):
    def get(self,cal_id):
        if not cal_id:
            cals: [Cal] = Cal.query.all()
            results=[
                {
                    'id':cal.id,
                    'exp':cal.exp,
                    'ans':cal.ans,
                }for cal in cals
            ]
            return {
                'results':results
            }
        cal:[Cal] = Cal.query.order_by(Cal.id.desc()).get(cal_id).limit(10)
        return {
            'result':{
                'id':cal.id,
                'exp':cal.exp,
                'ans':cal.ans
            }
        }
    def post(self):
        form = request.json
        cal=Cal()
        cal.exp=form.get('exp')
        cal.ans = form.get('ans')
        db.session.add(cal)
        db.session.commit()
        return{
            'status':'success',
            'message':'数据添加成功'
        }
    def delete(self,cal_id):
        cal = Cal.query.get(cal_id)
        db.session.delete(cal)
        db.session.commit()
        return{
            'status':'success',
            'message':'数据删除成功'
        }
    def put(self,cal_id):
        cal: Cal = Cal.query.get(cal_id)
        cal.exp=request.json.get('exp')
        cal.ans=request.json.get('ans')
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }


deposit_view = DepositApi.as_view('deposit_api')
app.add_url_rule('/deposits/',defaults={'deposit_id':None},view_func=deposit_view,methods=['GET',])
app.add_url_rule('/deposits/',view_func=deposit_view,methods=['POST',])
app.add_url_rule('/deposits/<int:deposit_id>',view_func=deposit_view,methods=['GET','PUT','DELETE'])

loan_view = LoanApi.as_view('loan_api')
app.add_url_rule('/loans/',defaults={'loan_id':None},view_func=loan_view,methods=['GET',])
app.add_url_rule('/loans/',view_func=loan_view,methods=['POST',])
app.add_url_rule('/loans/<int:loan_id>',view_func=loan_view,methods=['GET','PUT','DELETE'])

cal_view = CalApi.as_view('cal_api')
app.add_url_rule('/cals/',defaults={'cal_id':None},view_func=cal_view,methods=['GET',])
app.add_url_rule('/cals/',view_func=cal_view,methods=['POST',])
app.add_url_rule('/cals/<int:cal_id>',view_func=cal_view,methods=['GET','PUT','DELETE'])

if __name__ == '__main__':
    app.run(debug=True)

