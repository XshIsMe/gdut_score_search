#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from flask import Flask, render_template, request, make_response
from spider import get_cookies, login, get_score, get_verify_code
from aes import aes

app = Flask(__name__)


def cookies():
    return {'JSESSIONID': request.cookies['JSESSIONID']}


@app.route('/refresh_verify_code/')
def refresh_verify_code():
    verify_code_img = get_verify_code(cookies())
    return verify_code_img


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'GET' == request.method:
        response = make_response(render_template('index.html'))
        response.set_cookie('JSESSIONID', get_cookies()['JSESSIONID'])
        return response
    else:
        data = request.form.to_dict()
        account, pwd, verifycode = data['username'], aes(
            data['verify_code'], data['password']), data['verify_code']
        result = login(account, pwd, verifycode, cookies())

        if '登录成功' == result:
            return get_score(cookies())
        else:
            return result, 403


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
