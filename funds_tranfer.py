from database import myengine,UserDatabase
def funds_tranfer(name,my_bal):
    my_friend = myengine.find_one(UserDatabase,UserDatabase.name==name)
    if my_friend is None:
        print("your friend does not exist")
    else:
        his_bal = my_friend.balance
        print("1 to send money")
        print("2 to take money")
        action = int(input("Choose"))
        if action == 1:
           return(sending_money(my_bal,his_bal),my_friend)
           
        elif action == 2:
            return(take_money(my_bal,his_bal),my_friend)
        else:
            print("wrong input")
            return
        


def sending_money(my_bal,his_bal:int):
            money = int(input("how much money you want to send"))
            if my_bal >= money:
                my_bal-=money
                his_bal+=money
                print("You are a good person")
            else:
                print("you are broke man ,please enter accordingly")
                sending_money(my_bal,his_bal)
            return my_bal,his_bal

def take_money(my_bal,his_bal):
    money=int(input("how much money you want to take"))
    if money>his_bal:
        print("your friend does not own that much money")
        print("do you want to all what is there in the account")
        choice = int(input("enter 1 to proceed"))
        if choice==1:
            my_bal+=his_bal
            his_bal=0
            print("you are a true jerk !! Keep it Up")
        else:
            print("You do have a heart ! Nice ")                   
    else:
        his_bal-=money
        my_bal+=money
        
    return my_bal,his_bal
    