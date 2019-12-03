from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
#account_sid = 'xxxxxxxxxxxxxxxxxxxx'
#auth_token = 'xxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='All in the game, yo',
                              from_='xxxxxxxxxxxx',
                              to='xxxxxxxxx'
                          )

print(message.sid)
