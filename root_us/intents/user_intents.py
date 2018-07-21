from ..dialogflow_fulfillment import make_fulfillment
from ..rehive_api.rehive_client import who_am_i, debit_account
import json
from ..local_settings import REDIS_CLIENT
# from flask import

def wallet_fullfilment():
    user_detail = who_am_i()
    print(json.dumps(user_detail))

    return make_fulfillment("Your balance is: {}{}".format(
            user_detail.get("currency", {}).get("symbol", None),
            user_detail.get('balance', 0) / 100)
    )
def who_am_i_fullfillment():
    user_detail = who_am_i()
    user_detail = "Your name: {name}, last name: {surname}, email: {email} and currency: {currency} ".format(
        name=user_detail.get("first_name", None),
        surname=user_detail.get("last_name", None),
        email=user_detail.get("email", None),
        currency=user_detail.get("currency", {}).get("code", None)
    )
    print("User detail 2:", user_detail)
    return make_fulfillment(user_detail)

# def buy_voucher(amount):
#     user_email = who_am_i().get('Email', None)
#     if not REDIS_CLIENT.exist('user_email'):
#         debit_resp = debit_account(amount)
#     #
#     else:
#         return "Existing voucher"


