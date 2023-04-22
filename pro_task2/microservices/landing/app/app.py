from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import os


import requests
import os

app = Flask(__name__)
api = Api(app)


add_url = os.environ['ADD_URL']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def addition():
    operation = request.form.get('operation')
    if request.method=='POST' and operation == 'add':
        number_1 = (request.form.get('first',type=int))
        number_2 = (request.form.get('second',type=int))
        url = f"{add_url}/add/{number_1}/{number_2}/"
        response = requests.get(url)
        result = response.json()
        return f"The result of adding {number_1} and {number_2} is {result['result']}"
    else:
        return render_template('index.html')
    


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )