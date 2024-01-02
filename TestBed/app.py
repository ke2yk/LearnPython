from flask import Flask, render_template, redirect, url_for, session
from forms import QslForm
from hamdb import getcallinfo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd70d72ee73d021d8d8538c02620ca860c038687c0675a038'

qslinfo = [{}]
userinfo = [{}]
callsign = ""

'''
courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]
'''

@app.route('/', methods=('GET', 'POST'))
def index():
    form = QslForm()
    if form.validate_on_submit():
        qslinfo.append({'callsign': form.callsign.data,
                        'qsldate': form.qsldate.data,
                        'qsltimehh': form.qsltimehh.data,
                        'qsltimemm': form.qsltimemm.data,
                        'qslmode': form.qslmode.data                         
                       })

        session['callsign'] = form.callsign.data
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success/')
def success():
    callsign = session.get('callsign')
    userinfo = getcallinfo(callsign)
    return render_template('success.html', qslinfo=qslinfo, userinfo=userinfo)


if __name__ == '__main__':
    print("Starting the damn App")
    app.run(debug=True)    