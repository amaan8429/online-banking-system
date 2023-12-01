from account_actions import account_actions
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
            return new_pass
             
    else:
            print("Passwords do not match. Please try again.")
            return creating_password()