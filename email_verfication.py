import os
from email.message import EmailMessage
import ssl , smtplib
import random


def generating_otp():
    otp = random.randint(1000,9999)
    return otp

def ask_the_mail():
    new_email = input("Enter your email for verfication  ")
    final_ans = send_mail(new_email)
    if final_ans is None:
        print("try again to verfiy your email")
        ask_the_mail()
    
    print("good job, now go ahead and finish your last task")
    return True,new_email

def send_mail(user_mail):
    sender = "amaanrizvi73@gmail.com"
    receiver = user_mail
    subject="this is a mail"
    password = "gamz qqne csci ltld"
    generated_otp = generating_otp()
    body=str(generated_otp)

    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465 ,context=context) as smtp:
            smtp.login(sender,password)
            smtp.sendmail(sender,receiver,em.as_string())
            print("email sent")
            print("Please check your mail for otp")
            ans = input_otp(generated_otp)
            if ans:
                 return True
            

    
def input_otp(generated_otp:int):
    user_input_otp = int(input("Enter the OTP  "))
    return(verify_otp(user_input_otp,generated_otp))

def verify_otp(opt_user,otp_generated):
    if opt_user==otp_generated:
        print("email verfied")
        return True
    else:
        print("wrong otp")
        input_otp(otp_generated)

         
    
          
     
     