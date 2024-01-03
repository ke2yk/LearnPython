from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectField, DateField, TimeField)
from wtforms.validators import DataRequired

from wtforms.validators import InputRequired, Length

'''
class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')
'''

class QslForm(FlaskForm):
    callsign = StringField('CallSign:', validators=[InputRequired(),
                                             Length(min=3, max=10)])
  
    qsldate = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
                                        
   # qsltime = TimeField('Time', validators=[DataRequired()], format='%H:%M')
    qsltimehh = StringField('Time UTC HH:', validators=[DataRequired(), Length(min=2, max=2)])
    qsltimemm = StringField(':', validators=[DataRequired(), Length(min=2, max=2)])

    modes = [('SSB', 'SSB'), ('CW', 'CW'), ('Digital', 'Digital')]

    qslmode = SelectField('Mode:', choices=modes, validators=[DataRequired()])
    
    qslemail = StringField('Your Email', validators=[DataRequired(), Length(max=20)])
