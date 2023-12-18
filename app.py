from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def link1():
    return render_template('index.html')

@app.route('/2')
def link2():
    return render_template('index2.html')