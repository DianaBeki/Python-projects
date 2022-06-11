from flask import Flask,render_templates

app = Flask(__name__)
#print(__name__)

@app.route("/")
def hello_world():
   return 'Hello, World!'
   return render_templates('./index.html')