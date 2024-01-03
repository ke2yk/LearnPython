from flask import Flask, render_template, redirect, url_for, session, request
from forms import QslForm
from hamdb import getcallinfo
import sqlite3

app = Flask(__name__)

#app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'd70d72ee73d021d8d8538c02620ca860c038687c0675a038'

qslinfo = [{}]
userinfo = [{}]
callsign = ""

def createdb():
    conn = sqlite3.connect('qslinfo.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS  userinfo (
        id INTEGER PRIMARY KEY,
        callsign TEXT,
        qsldate TEXT,
        qsltimehh TEXT, 
        qsltimemm TEXT,
        qslmode TEXT,
        qslemail TEXT,
        status TEXT
        )
        ''')

    conn.commit()
    conn.close()

def querydb():

    conn = sqlite3.connect('qslinfo.db')
    cursor = conn.cursor()

    # Reading data from the table
    cursor.execute('SELECT * FROM userinfo')
    rows = cursor.fetchall()

    # Displaying the retrieved data
    for row in rows:
         print(row)
    conn.close()    

#createdb()

#querydb()

@app.route('/', methods=('GET', 'POST'))
def index():

    form = QslForm()
    
    if form.validate_on_submit():

        qslinfo = [{'callsign': form.callsign.data,
                        'qsldate': form.qsldate.data,
                        'qsltimehh': form.qsltimehh.data,
                        'qsltimemm': form.qsltimemm.data,
                        'qslmode': form.qslmode.data,
                        'qslemail': form.qslemail.data                         
                   }]
         
        timehh = int(form.qsltimehh.data)
        timemm = int(form.qsltimemm.data)

        if timehh > 23: 
            error = "QSL Hour Cannot Exceed 23"
            return render_template('index.html', form=form, error=error)

        if timemm > 59: 
            error = "QSL Minutes Cannot Exceed 59"
            return render_template('index.html', form=form, error=error)            

        # Store callsign in a session variable
        session['callsign'] = form.callsign.data

        # Store qslinfo in a session variable
        session['qslinfo'] = qslinfo

        return redirect(url_for('validate'))
    
    return render_template('index.html', form=form, message="Enter QSL Info")

@app.route('/validate/')
def validate():
    
    # Get qslinfo session variable From / route
    qslinfo = session.get('qslinfo')
    
    # get callsign session variable From / route
    callsign = session.get('callsign')

    # Execute API In hamdb.by and return result to userinfo
    userinfo = getcallinfo(callsign)
    
    # Store userinfo in a session variable
    session['userinfo'] = userinfo

    if request.method == 'POST':
        button_pressed = request.form['action']
    
        if button_pressed == 'submit':
            message = "SUBMIT"
            return redirect(url_for('process', message="Processing"))
        
        elif button_pressed == 'reject':
            message = "REJECT"
            qslinfo = {}
            return redirect(url_for('index', message="Rejected"))
        
    return render_template('validate.html', qslinfo=qslinfo, userinfo=userinfo, message="Please Validate Your Input")

@app.route('/process/')
def process():
    
    #callsign = session.get('callsign')
    
    qslinfo = session.get('qslinfo')
        
    fel = qslinfo[0] 

    qslcallsign = fel['callsign']
    qsldate = fel['qsldate']
    qsltimehh = fel['qsltimehh']
    qsltimemm = fel['qsltimemm']
    qslmode = fel['qslmode']
    qslemail = fel['qslemail']
    status = 'ready'

    conn = sqlite3.connect('qslinfo.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO userinfo (callsign, qsldate, qsltimehh, qsltimemm, qslmode, qslemail, status) VALUES (?, ?, ?, ?, ?, ?, ?)', (qslcallsign, qsldate, qsltimehh, qsltimemm, qslmode, qslemail, status))

    conn.commit()
    conn.close()


    userinfo = session.get('userinfo')
    #callsign = (userinfo['hamdb']['callsign']['call'])
    
    #userinfo = getcallinfo(callsign)
    
    #return render_template('index.html', message="Processed...")
    
    return redirect(url_for('index'))



if __name__ == '__main__':
    print("Starting the damn App")
    app.run(debug=True)    