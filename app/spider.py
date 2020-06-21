#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
import json
import requests
import base64


def get_cookies():
    url = 'https://jxfw.gdut.edu.cn/'
    response = requests.get(url, verify=False)
    return response.cookies.get_dict()


def get_verify_code(cookies):
    current_time = int(time.time()*1000)
    url = 'http://jxfw.gdut.edu.cn/yzm?d={current_time}'.format(
        current_time=current_time)
    response = requests.get(url, cookies=cookies, verify=False)
    verify_code_img = 'data:image/png;base64,' + \
        base64.b64encode(response.content).decode()
    return verify_code_img


def login(account, pwd, verifycode, cookies):
    data = {
        'account': account,
        'pwd': pwd,
        'verifycode': verifycode
    }
    url = 'https://jxfw.gdut.edu.cn/new/login'
    response = requests.post(url, data=data, cookies=cookies, verify=False)
    return json.loads(response.text)['message']


def get_score(cookies):
    url = 'https://jxfw.gdut.edu.cn/xskccjxx!getDataList.action'
    data = {
        'xnxqdm': '201901',
        'jhlxdm': '01',
        'page': '1',
        'rows': '11',
        'sort': 'xnxqdm',
        'order': 'asc'
    }
    response = requests.post(url, data=data, cookies=cookies, verify=False)
    datas = response.text
    datas = json.loads(datas)

    sum_score = 0
    sum_rank = 0
    for data in datas['rows']:
        score = float(data['cjjd'])
        rank = float(data['xf'])
        sum_score += score * rank
        sum_rank += rank
    avg_score = round(sum_score / sum_rank, 2)
    datas['avg_score'] = str(avg_score)
    return datas
