from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if 'name' in request.form:
        if request.form['name'] != '':
            session['name'] = request.form['name']
    return redirect('/result')
    return redirect('/')

@app.route('/result')
def result():
    if 'name' in session:
        return render_template('index.html', name = session['name'])
        return redirect('/')

app.run(debug=True)
