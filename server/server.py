import requests
import os
from flask import Flask, jsonify

app = Flask(__name__)


''' MISC '''
@app.route('/')
def hello():
    return 'Hello!'


if __name__ == "__main__":
    app.run(debug=True)