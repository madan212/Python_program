import re
import logging
import time
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s',filename='logfile1.txt')
logging.debug('start ATM program')

class ATM:
    '''welcome to the ATM'''
    
    def __init__(self,balance=0):
        '''credentials of account.'''
        self.balance = balance
        

    def login(self,pin):
        
        '''Logi credentials for ATM'''
        self.pin = pin

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
    def withdraw(self,amount):

        "aceesing the amount to customer"

        self.balance -= amount
    def deposit(self,amount):

        "Deposits are accepted"

        self.balance += amount
    def display(self):

        "providing the final results"
        
        return self.balance



acc = ATM()


for i in range(1,3):
    
    match = ''
    pin = input("Enter the pin: ")
    mo = acc.login(pin)
    
    try:
        match = mo.group(0)
        time.sleep(0.5)
        print("processing")
        #break
    except AttributeError:
        print("retry once ")
        logging.debug('something is going to be happening')
    except TypeError:
        print ("Type Error")
        logging.debug('users problem')
    except e : 
        print("please enter the correct pin.")
        #logging.debug()
    #finally:
        #print("you can procces")


    if match:
        i=0
        while i<3:
            option = None
            print("welcome to the SBI")
            print("""
                Press 1 for deposit
                Press 2 for withdraw
                Press 3 for balance
                Press 4 for exit
                """)
            try:
                option = int(input("enter your option: "))
                print("Access granted")
                #break

            except (ValueError,TypeError,NameError):

                print("use 1,2,3,4 only")
                logging.debug(Exception)
            #except NameError:
                #print("use 1,2,3,4 only")
            except e:
                print("Error",e)
                print("Enter 1,2,3 or 4 only.")
                logging.debug(e)

            #i+=1
            import pdb
            pdb.set_trace()

            if option==1:
                "For deposit"
                acc.deposit(int(input("enter amount for deposit: ")))
                x=acc.display()
                print("After deposit total amount is ",x)
                #break
            elif option == 2:
                "reading withdraw"
                amt=int(input("enter amount for withdraw:"))
                if amt<acc.balance:
                    acc.deposit(amt)
                    x=acc.display()
                    print("After deposit total amount is  ",x)
                else:
                    print("insufficient balance",acc.display())
                #break
                        
            elif option==3:
                "for balance enquiry"
                x=acc.display()
                print("Total balance is ",x)
                #break
            elif option==4:
                exit()
            else:
                print("Invalid options")

            i+=1
        break

else:
    print("sorry we are unable to process this transaction")

#else:
    #print("you entered wrong pin.")


                
             
             
        
