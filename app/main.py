from flask import Flask, jsonify, render_template, request
from form import MultiplyNumbersForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


def multiplyit(num1, num2):
    return str(int(num1) * int(num2))


@app.route('/', methods=['GET', 'POST'])
def multiply_numbers():
    num1 = None
    num2 = None
    op = None
    form = MultiplyNumbersForm()

    if request.method == 'POST':
        num1 = form.num1.data
        num2 = form.num2.data
        op = multiplyit(num1, num2)

    return render_template('multiply.html', form=form, sum=op)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')