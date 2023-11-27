# from typing import Optional

from odmantic import Model,Field,SyncEngine

myengine=SyncEngine()


class UserDatabase(Model):
    name: str
    age: int = Field(ge=18)
    balance:int = 0
    password:int 
    loan_status:bool = False


    def deposit(self,amount):
        self.balance+=amount
        myengine.save(self)
        print(f"New Balance = {self.balance}")
        print(f"You have deposited {amount}")



    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"you have withdrawn the amount.New Balance = {self.balance}")
            myengine.save(self)
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"Name = {self.name}\nAge = {self.age}\nBalance = {self.balance}")
        

    



    
    



    










# myname=input("enter your name");
# myage=int(input("age dalo"));
# myuser=UserDatabase(name=myname,age=myage)

# myengine.save(myuser)


