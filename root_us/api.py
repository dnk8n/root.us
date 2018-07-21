from flask import Flask
# import rehive_client
from .endpoints.webhook import webhook_blueprint
from .google_maps.google_maps import gmaps_client

import json
app = Flask(__name__)

app.register_blueprint(webhook_blueprint)

@app.route("/")
def hello():
    response = {
        "message": "Welcome to the Root.us API"
    }
    print(gmaps_client.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    )
    return app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )
    # return "Welcome to the root.us APIs"






