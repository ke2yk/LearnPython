from flask import Flask, render_template, redirect, url_for
from forms import CourseForm
from forms import QslForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd70d72ee73d021d8d8538c02620ca860c038687c0675a038'

qslinfo = [{}]

courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]



@app.route('/courses/')
def courses():
    return render_template('courses.html', courses_list=courses_list)

    # ...
@app.route('/xyz', methods=('GET', 'POST'))
def xyz():
    form = CourseForm()
    if form.validate_on_submit():
        courses_list.append({'title': form.title.data,
                             'description': form.description.data,
                             'price': form.price.data,
                             'available': form.available.data,
                             'level': form.level.data
                             })
        return redirect(url_for('courses'))
    return render_template('index.html', form=form)

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
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success/')
def success():
    return render_template('success.html', qslinfo=qslinfo)


#if __name__ == '__main__':
 #   app.run(debug=True)    