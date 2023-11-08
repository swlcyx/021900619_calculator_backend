#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/11/8 16:12
# file: rate_calculate.py
# author: 孙伟亮
# email: 2849068933@qq.com
from flask import request
import json
from src.models import Rate
from src.utils.flask_app import app


@app.route('/get_rate/', methods=['GET'])
def get_rate():
    try:
        ck_rate = Rate.objects(t="存款").first()
        dk_rate = Rate.objects(t="贷款").first()
        return {"code": 200, "ck": ck_rate.rate, "dk": dk_rate.rate}
    except Exception as e:
        return {"code": 401,
                "data": {
                    "msg": str(e)
                }}


@app.route('/calculate_ck/', methods=['POST'])
def calculate_ck():
    try:
        result_data = json.loads(request.data)
        ck = result_data.get("ck")
        c_type = ck.get("c_type")
        year = ck.get("year")
        rate = ck.get("rate", {})
        money = ck.get("money")
        ck_rate = Rate.objects(t="存款").first()
        ck_rate.rate = rate
        ck_rate.save()
        if c_type == "活期":
            return {"code": 200, "result": float(rate.get("huoqi_rate")) * float(money) * float(year)/100.0}
        elif c_type == "活期":
            if year == "three_month":
                year = 0.25
            elif year == "half_year":
                year = 0.5
            elif year == "one_year":
                year = 1
            elif year == "two_year":
                year = 2
            elif year == "three_year":
                year = 3
            elif year == "five_year":
                year = 5
            return {"code": 200, "result": float(rate.get("huoqi_rate")) * float(money) * year/100.0}


    except Exception as e:
        return {"state": 401,
                "data": {
                    "msg": str(e)
                }}


@app.route('/calculate_dk/', methods=['POST'])
def calculate_dk():
    try:
        result_data = json.loads(request.data)
        ck = result_data.get("dk")
        year = ck.get("year")
        rate = ck.get("rate", {})
        money = ck.get("money")
        dk_rate = Rate.objects(t="贷款").first()
        dk_rate.rate = rate
        dk_rate.save()

        if year == "half_year":
            year = 0.5
            r = rate.get("half_year")
        elif year == "one_year":
            year = 1
            r = rate.get("one_year")
        elif year == "two_year":
            year = 2
            r = rate.get("one_three_year")
        elif year == "three_year":
            year = 3
            r = rate.get("three_five_year")
        elif year == "four_year":
            year = 4
            r = rate.get("three_five_year")
        elif year == "five_year":
            year = 5
            r = rate.get("five_year")
        return {"code": 200, "result": float(r) * float(money) * year/100.0}


    except Exception as e:
        return {"state": 401,
                "data": {
                    "msg": str(e)
                }}
