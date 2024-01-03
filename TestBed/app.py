from flask import Flask, render_template, redirect, url_for, session, request
from forms import QslForm
from hamdb import getcallinfo
import sqlite3

app = Flask(__name__)
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
        qslmode TEXT
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

def writedb():

    conn = sqlite3.connect('qslinfo.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO userinfo (callsign,
                              qsldate,
                              qsltimehh,
                              qsltimemm,
                              qslmode) 
                VALUES ('n2oud', 
                        '20211111',
                        15,
                        25,
                        'CW')
                    ''')

    conn.commit()
    conn.close()

#createdb()

#querydb()

#writedb()


@app.route('/', methods=('GET', 'POST'))
def index():

    form = QslForm()
    
    if form.validate_on_submit():

        qslinfo = [{'callsign': form.callsign.data,
                        'qsldate': form.qsldate.data,
                        'qsltimehh': form.qsltimehh.data,
                        'qsltimemm': form.qsltimemm.data,
                        'qslmode': form.qslmode.data                         
                       }]

        # Store callsign in a session variable
        session['callsign'] = form.callsign.data

        # Store qslinfo in a session variable
        session['qslinfo'] = qslinfo

        return redirect(url_for('validate'))
    
    return render_template('index.html', form=form)

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
        
    return render_template('validate.html', qslinfo=qslinfo, userinfo=userinfo)

@app.route('/process/')
def process():
    
    #callsign = session.get('callsign')
    
    qslinfo = session.get('qslinfo')
    
    userinfo = session.get('userinfo')

    #userinfo = getcallinfo(callsign)
    
    #return render_template('index.html', message="Processed...")
    
    return redirect(url_for('index'))



if __name__ == '__main__':
    print("Starting the damn App")
    app.run(debug=True)    