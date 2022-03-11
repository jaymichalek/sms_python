# Code was provided by Twilio from their site.
from twilio.rest import Client

account_sid = 'AC925f409d124090950abccb58bbce6091'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGc35b8ff5dd61267c2cd2143b5370f78f',
    # In this case, 'Testing Twilio' was the text message body (see comments below):
    body='your_text_message',
    to='your_phone_number'
)

print(message.sid)


""" Successfully sent text message to my verified phone number using this code.
    Text message received from Twilio:
    'Sent from your Twilio account - Testing Twilio' """
