from flask import Flask
app = Flask(__name__)
@app.route("/blog")
def blog():
   return 'These are my thoughts on blogs'

@app.route("/blog/2020/dogs")
def blog2():
    return 'This is my dog'
    
       