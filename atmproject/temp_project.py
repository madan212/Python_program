import re
#import logging
import time
import os
from random import randint
from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__,instance_relative_config=True)
#import pdb
#pdb.set_trace()

#app.config.from_mapping(SECRET_KEY='dev',DATABASE=os.path.join(app.instance_path,'C:/Users/ADMIN/Documents/SQL Server Management Studio/atm1.sql'),)
app.config.from_mapping(SECRET_KEY='dev',DATABASE=os.path.join(app.instance_path,'F:/Program Files/Microsoft SQL Server/MSSQL15.MSSQLSERVER/MSSQL'))

app.config['SQLALCHEMY_ECHO'] = True
#app.config['SQLALCHEMY_DATABASE_URI']="mssql+pyodbc://DESKTOP-URHHJQ5/MyTestDb?driver=SQL+Server?trusted_connection=yes"
app.config['SQLALCHEMY_DATABASE_URI']="mssql+pyodbc://DESKTOP-URHHJQ5/atm4?driver=SQL+Server?trusted_connection=yes"

#app.config['SQLALCHEMY_DATABASE_URI']="mssql+pyodbc://MySQLServerName/MyTestDb?driver=SQL+Server?trusted_connection=yes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s',filename='logfile1.txt')
#logging.debug('start ATM program')
#def __init__(self,pin,withdraw,deposit_amount):
    #self.pin=pin
    #self.withdraw=withdraw
    #self.deposit_amount=deposit_amount


'''def create_app(test_config=None):
    if test_config is None:
    # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
    # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass'''


#class credit(db.Model) :
#    #__tablename__='credit'
#    #id = db.Column('pin', db.Integer, primary_key = False)
#    amount = db.Column(db.Integer)
#    pin = db.Column(db.Integer)



 #   def __init__(self,amount,pin):
 #      ""
 #       self.amount = amount
 #       self.pin = pin

class customer_details(db.Model) :
    id = db.Column( db.Integer,primary_key=True)
    pin = db.Column(db.Integer,unique=True,nullable=False)
    balance = db.Column(db.Integer)
    #credit = db.relationship('customer_details',order_by=customer_details.id,lazy='SELECT',backref=db.backref('credit', lazy=True))

    def __init__(self,pin):
       #self.name = name
       #self.balance =balance
    
       self.pin = pin
       

class credit(db.Model):
    Transaction_idn = db.Column(db.Integer,primary_key=True)
    deposit_amt=db.Column(db.Float)
    #balance= db.Column(db.Integer, db.ForeignKey('customer_details.balance'),nullable=False)
    balance= db.Column(db.Integer, unique=True,nullable=False)
    cus_id= db.Column(db.Integer, db.ForeignKey('customer_details.id'),nullable=False)
    crt_dt = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    #customer_details = db.relationship('credit',order_by=customer_details.id,backref=db.backref('customer_details', lazy=True))
    #customer_details.credit = relationship("credit", order_by = credit.Transaction_idn, back_populates = "customer_details")


    #category = db.relationship('Category',backref=db.backref('posts', lazy=True))

    def __init__(self,deposit_amt,balance,cus_id):
    
        self.deposit_amt=deposit_amt
        self.balance=balance
        self.cus_id=cus_id
        #self.Transaction_idn=Transaction_idn
        #self.id1=id1


class debit(db.Model):
    Transaction_idn = db.Column(db.Integer,primary_key=True)
    withdraw_amt=db.Column(db.Float)
    cus_id= db.Column(db.Integer, db.ForeignKey('customer_details.id'),nullable=False)
    balance= db.Column(db.Integer, unique=True,nullable=False)
    crt_dt = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    
    #customer_details = db.relationship('customer_details',backref=db.backref('debit', lazy=True))
    

    def __init__(self,withdraw_amt,balance,cus_id):
        self.withdraw_amt=withdraw_amt
        self.balance=balance
        self.cus_id=cus_id


    



@app.route('/error')
def error():
    return'<html><body><h>you entered wrong pin</h><a href="http://localhost:5000/login">retry once</a></body></html>'

@app.route('/')
def index():
    return render_template('atm2.html')
class ATM:
    '''welcome to the ATM'''
    
    def __init__(self,balance=0):
        '''credentials of account.'''
        #balance=session.query(customer_details).filter(customer_details.pin==pin)
        self.balance = balance

        
    
    def login(self,pin):
        
        '''Logi credentials for ATM'''
        self.pin = pin
        #self.id = randint(1000,9999)

        #self.pin[self.id] = id

        pin_regex = re.compile(r'^[1-3]+\d{3}$')
        
        searcher_output = pin_regex.search(pin)
        
        return searcher_output
        
       
        
        #if match:
            #return True
        #else:
            #return False

    def getBalance(self):

        "accessing for amount"

        return self.balance
    def getPin(self):

        "waiting for user response"
        import pdb
        pdb.set_trace()
        #self.balance=db.session.query(customer_details).filter(customer_details.pin==self.pin)

        return self.pin

    #@app.route('/withdrawl',methods=['POST','GET'])
    def withdraw(self,amount,bal):

        "aceesing the amount to customer"
        #amt1=credit.query.filter_by(Transaction_idn='1').first()
        #balance=amt1.balance

        self.balance = bal-amount
        
        return self.balance

    #@app.route('/deposit',methods=['POST','GET'])
    def deposit(self,amount):

        "Deposits are accepted"

        self.balance += amount
        return self.balance

    def display(self):

        "providing the final results"
        #db.session.add(customer_details(balance=self.balance))
        ##db.session.commit()
        #import pdb
        #pdb.set_trace()
        #self.balance=db.session.query(customer_details).filter(customer_details.pin==3457)
        
        return self.balance



