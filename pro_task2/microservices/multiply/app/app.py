from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

@app.route('/mul/<int:num1>/<int:num2>/')
def mutliply(num1, num2):
    result = num1 * num2
    return str(result)
    #return render_template('mutliply.html')

'''
class mutliplyitionResource(Resource):
    def get(self, n1, n2):
        res = n1 + n2
        return {'result': res}
'''
#api.mutliply_resource(mutliplyitionResource, '/mutliply/<int:n1>/<int:n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5053,
        host="0.0.0.0"
    )