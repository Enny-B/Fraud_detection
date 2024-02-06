# Importing necessary libraries
import pandas as pd
from flask import Flask, request, render_template, url_for, redirect
from flask_mail import Message, Mail
import socket
from itsdangerous import URLSafeTimedSerializer
from flask_bcrypt import bcrypt
import random
from random import *
import vonage
import os
from twilio.rest import Client 
import time 
import re
from twilio.rest import Client
# global register


#Using Twilio API
# account_sid = os.environ.get()

# Function for checking the data ba=undles in case he user wants to buy/purchase data
def data_bundles():
    data = input(
        "1. Daily Bundles\n"
        "2. Weekly Bundles\n"
        "3. Monthly Bundles\n"
    )
    if data == "1":
        print("Daily Bundles include: ")
    elif data == "2":
        print("Weekly Bundles include: ")
    elif data == "3":
        print("Weekly Bundles include: ")
    else:
        print("Invalid entry\n"
              "Try Again")
        data_bundles()


# FUnction for checking the points the user has
def points():
    my_points = input(
        "1. Check points balance\n"
        "2. Redeem Data Bundles\n"
        "3. Purchase more points\n"
        "4. Purchase Airtime\n"
        ""
    )
    if my_points == "1":
        print("Your points balance is : ")
    elif my_points == "2":
        data_bundles()
    elif my_points == "3":
        print("Plans for purchasing more points include: ")
    elif my_points == "4":
        print("Airtime Bundles include: ")
    else:
        print("Invalid entry\n"
              "Try Again")
        points()


# Function to confirm phone number
def confirm_phone_number():
    phone_number = phone_number

# writing a function to generate otp every 2 mins
def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(randint(000000, 999999))
        print("OTP is: ")
generate_otp()



# 




# Function for confirming the latest payment received by the client
def latest_payment():
    no_sent = input("Enter phone number: ")
    if len(no_sent) == 11 and no_sent.isnumeric():
        print("OTP is #XXXXXXXXXXX")
    elif no_sent == no_sent:
        generate_otp()
        otp = input("Enter OTP: ")
    elif  len(otp) == 6 and otp.isnumeric():
        input("Enter the last four digits of your account number to proceed")
    else:
        print("Invalid Entry\n"
              "Try Again in 2 seconds")
        latest_payment()


# Function for checking the services
def myservices():
    services = input(
        "1. Latest Payment Received\n"
        "2. My Wallet\n"
        "Select one: "
    )
    if services == "1":
        latest_payment()
    elif services == "2":
        print("Wallet getting ready to be opened..")
        myservices()

# Function for when the user dials the code
def registerEntry():
    register = input(
        "1. Register\n"
        "2. My Services\n"
        "3. My Points\n"
        "Select any service: "
    )
    if register == "1":
        print('You have joined our family!!')
    elif register == "2":
            myservices()
    elif register == "3":
        points()
    else:
        print("Invalid Entry\n"
              "Try Again")
        registerEntry()
        
# registerEntry()        


# creating a function that checks for the ussd code
def check_ussd():
    ussd = input("Enter USSD code: ")
    if ussd == "*250#":
        print("Welcome to Fraud Detection Services..")
        registerEntry()
    else:
        print("Invalid Entry\n" "Try Again")
        check_ussd()
        
check_ussd()


# if __name__ == '__main__':
#     app.run(threaded = True, host= '0.0.0.0', port=8080) 















# app = Flask(__name__)

# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)

# otp = randint(000000, 999999)


# setting the mail server
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'eniolasomoye16@gmail.com'
# app.config['MAIL_PASSWORD'] = 'vzbklcquslizoumh'
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USE_TLS'] = False
# mail = Mail(app)


# @app.route("/", methods=['GET', 'POST'])
# def form():
#     return render_template('form.html')