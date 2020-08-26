from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/covid')
def tracker():
    data = dict(
        total=1000,
        activecases=100,
        recovery=800,
        deaths=50,
        newcases=50
    )
    return jsonify(data)