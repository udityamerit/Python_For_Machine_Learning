from flask import Flask
''''
It creates an instance of Flask class,
which will be your WSGI(Web Server Gateway Interface) application
'''

## WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
        return "welcome to this Flask introduction and i am in learning phase"

@app.route("/index")
def index():
        return "welcome to this Flask index and i am in learning phase"

if __name__ == "__main__":
        
        app.run(debug=True)
