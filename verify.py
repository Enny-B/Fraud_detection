# importing necessary libraries
import pandas as pd
from flask import Flask, redirect, request, render_template, url_for, session, flash
import socket


app = Flask(__name__)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

@app.route('/verify', methods=['GET'])
def verify():
    # user_otp = request.form['otp']
    # if otp == int(user_otp):
        # return "<h3>Email verification is successful</h3>"
    # return "<h3>Failure, OTP dosen't match</h3>"
    return render_template('verify.html')


if __name__ == '__main__':
    app.run(debug = True, threaded = True, host= str(IPAddr), port=5000) 