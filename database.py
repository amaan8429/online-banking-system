
from odmantic import Model,Field,SyncEngine
from transaction_history import transaction_history_func

myengine=SyncEngine()


class UserDatabase(Model):
    name: str
    age: int = Field(ge=18)
    balance:int = 0
    password:int 
    loan_status:bool = False
    email:str
    transaction_history:list = []

    def deposit(self,amount):
        prev_bal=self.balance
        self.balance+=amount
        new_bal=self.balance
        myengine.save(self)
        print(f"New Balance = {self.balance}")
        print(f"You have deposited {amount}")
        return prev_bal,new_bal


    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"you have withdrawn the amount.New Balance = {self.balance}")
            myengine.save(self)
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"Name = {self.name}\nAge = {self.age}\nBalance = {self.balance}")

    def transactions(self,rs):
        self.transaction_history.insert(0,rs)
        myengine.save(self)

    def print_transactions(self):
        print(self.transaction_history)

    def transfer_funds(self,new_data):
        if new_data is not None:
            (a1,a2),friend=new_data
            self.balance = int(a1)
            friend.balance = int(a2)
            myengine.save(self)
            myengine.save(friend)



    
        

    



    
    



    










# myname=input("enter your name");
# myage=int(input("age dalo"));
# myuser=UserDatabase(name=myname,age=myage)

# myengine.save(myuser)


