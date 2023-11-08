#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/11/1 10:20
# file: course_list.py
# author: 孙伟亮
# email: 2849068933@qq.com
from flask import request
import json
import time
from src.utils.flask_app import app
from src.models import History


@app.route('/get_history_list/', methods=['GET'])
def get_history_list():
    try:
        history = History.objects().order_by("-update_time").limit(10)
        history = [{"expression": i.expression, "result": i.result} for i in history]
        return history
    except Exception as e:
        return {"code": 401,
                "data": {
                    "msg": str(e)
                }}


@app.route('/calculate/', methods=['POST'])
def calculate():
    try:
        result_data = json.loads(request.data)
        expression = result_data.get("expression")
        history = History.objects().order_by("-update_time").limit(1).first()
        if "Ans" in expression:
            if not history:
                return {"code": 500, "error": "没有ans"}
            Ans = history.result
        try:
            res = eval(expression.replace('%', '/100').replace('x', '*').replace('^', '**'))
            History(expression=expression, result=res, update_time=time.time()).save()
            return {"code": 200, "data": {"result": res, "expression": expression}}
        except ZeroDivisionError:
            return {"code": 500, "error": "0不能作为除数"}
        except SyntaxError:
            return {"code": 500, "error": "表达式错误"}
        except Exception:
            return {"code": 500, "error": "表达式错误"}
    except Exception as e:
        return {"state": 401,
                "data": {
                    "msg": str(e)
                }}
