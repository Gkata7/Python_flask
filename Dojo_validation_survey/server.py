from flask import Flask, render_template, request, redirect,session,flash
app = Flask(__name__)
app.secret_key ='ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/survey', methods=['POST'])
def user_info():
    if request.form['name'] == "" and request.form['comment'] == "":
        flash("Name cannot be empty!")
        flash("Comment cannot be empty")
    if request.form['name'] =="":
        flash("Fill out field", "name error")
        return redirect('/')
    if request.form['comment']=="":
        flash("Fill out field", "comment + error")
        return redirect('/')
    if len(request.form['comment']) >120:
        flash ("Too long")
        return redirect('/')
    if 'name' in request.form and 'location' in request.form and 'language' in request.form and 'comment' in request.form:
        if request.form['name'] != '' and request.form['location'] != '' and request.form['language'] != '':
            session['name'] = request.form['name']
            session['location'] = request.form['location']
            session['language'] = request.form['language']
            session['comment'] = request.form['comment']

        return redirect('/survey_result')

@app.route('/survey_result')
def show_info():
    if 'name' in session and 'location' in session and 'language' in session and 'comment' in session:
        return render_template('index2.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])
    return redirect('/')
app.run(debug=True)
