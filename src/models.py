#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/10/31 18:17
# file: models.py
# author: 孙伟亮
# email: 2849068933@qq.com
from mongoengine import *


class History(DynamicDocument):
    expression = StringField()
    result = FloatField()
    update_time = FloatField()
    meta = {"collection": "history", "db_alias": "history", "indexes": [
    ]}


class Rate(DynamicDocument):
    t = StringField()
    rate = DictField()
    meta = {"collection": "rate", "db_alias": "rate", "indexes": [
    ]}
