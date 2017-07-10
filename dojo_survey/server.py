from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key ='ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def user_info():
   if 'name' in request.form and 'location' in request.form and 'language' in request.form and 'comment' in request.form:
       if request.form['name'] != '' and request.form['location'] != '' and request.form['language'] != '':
           session['name'] = request.form['name']
           session['location'] = request.form['location']
           session['language'] = request.form['language']
           session['comment'] = request.form['comment']

           return redirect('/survey_result')
   return redirect('/')

@app.route('/survey_result')
def show_info():
    if 'name' in session and 'location' in session and 'language' in session and 'comment' in session:
        return render_template('index2.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])
    return redirect('/')
app.run(debug=True)
