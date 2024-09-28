#!/usr/bin/env python3
""" This is a basic flask app """
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def data():
    sample = jsonify({"message": "Bienvenue"})
    return sample

@app.route('/users', methods=['POST'])
def users():
    """ this will help me to register user for my app """
    try:
        data = request.get_json()
        if data is None:
            pass
        email = data.get("email")
        password = data.get("password")
        
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
