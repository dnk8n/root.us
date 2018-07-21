from flask import Flask
from flask import request
from .rehive_client import rehive_client, who_am_i
# import rehive_client
from .dialogflow_fulfillment import make_fulfillment

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


@app.route("/webhook", methods=['POST'])
def dialogflow_webhook():
    # print(request.json())
    webhook_req = request.get_json()
    print(json.dumps(webhook_req))

    intent = webhook_req.get('queryResult', {}).get('intent', {}).get('displayName', None)

    if  intent == "Wallet Balance":
        user_detail = who_am_i()
        print(json.dumps(user_detail))

        return app.response_class(
            response=json.dumps(make_fulfillment("Your balance is: {}{}".format(
                user_detail.get("currency", {}).get("symbol", None),
                user_detail.get('balance',0)/100))
            ),
            status=200,
            mimetype='application/json'
        )
    elif intent == "Who Am I":
        print("Entered who am I?")
        user_detail = who_am_i()
        user_detail = "Your name: {name}, last name: {surname}, email: {email} and currency: {currency} ".format(
            name=user_detail.get("first_name", None),
            surname=user_detail.get("last_name", None),
            email=user_detail.get("email", None),
            currency=user_detail.get("currency", {}).get("code", None)
        )
        print("User detail 2:", user_detail)
        fullfillment = make_fulfillment(user_detail)
        return app.response_class(
            response=json.dumps(fullfillment),
            status=200,
            mimetype='application/json'
        )




