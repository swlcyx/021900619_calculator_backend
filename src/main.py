#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/11/1 10:17
# file: main.py
# author: 孙伟亮
# email: 2849068933@qq.com
from src.utils.mongo_connect import mongo_connect
from flask_cors import CORS

CORS(app, supports_credentials=True)

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)


if __name__ == '__main__':
    config = read_json("config/config.json")
    mongo_connect(config.get("db", []))
    server_port = config.get("server_port")
    # 多进程
    app.run(host="0.0.0.0", port=server_port, threaded=True)
