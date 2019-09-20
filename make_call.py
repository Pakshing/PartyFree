from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse
account_sid = 'AC94a0517d20fc9a6ad2eee9d5423791b7'
auth_token = '55c574509ef373551518e269a64f03a7'
client = Client(account_sid, auth_token)
ToCall = "+19162774165"
CallFrom = "+19167961080"

print("This program will call you when you need it. And it will play a pre-recorded drunk voice message, so you can have perfect exercute to leave the meeting or party.")
userPhoneNo= int ( input("Enter your phone number with country code (i.e. 1916xxxxxxx): ") )

call = client.calls.create(
                    url='https://handler.twilio.com/twiml/EH632370b0a5400e644a00ce6ee4cff1af',
                    to=userPhoneNo,
                    from_=CallFrom
                )
print(call.sid)

