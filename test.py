from cgitb import text
import os
import smtplib
import sys
import openai

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

print('Enter a prompt: ')
message_to_send = input()

print('Enter a number: ')
number = "+1"+input()




account_sid = 'AC077b3e50465d9691130ad9fc34b6ae18'
auth_token = 'b9a5dd0ad5163118a852562f6f716460'
client = Client(account_sid, auth_token)



openai.api_key = "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"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=message_to_send,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.get("choices")[0].get("text"))

answer = response.get("choices")[0].get("text")

message = client.messages \
    .create(
         body=answer,
         from_='+17754069764',
         to=number
     )




