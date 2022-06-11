from flask import Flask,render_template,url_for
p = Flask(__name__)
int(__name__)

pp.route('/<username>')
def hello_World(name=username):
    return render_template('index.html', name=name)
    