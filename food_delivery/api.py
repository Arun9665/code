
from flask import Flask, jsonify, request
import webview

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({"result": result})

if __name__ == '__main__':
    #app.run(debug=True)
    webview.start()
