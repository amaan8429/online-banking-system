# from bank import Bank
from database import UserDatabase,myengine 
from email_verfication import ask_the_mail
from password import *


def login():
    my_username=input("enter the nanme you registed  ")
    my_user = myengine.find_one(UserDatabase,UserDatabase.name==my_username)
    if my_user is None:
        print("Invalid UserName,Try Again")
        login()
    else:
         password_check(my_user)


def main():
    choice = int(input("press 1 to login and 2 to sign up  "))
    match choice:
        case 1: 
            login()
        case 2:
            new_name=input("enter your name  ")
            new_age=int(input("enter your age  "))
            final_final_ans,email = ask_the_mail()
            if final_final_ans:
                final_pass = creating_password()
                if isinstance(final_pass,int):
                    new_account = UserDatabase(
                        name=new_name,
                        age=new_age,
                        password=final_pass,
                        email=email
                    )
                    myengine.save(new_account)
                login()

        case _ :
            print("javascript")
        

     

    

if __name__=="__main__":
    main()
        