#!/usr/bin/python3
# -*- coding:utf-8 -*-
import json
from flask import Flask, Response
import requests


app = Flask(__name__)
@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')
@app.route("/getUser")
def getUser():
    result = {'username': 'python', 'password': 'python'}
    return Response(json.dumps(result), mimetype='application/json')
@app.route("/getJava")
def getJava():
    result = {'username': 'python', 'password': 'python'}
    url = 'http://localhost:5678/consumer1/java-user'  # django api路径

    parms = {
        'name': '客户端',  # 发送给服务器的内容
    }

    headers = {  # 请求头 是浏览器正常的就行 就这里弄了一天 - -！
        'User-agent': 'none/ofyourbusiness',
        'Spam': 'Eggs'
    }

    resp = requests.post(url, data=parms, headers=headers)  # 发送请求

    # Decoded text returned by the request
    text = resp.text
    # print(json.loads(text))

    return Response(json.dumps(text), mimetype='application/json')
app.run('0.0.0.0', 3000)
app.run(port=3000, host='0.0.0.0')

