from flask import Flask, render_template
''''
It creates an instance of Flask class,
which will be your WSGI(Web Server Gateway Interface) application
'''

## WSGI Application 
app = Flask(__name__)

@app.route("/home")
def welcome():
        return "<html><H1>welcome to this Flask introduction and i am in learning phase</H1></html>"

@app.route("/index")
def index():
        return render_template('index.html')

@app.route("/about")
def about():
        return render_template('about.html')


if __name__ == "__main__":
        
        app.run(debug=True)


## four types of verbs: get, post, put, delete 
