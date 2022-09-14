from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField


class MultiplyForm(FlaskForm):
    num1 = IntegerField('number 1?')
    num2 = IntegerField('number 2?')
    
submit = SubmitField('multiply!')