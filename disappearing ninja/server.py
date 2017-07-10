
from flask import Flask, redirect, render_template, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninja():
    displayALL = True
    return render_template('ninja.html', displayALL=displayALL)

@app.route('/ninjas/<color>')
def Color(color):
    displayALL = False
    return render_template('ninja.html', color=color, displayALL=displayALL)

app.run(debug=True)
