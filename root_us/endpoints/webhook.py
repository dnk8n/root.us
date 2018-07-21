from flask import Blueprint, request
from ..rehive_client import rehive_client, who_am_i
# import rehive_client
from ..dialogflow_fulfillment import make_fulfillment
from ..intents.user_intents import wallet_fullfilment, who_am_i_fullfillment
# from ..api import app
import json
from flask import current_app

app = current_app

webhook_blueprint = Blueprint('webhook', __name__)

@webhook_blueprint.route("/webhook", methods=['POST'])
def dialogflow_webhook():
    # print(request.json())
    webhook_req = request.get_json()
    print(json.dumps(webhook_req))

    intent = webhook_req.get('queryResult', {}).get('intent', {}).get('displayName', None)

    if  intent == "Wallet Balance":

        return app.response_class(
            response=json.dumps(wallet_fullfilment()
            ),
            status=200,
            mimetype='application/json'
        )
    elif intent == "Who Am I":
        return app.response_class(
            response=json.dumps(who_am_i_fullfillment()),
            status=200,
            mimetype='application/json'
        )
