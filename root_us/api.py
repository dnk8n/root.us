from flask import Flask
# from root_us.rehive_client import rehive_client
import json
app = Flask(__name__)

@app.route("/")
def hello():
    response = {
        "message": "Welcome to the Root.us API"
    }
    return app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )
    # return "Welcome to the root.us APIs"


@app.route("/webhook")
def dialogflow_webhook(request):
    print(request.json())

