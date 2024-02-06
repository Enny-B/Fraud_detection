# importing necessary libraries
import pandas as pd
from flask import Flask, redirect, request, render_template, url_for, session, flash
from flask_bcrypt import bcrypt
from flask_mongoengine import MongoEngine
from flask import *
from flask_mail import Message, Mail
import socket
import csv
import pyotp
from itsdangerous import URLSafeTimedSerializer
import random
from random import *
import vonage



app = Flask(__name__)

secret = URLSafeTimedSerializer('Thisisasecret!')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'eniolasomoye16@gmail.com'
app.config['MAIL_PASSWORD'] = 'vzbklcquslizoumh'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

otp = randint(000000, 999999)

@app.route('/', methods = ['POST', 'GET'])
def signup():
    return render_template('signup.html')



@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone_number = request.form['phone-number']
        password = request.form['password']
        password2 = request.form['password2']
        print(fullname, email, password, password2)
        header = ['fullname', 'email', 'password', 'Phone Number']
        with open('signup_details.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            # writer.writerow(header)
            writer.writerow([fullname, email, password, phone_number])
            if password == password2:
                print("You have signed up successfully")
    print("start")
    email = request.form['email']
    phone_number = request.form['phone-number']
    print(email)
    msg = Message(subject = 'OTP', sender = 'eniolasomoye16@gmail.com', recipients=[email])
    # print("get message")
    msg.body = 'Hello, Your OTP is ' + str(otp)
    print(msg.body)
    # print(randint(000000, 999999))
    # print("got otp")
    mail.send(msg)
    # print("send message")
    return render_template('verify.html')



@app.route('/validate', methods = ['POST'])
def validate():
    user_otp = request.form['otp']
    if  otp == int(user_otp):
        return render_template('email_verify.html')


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST" and 'email' in request.form and 'password' in request.form:
        username = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        if bcrypt.checkpw(password, hashed):
            header = ['username', 'hashed_password']
            with open("login_details.csv", 'a', newline = '') as f:
                writer = csv.writer(f, delimiter=',')
                # writer.writerow(header)
                writer.writerow([username, hashed])
            print('It matches')
            print(username, password)
            return redirect(url_for('detector'))

    return render_template('login.html')



@app.route('/detector')
def detector():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return render_template('detector.html')

# @app.route("/logout")
# def logout():
    # logout_user()
    # return redirect(mess)

if __name__ == '__main__':
    app.run(threaded = True, host= '0.0.0.0', port=8080, debug=True)
    # app.run(debug = True, threaded = True, host= '0.0.0.0', port=5000) 
