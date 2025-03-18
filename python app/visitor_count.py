from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!'

if __name__ == '__main__':
    app.run(debug=True)
