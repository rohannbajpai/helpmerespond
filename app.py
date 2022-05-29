# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask, redirect, url_for, request, render_template
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

from cgitb import text
import openai

from twilio.rest import Client
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/main',methods = ['POST', 'GET'])
def main(): 
   if request.method == 'POST':
      message = request.form['message']
      number = request.form['number']
      print(number)
      processRequest(number, message)

      return render_template('main.html')
   else:
      user = request.args.get('nm')
      return render_template('main.html')
  

def processRequest(number, message): 
    account_sid = ''#filler
    auth_token = ''filler
    client = Client(account_sid, auth_token)

    openai.api_key = "" #filler key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Respond to the following: " + message,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print("message: " + response.get("choices")[0].get("text"))

    answer = response.get("choices")[0].get("text")
    message = client.messages \
        .create(
            body= "\n" + answer,
            from_='+17754069764',
            to='+1'+number
        )

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
