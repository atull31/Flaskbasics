from flask import Flask
###it creates an instance of the flask class
###which will be my WSGI(web server gateway interface) application.

app = Flask(__name__)

@app.route("/") #it is an decorator which contains the rule '/'
def welcome():
    return "Welcome to this Flask application. This will be an amazing app..SUIIIII"

@app.route("/index") #it is an decorator which contains the rule '/'
def index():
    return "Welcome to index page..SUIIIII"


#Entry point of this file
if __name__ == "__main__":
    app.run(debug = True) #Entire flask app will run
