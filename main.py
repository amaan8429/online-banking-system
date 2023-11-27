# from bank import Bank
from database import UserDatabase,myengine 
from account_actions import account_actions


def login():
    my_username=input("enter the nanme you registed  ")
    my_user = myengine.find_one(UserDatabase,UserDatabase.name==my_username)
    if my_user is None:
        print("Invalid UserName,Try Again")
        login()
    else:
         password_check(my_user)
        


def password_check(my_user):
    my_password=int(input("enter your password"))
    if my_password == my_user.password:
            account_actions(my_user)
    else:
            print("Wrong Password,Try Again")
            password_check(my_user)

    
          
def creating_password(): 
    new_pass=int(input("create a new password"))
    new_pass_confirm=int(input("enter your password again"))
    if new_pass==new_pass_confirm:
            print("you have successfully created a account")
            print("go ahead and login into your account")
            login()
            return new_pass
             
    else:
            print("Passwords do not match. Please try again.")
            return creating_password()


def main():
    choice = int(input("press 1 to login and 2 to sign up"))
    match choice:
        case 1: 
            login()
        case 2:
            new_name=input("enter your name")
            new_age=int(input("enter your age"))
            final_pass = creating_password() 
            if final_pass:
                new_account = UserDatabase(
                    name=new_name,
                    age=new_age,
                    password=final_pass
                )
                myengine.save(new_account)
        case _ :
            print("javascript")
        

     

    

if __name__=="__main__":
    main()
        