acc = ATM()

#app.add_url('/login',methods=['POST','GET'])

@app.route('/login',methods=['POST','GET'])
def log_in():
    ''' accessing the credentials'''
    return render_template('atm.html')

@app.route('/menu',methods=['POST','GET'])
def menu():
    if request.method=='GET':
        return render_template('atm3.html')

@app.route('/deposit',methods=['POST','GET'])
def deposit():
    #bal=0
    if request.method=='POST':

        #bal=amount
        res=make_response(render_template('atm4.html'))
        #res.set_cookie('bal',bal)
        return res

@app.route('/withdrawl',methods=['POST','GET'])
def withdrawl():
    #import pdb
    #pdb.set_trace()
    if request.method=='POST':
        #amount==request.form['amount']
        #bal-=amount
        res=make_response(render_template('atm5.html'))
        #res.set_cookie('bal',bal)
        return res
    
@app.route('/verify',methods=['POST','GET'])
def verify():

    for i in range(1,3):
        if request.method=='POST':
            match = ''
            pin = request.form['pin']
            #x=randint(1000,9999)
            #balance=db.session.query(customer_details).filter(customer_details.pin==pin)
            #credentials=customer_details(pin=request.form['pin'],balance=balance,id == id )
            #db.session.add(credentials)
            #db.session.commit()
            mo = acc.login(pin)
            if request.method=='POST':
                import pdb
                pdb.set_trace()
                credentials=customer_details(pin=request.form['pin'])
                if not credentials.pin :
                    return '<html><body><h>invalid wrong pin</h><a href="http://localhost:5000/login">retry once</a></body></html>'
                #else:
                    #y=credentials.id
                    #id=db.session.query(customer_details).filter(customer_details.pin==pin)
                    #id1=customer_details.query.filter_by(pin=request.form['pin']).first()
                    

                #db.session.add(credentials)
                #db.session.commit()

            
    
            try:
                match = mo.group(0)
                time.sleep(0.5)
                return render_template('atm3.html')
        #break
            except AttributeError:
                print("retry once ")
                #logging.debug('something is going to be happening')
            except TypeError:
                print ("Type Error")
                #logging.debug('users problem')
            except e : 
                print("please enter the correct pin.")
                return redirect(url_for('error'))
            if match:
                return redirect(url_for('menu'))
        #logging.debug()
    #finally:
        #print("you can procces")

                #else:
                    #print("Invalid options")

@app.route('/balance/<option>',methods=['POST','GET'])
def balance(option):
    if request.method=='POST':
        while 1:
            
            if option == 'deposit':
                #"For deposit"
                import pdb
                pdb.set_trace()
                amt=int(request.form['amount'])
                #c1=credit(deposit_amt=request.form['amount'])
                #db.session.add(c1)
                #db.session.commit()
                
                
                bal = acc.deposit(amt)
        
                
                x=acc.display()
                #z1=verify()
                z1=acc.getPin()
            
                
                #z=1

                y=customer_details.query.filter_by(pin='3456').first()
                y1=y.id
                #y2=customer_details.query.get(id)
        
    


            

                c1=credit(deposit_amt=amt,balance=x,cus_id=y1)
                db.session.add(c1)
                db.session.commit()
                #c3=customer_details(balance=x)
                #db.session.add(c3)
                #db.session.commit()
                return render_template('atm6.html',x=x)
                #break
            elif option == 'withdrawl':
                #"reading withdraw"
                import pdb
                pdb.set_trace()
                amt=int(request.form['amount'])
                #c2=debit(withraw_amt=request.form['amount'])
                #db.session.add(c2)
                #db.session.commit()
                amt1=credit.query.filter_by(Transaction_idn='1').first()
                bal=amt1.balance
                if amt<bal:
                    amount=amt

                    acc.withdraw(amount,bal)
                    x=acc.display()
                    y=customer_details.query.filter_by(pin='3456').first()
                    y1=y.id
                    c2=debit(withdraw_amt=amount,balance=x,cus_id=y1)
                    #c2=customer_details(balance=x)
                    db.session.add(c2)
                    db.session.commit()

                    return render_template('atm6.html',x=x)
                else:
                    return '<html><body><h>choose correct amount</h1></body></html>'
                #break
                        
            elif option == 'balance':
                "for balance enquiry"
                x=acc.display()
                return render_template('atm6.html',x=x)
                #break
            else:
                exit()
        

        else:
            print("sorry we are unable to process this transaction")

#else:
    #print("you entered wrong pin.")



if __name__=='__main__':
    import pdb
    pdb.set_trace()
    db.create_all()
    app.run(debug=True)


                
             
             
        
