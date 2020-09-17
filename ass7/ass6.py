import numpy as np
import pandas as pd

#1
A = np.array([[1, 5, 2, 3], [5, 6, 3, 1], [7, 6, 2, 1]])
b = np.array([A[0]*30000, A[1]*35000, A[2]*40000])
print(A)
print(np.sum(b, axis=0))



#2

a=np.array([[3.0,3.2],[3.5,3.6]])
b=np.array([118.40,135.20])
np.linalg.solve(a,b)

#3

class bankAccounts():
    type = ''

    def __init__(self): 
        self.balance=0        
        print("Welcome to the bank") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print(" You Withdrew:", amount) 
        else: 
            print("Insufficient balance  ") 

    def makeaccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.address = input("Enter the account holder address : ")
        dict = {}
        key = self.accNo
        values = self.name
        dict[key] = values
        print(self.accNo, " ",self.name ," ",self.type, " " ,self.address,"Account created")

    def getAccount(self): 
        dict = {1:'KANNUR',2:'COVAI',3:'CHENNAI'}
        # key = self.accNo
        # values = self.name
        # dict[key] = values
        a=int(input("Enter the account number : "))
        print(dict[a])
        

    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Account Holder Address : ",self.address)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)      
        

    def display(self): 
        print(" Available Balance=",self.balance) 


ch=''

s=bankAccounts()
while ch != 7:
    
    
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. SHOW ACCOUNTDETAILS")
    print("\t6. GET ACCOUNT")
    print("\t7. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input()
   
    
    if ch == '1':
        s.makeaccount()
    elif ch =='2':
        
        s.deposit()
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        s.withdraw()
    elif ch == '4':
        
        s.display()
    elif ch == '5':
        s.showAccount()
    elif ch == '6':    
        s.getAccount()
    elif ch == '7':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
  



