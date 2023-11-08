from flask import Flask
from src.utils.json_tools import read_json

config = read_json("config/config.json")

app = Flask(__name__)
