from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key="counterkey"

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 2
    else:
        session['count'] += 1
    return render_template("index.html", count=session['count'])

@app.route('/reset', methods=['post'])
def reset():
    session['count'] = 0
    return redirect("/")

@app.route('/counter', methods=['post'])
def create_user():
   return redirect('/')

app.run(debug=True)
