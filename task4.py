
import math,os
import random,sys
import smtplib
import mysql.connector

email=input("Enter the email address")
otp=''.join([str(random.randint(0,9))for i in range(6)])
for i in range(1,6):
   if email in open('emailaddress.csv').read():
     print("One time-password is:",otp)
     flag1=1
     break;
   else:
     print("Please enter another address:")
     email=input()
else:
    print("Sorry,more than 5 trials not allowed")     

msg="Hello,Your OTP is"+str(otp)
user=input("Enter the otp you received:")
for j in range(1,6):
    if(user==otp):
        print("Successfully Authenticated")
        break;
    else:
        print("Authentication failed!!Please try again")
        user=input("Please enter the otp again you received:")
else:
    print("Sorry,more than 5 trials not allowed")             
companyname=input("Enter a company name:")
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb) 


    
