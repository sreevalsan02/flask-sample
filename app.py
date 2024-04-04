from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def hello():
  
  return "hello you are in root page"

@app.route('/message')

def message():
  return "hi message"

if __name__ == '__main__':
  app.run(debug=True)