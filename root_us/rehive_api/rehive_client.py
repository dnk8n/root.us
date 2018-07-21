from rehive import Rehive
import uuid

rehive_client = Rehive(token="cc18ad2a05760628eaff7fefd73857879e6abbddafa1f477fc453c55666e31db")

def who_am_i():
    return rehive_client.user.get()

def debit_account(amount):
    amount = amount * 100
    user = who_am_i()
    user_balance = user.get('balance', 0)
    currency = user.get('currency',{}).get('code','')
    if user_balance > 0 and user_balance >= amount:
        rehive_response = rehive_client.transactions.create_debit(
            amount=amount,
            currency=currency
        )
        print(rehive_response)
        if 'id' in rehive_response:
            return "Success"
        else:
            return "Failed"
    else:
        return "Not enough in balance"


def credit_account(amount):
    amount = amount * 100
    user = who_am_i()
    user_balance = user.get('balance', 0)
    currency = user.get('currency', {}).get('code', '')
    if user_balance > 0 and user_balance >= amount:
        rehive_response = rehive_client.transactions.create_credit(
            amount=amount,
            currency=currency
        )
        print(rehive_response)
        # if ['id', 'created'] in rehive_response.keys():
        if 'id' in rehive_response:
            return "Success"
            # return uuid.uuid4()
        else:
            return "Failed"
    else:
        return "Not enough in balance"