import re
#import logging
import time
import os
from random import randint
from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__,instance_relative_config=True)
#connecting db using mssql
app.config.from_mapping(SECRET_KEY='dev',DATABASE=os.path.join(app.instance_path,'C:/Users/ADMIN/Documents/SQL Server Management Studio/atm1.sql'),)
app.config['SQLALCHEMY_DATABASE_URI']="mssql+pyodbc://MySQLServerName/MyTestDb?driver=SQL+Server?trusted_connection=yes"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s',filename='logfile1.txt')
#logging.debug('start ATM program')
#def __init__(self,pin,withdraw,deposit_amount):
    #self.pin=pin
    #self.withdraw=withdraw
    #self.deposit_amount=deposit_amount

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
        #self.customer_id = randint(1000,9999)

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

        return self.id

    #@app.route('/withdrawl',methods=['POST','GET'])
    def withdraw(self,amount):

        "aceesing the amount to customer"

        self.balance -= amount
        
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
            '''credentials=customer_details(pin=request.form['pin'])
            db.session.add(credentials)
            db.session.commit()'''
            mo = acc.login(pin)
            
    
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
                amount=int(request.form['amount'])
                '''c1=credit(amount=request.form['amount'])
                db.session.add(c1)
                db.session.commit()
                acc.deposit(amount)'''
                
                x=acc.display()
                c1=customer_details(balance=x)
                #db.session.add(c1)
                #db.session.commit()
                return render_template('atm6.html',x=x)
                #break
            elif option == 'withdrawl':
                #"reading withdraw"
                amt=int(request.form['amount'])
                c2=debit(amont=request.form['amount'])
                db.session.add(c2)
                db.session.commit()
                if amt<acc.balance:
                    acc.withdraw(amt)
                    x=acc.display()
                    '''c2=customer_details(balance=x)
                    db.session.add(c2)
                    db.session.commit()'''

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
    db.create_all()
    app.run(debug=True)


                
             
             
        
