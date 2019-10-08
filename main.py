import time
from datetime import datetime as dt
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse
from flask import Flask, render_template, request, redirect, url_for,flash
account_sid = 'AC94a0517d20fc9a6ad2eee9d5423791b7'
auth_token = 'c135b809899593c0b8317a57ce5b9a0b'
client = Client(account_sid, auth_token)
ToCall = "+19162774165"
CallFrom = "+19167961080"
userPhoneNo="9162774165"
waitTime=""


        
app = Flask(__name__)
app.config['SECRET_KEY'] = '83a424a295e35e7e1639b63ef9f494e4'

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/hello', methods=['POST','GET'])
def hello():
    global userPhoneNo
    global waitTime
    userPhoneNo = request.form['userPhoneNo']
    waitTime = request.form['waitTime']
    print("It works." + userPhoneNo +" " + waitTime +"min")
    render_template('makingCall.html')

    time.sleep(float(waitTime)*60)
    call = client.calls.create(
                    url='https://handler.twilio.com/twiml/EHc4f001455119c10a559b8d06b71339b6',
                    to="+" + userPhoneNo,
                    from_=CallFrom
                )
    print(call.sid)
    return render_template('makingCall.html')


@app.route('/makeCall')
def makeCall():
    print("It works.")
    time.sleep(float(waitTime)*60)
    call = client.calls.create(
                    url='https://handler.twilio.com/twiml/EHc4f001455119c10a559b8d06b71339b6',
                    to="+" + userPhoneNo,
                    from_=CallFrom
                )
    print(call.sid)




if __name__ == '__main__':
    app.run(debug=True)




