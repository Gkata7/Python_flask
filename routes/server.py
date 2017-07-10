from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')


def ninjas():
  return render_template("ninjas.html")
app.run(debug=True)
