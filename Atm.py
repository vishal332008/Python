
users = {
    "Vishal":25000,
    "James":20000
    }
class Atm:
    def __init__(self,name):
        self.name = users
        self.withdrawedcash = 0
        self.depositedcash = 0 
        self.cash = users.get(name)
            
    def withdraw(self,user):
        print(f"You have {users.get(user)} cash")
        cash1 = int(input("Enter the Cash you want to Withdraw : "))
        self.withdrawedcash = cash1
        self.cash = self.cash - cash1
        users.update({user:self.cash})
        print("Succesfully Withdrawed")
        print(f"Now you have {users.get(user)} cash")
            
    def deposit(self,user):
        print(f"You have {users.get(user)} cash")
        cash1 = int(input("Enter the Cash you want to Deposit : "))
        self.depositedcash = cash1
        self.cash = self.cash + cash1
        users.update({user:self.cash})
        print("Succesfully Deposited")
        print(f"Now you have {users.get(user)} cash")
        
        
name1 = input("Enter your Name : ")
  
atm1 = Atm(name1)

if name1 in users:
    print("TYPE 1 TO WITHDRAW")
    print("TYPE 2 TO DEPOSIT")

    page = int(input())
    
    if (page==1):
        Atm.withdraw(atm1 ,name1)
    elif (page==2):
        Atm.deposit(atm1 ,name1)
    else:
        print("ENTER A VALID NUMBER")
else:
    print("You Are Not Yet Registered")


        