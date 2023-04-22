from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

@app.route('/sub/<int:num1>/<int:num2>/')
def sub(num1, num2):
    result = num1 - num2
    return str(result)
    #return render_template('sub.html')

'''
class subitionResource(Resource):
    def get(self, n1, n2):
        res = n1 + n2
        return {'result': res}
'''
#api.sub_resource(subitionResource, '/sub/<int:n1>/<int:n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5052,
        host="0.0.0.0"
    )