from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key="bookkey"
mysql = MySQLConnector(app,'articles')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    data = {
            'id': id
        }
    users = mysql.query_db(query,data)
    print users
    return render_template('index.html', users = users)

@app.route('/add', methods=["GET","POST"])
def add():
    return render_template("add.html")

@app.route("/adduser", methods=["POST"])
def create():
    error = 0
    if request.form['title'] == '':
        flash("Title can't be left blank!","titleError")
        error += 1
    if len(request.form['title']) < 2:
        flash("Title needs to be more than 2 characters", "titleError")
        error += 1
    if request.form['author'] == '':
        flash("Author can't be left blank!", "authorError")
        error += 1
    if len(request.form['author']) < 3:
        flash("Author needs to be more than 3 characters", "authorError")
        error += 1
    elif any(char.isdigit() for char in request.form['author']) == True:
        flash("Author can't have numbers", "authorError")
        error += 1

    if error == 0:
        query = "INSERT INTO users(title, author,created_at,updated_at) VALUES (:title, :author,NOW(),NOW())"
        data = {
                'title': request.form['title'],
                'author': request.form['author']
                }
        mysql.query_db(query,data)
        return redirect('/')
    else:
        error = 0
        return redirect('/add')

@app.route('/delete/<user_id>',methods = ['GET'])
def delete(user_id):
    return render_template("delete.html")

@app.route('/cancel', methods=['GET'])
def cancel():
    return redirect('/')

@app.route('/destroy', methods=['DELETE'])
def destroy():
    users = [user for user in user if user['title'] == title]
    users.remove(users[0])
    return redirect('/')

app.run(debug=True)
