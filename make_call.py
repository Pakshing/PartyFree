from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
CallFrom = "+19167961080"

print("This program will call you when you need it. And it will play a pre-recorded drunk voice message, so you can have perfect exercute to leave the meeting or party.")
userPhoneNo= int ( input("Enter your phone number with country code (i.e. 1916xxxxxxx): ") )

call = client.calls.create(
                    url='https://handler.twilio.com/twiml/EH632370b0a5400e644a00ce6ee4cff1af',
                    to=userPhoneNo,
                    from_=CallFrom
                )
print(call.sid)

