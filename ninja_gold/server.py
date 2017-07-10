from flask import Flask, render_template, request, redirect,session,Markup
import random
import datetime

app = Flask(__name__)
app.secret_key ='ninjagold'

@app.route('/')
def render_index():
    if 'gold_count'not in session:
        session['gold_count'] = 0
    if 'message' not in session:
        session['message'] = []
    return render_template("index.html",gold_count=session['gold_count'])

@app.route('/process_money', methods=['post'])
def process_money():
    if 'building' in request.form:
        message = ""
        building = request.form['building']
        golds = 0
        if building == "casino":
            win_or_lost = random.randrange(0,2)
            if win_or_lost == 0:
                if session['gold_count'] >50:
                    golds = random.randrange(0,51)
                else:
                    golds = random.randrange(0, session ['gold_count']+1)
                    session['gold_count'] -= golds
                    message = Markup("<p id='red'>Entered a casino and lost {} golds...ouch...{}</p>".format(golds,datetime.datetime.now()))
            else:
                golds = random.randrange(0,51)
                session['gold_count'] += golds
                message = Markup("<p id='green'>Entered a casino and won {} golds...yeah...{}</p>".format(golds, datetime.datetime.now()))

        else:
            if building == 'farm':
                golds += random.randrange(10,21)
            elif building == 'cave':
                golds += random.randrange(5,11)
            elif building == 'house':
                golds += random.randrange(2,6)
            message = Markup("<p id ='green'>Earned {} golds from the {}! {}</p>".format(golds, building,datetime.datetime.now()))
            session['gold_count'] += golds

        session['message'].insert(0,message)

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold_count'] = 0
    session['message'] = []
    return redirect('/')
app.run(debug=True)
