from flask import Flask
# from flask import app

app = Flask(__name__)

@app.route("/")
def hello():
    return {
        "message": "Welcome to the Root.us API"
    }

