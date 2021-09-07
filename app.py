import requests
from flask import Flask, render_template, request
import os

import json

app = Flask(__name__)


@app.route('/')
def index():
    example = ['a', 'b', 'c']
    return render_template('index.html', example=example)


# @app.route('/results', methods=['POST'])
# def results():
#     if request.method == 'POST':
#         member_info = []
#         thing = request.form.get('member')
#         for r in response['data']:
#             if r['handle'].__contains__(thing):
#                 member_info.append(r)
#
#         return render_template('results.html', member=member_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
