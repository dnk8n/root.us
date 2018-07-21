
def make_fulfillment(message):
    fullfillment_tempalte = dict({
          "fulfillmentText": message,
          "fulfillmentMessages": [
            {
              "card": {
                "title": "Response",
                "subtitle": message,
                "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                "buttons": [
                  {
                    "text": "button text",
                    "postback": "https://assistant.google.com/"
                  }
                ]
              }
            }
          ],
          # "source": "example.com",
          "payload": {
            "google": {
              "expectUserResponse": True,
              "richResponse": {
                "items": [
                  {
                    "simpleResponse": {
                      "textToSpeech": message
                    }
                  }
                ]
              }
            },
            "facebook": {
              "text": message
            },
            "slack": {
              "text": message
            }
          },
          # "outputContexts": [
          #   {
          #     "name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
          #     "lifespanCount": 5,
          #     "parameters": {
          #       "param": "param value"
          #     }
          #   }
          # ],
          # "followupEventInput": {
          #   "name": "event name",
          #   "languageCode": "en-US",
          #   # "parameters": {
          #   #   "param": "param value"
          #   # }
          # }
        }
    )
    return fullfillment_tempalte