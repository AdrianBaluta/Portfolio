from twilio.rest import Client 
 
account_sid = 'enter accound sid here'
auth_token = 'enter token here'
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='phone number',
                              body='Boo!',        
                              to='phone number'
                          ) 
 
print(message.sid)