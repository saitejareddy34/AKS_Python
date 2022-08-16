from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField


class AddNumbersForm(FlaskForm):
    num1 = IntegerField('What is number 1?')
    num2 = IntegerField('What is number 2?')
    num3 = IntegerField('what is number 3?')
    submit = SubmitField('Add!')