from flask import Flask,render_template
###it creates an instance of the flask class
###which will be my WSGI(web server gateway interface) application.

app = Flask(__name__)

@app.route("/") #it is an decorator which contains the rule '/'
def welcome():
    return "<html><H1>Welcome to the flask app </H1></html>"

@app.route("/index") #it is an decorator which contains the rule '/'
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


#Entry point of this file
if __name__ == "__main__":
    app.run(debug = True) #Entire flask app will run
