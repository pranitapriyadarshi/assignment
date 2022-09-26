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
  user="root",
  password="pass",
  database="company"
)   
if mydb.is_connected():
    print("Successfully Connected to MySQL database.")
else:
    print("Check yo inputs, they really correct?")
query1 = """CREATE TABLE IF NOT EXISTS Tablename(column1 INT AUTO_INCREMENT PRIMARY KEY, 
 column2 DATE,
 .
 .
 column10 varchar(45));"""
it = 1
cursor = mydb.cursor()

print(mydb)


namecheck = mydb.execute("SELECT * FROM employees ")
if name in namecheck:
     print("Username already exists")


