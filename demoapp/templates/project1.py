#import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(level)s-%(message)s', filename='logfile1.txt')
#logging.debug("start atm_function code")
from flask import *
app=Flask(__name__)

@app.route('/error')
def error():
    return'<html><body><h>you entered wrong pin</h><a href="http://localhost:5000/login">retry once</a></body></html>'
@app.route('/')
def index():
    return render_template('atm2.html')
@app.route('/verify',methods=['POST','GET'])
def verify_pin():
    '''This is for credentials'''
    if request.method=='POST':
        pin=request.form['pin']
    
        if pin =='3232':
            return redirect(url_for('menu'))
        else:
            return redirect(url_for('error'))
@app.route('/login',methods=['POST','GET'])
def log_in():
    ''' accessing the credentials'''
    return render_template('atm.html')
        
        
@app.route('/menu',methods=['POST','GET'])
def menu():
    if request.method=='GET':

        '''proccessing is started'''
    #balance = 1000
    #print("Welcome to the atm!")

        return render_template('atm3.html')

@app.route('/deposit',methods=['POST','GET'])
def deposit():
    #bal=0
    if request.method=='GET':

        #bal=amount
        res=make_response(render_template('atm4.html'))
        #res.set_cookie('bal',bal)
        return res
@app.route('/withdrawl',methods=['POST','GET'])
def withdrawl():
    if request.method=='GET':
        #amount==request.form['amount']
        #bal-=amount
        res=make_response(render_template('atm5.html'))
        #res.set_cookie('bal',bal)
        return res
#@app.route('/balance1',methods=['POST','GET'])
def balance1(bal=0):
    #bal=request.cookies.get('balance')
    if request.method=='POST':
        bal=request.cookies.get('bal')
        amount=int(request.form['amount'])
        bal=bal+amount
        resp=make_response(render_template('atm6.html',bal=bal))
        resp.set_cookie('bal',bal)
        return resp
        #return redirect(url_for('balance'))

def balance2(bal=1000):

    if request.method=='POST':
        bal=request.cookies.get('bal')
        amount=int(request.form['amount1'])
        bal=bal-amount
        return bal
@app.route('/balance',methods=["POST","GET"])
def balance(bal=1000):
    if request.method=='POST':
        if deposit:
            bal=balance1()
            resp=make_response(render_template('atm6.html',bal=bal))
            resp.set_cookie('bal',bal)
            return resp
    
        elif withdrawl:
            bal=balance2()
            resp=make_response(render_template('atm8.html',bal=bal))
            resp.set_cookie('bal',bal)
            return resp
        elif balance:
            bal=request.cookies.get('bal')
            return render_template('atm6.html',bal=bal)
    

        #return resp
    

 
        
        

if __name__=='__main__':
    app.run(debug=True)


    
