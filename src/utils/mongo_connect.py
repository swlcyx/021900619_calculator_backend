from mongoengine import *


def mongo_connect(db_config):
    for db_c in db_config:
        connect(**db_c)
