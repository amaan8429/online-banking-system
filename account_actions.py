from transaction_history import transaction_history_func
from calculating_time import calculating_time
from funds_tranfer import funds_tranfer

def account_actions(my_user):
    print("Welcome\nWhat Operation do you want to perform today")
    print("press 1 to deposit money")
    print("press 2 to withdraw")
    print("press 3 to check all running loans")
    print("press 4 to apply for a loan")
    print("press 5 to check all details")
    print("press 6 to check your transaction history")
    print("press 7 to transfer money")
    print("press 8 to change your password")
    print("press 9 to contact customer support")
    print("press 10 to exit")
    option = int(input("Select your Option  "))
    perform_operation(option, my_user)

def perform_operation(option: int, my_user):
    if option == 1:
        option1(my_user)
    elif option==2:
       option2(my_user)
    elif option==5:
       option5(my_user)
    elif option==6:
       option6(my_user)
    elif option==7:
       option7(my_user)
    elif option ==10:
        return
    else:
        invalid_option(my_user)
        

def option1(my_user):
    money = int(input("how much money you want to deposit "))
    prev_bal,new_bal = my_user.deposit(money)
    curr_time = calculating_time()
    task = "Deposit"
    rs = transaction_history_func(task,money,curr_time,prev_bal,new_bal)
    my_user.transactions(rs)
    print("what else would you like to do today")
    what_else = int(input("Press 1 for more tasks and any other option to exit "))
    if what_else == 1:
        account_actions(my_user)

    print("See you Seen")
    return

def option2(my_user):
    money = int(input("how much money you want to withdraw "))
    prev_bal,new_bal = my_user.withdraw(money)
    curr_time = calculating_time()
    task = "WithDraw"
    rs = transaction_history_func(task,money,curr_time,prev_bal,new_bal)
    my_user.transactions(rs)
    my_user.withdraw(money)
    print("what else would you like to do today")
    what_else = int(input("Press 1 for more tasks and any other option to exit "))
    if what_else == 1:
        account_actions(my_user)

    print("See you Seen")
    return

def option3(my_user):
    if my_user.loan_status:
        print("you cannot apply for a new loan")
    else:
        print("how much amount you need as loan")



def option5(my_user):
    my_user.display()


def option6(my_user):
    my_user.print_transactions()
    what_else = int(input("Press 1 for more tasks and any other option to exit "))
    if what_else == 1:
        account_actions(my_user)

    print("See you Seen")
    return


def option7(my_user):
    other_acc=input("enter the name of the account you want to do transaction with")
    my_bal=my_user.balance
    new_data = funds_tranfer(other_acc,my_bal)
    # if new_data is not None:
    #     (a1,a2),friend=new_data
    #     print(a1)
    #     print(a2)
    my_user.transfer_funds(new_data)


def invalid_option(my_user):
    print("Invalid choice")
    print("Please try a valid operation")
    what_else = int(input("Press 1 for more tasks and any other option to exit "))
    if what_else == 1:
        account_actions(my_user)

    print("See you Seen")
    return



