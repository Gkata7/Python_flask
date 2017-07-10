from flask import Flask, render_template, request, redirect,session,flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key ='RegistrationKey'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if 'email' in request.form and 'first_name' in request.form and 'last_name' in request.form and 'password' in request.form and 'confirm_password' in request.form:
        failure = False
        if request.form['email'] == '':
            flash("Email must be valid!", 'emailError')
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid email", 'emailError')
        else:
            session['email'] = request.form['email']

        if request.form['first_name'] == '':
            flash("First name cannot be blank!", 'firstNameError')
        elif any(char.isdigit() for char in request.form['first_name']) == True:
            flash('Name cannot have numbers', 'firstNameError')
        else:
            session['first_name'] = request.form['first_name']

        if request.form['last_name'] == '':
            flash("Last name cannot be blank!", 'lastNameError')
        elif any(char.isdigit() for char in request.form['last_name']) == True:
            flash('Name cannot have numbers', 'lastNameError')
        else:
            session['last_name'] = request.form['last_name']

        if request.form['password'] == '':
            flash("Password needs to be more than 8 characters!", 'passwordError')
        elif len(request.form['password']) < 8:
            flash("Password must be longer than 8 characters", 'passwordError')
        else:
            session['password'] = request.form['password']

        if request.form['confirm_password'] == '':
            flash("Password Confirmation needs to match!", 'confirmError')
        elif request.form['password'] != request.form['confirm_password']:
            flash('Passwords do not match', 'confirmError')
        else:
            session['confirm'] = request.form['confirm_password']
    return redirect('/')

@app.route('/submit')
def register_results():
        return render_template('results.html')

app.run(debug=True)
