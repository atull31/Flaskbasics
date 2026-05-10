#we will focus on 3 things in this: 
#Building url dynamically
#Variable rule 
#jinja 2 template engine
'''
{{  }} expressions to print output in html
{%...%} conditions. for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request
###it creates an instance of the flask class
###which will be my WSGI(web server gateway interface) application.

app = Flask(__name__)

@app.route("/") #it is an decorator which contains the rule '/'
def welcome():
    return "<html><H1>Welcome to the flask app </H1></html>"

@app.route("/index",methods=['GET']) #it is an decorator which contains the rule '/'
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res= "FAIL"
    return render_template('result.html',results = res)

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res= "FAIL"
        
    exp = {'score':score,"res":res}
    return render_template('result1.html',results = exp)


#Entry point of this file
if __name__ == "__main__":
    app.run(debug = True) #Entire flask app will run
