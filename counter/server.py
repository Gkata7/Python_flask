from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secretkey'


@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    session['counter'] = 0
    return redirect ('/')

app.run(debug=True)
