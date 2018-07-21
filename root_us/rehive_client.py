from rehive import Rehive

rehive_client = Rehive(token="cc18ad2a05760628eaff7fefd73857879e6abbddafa1f477fc453c55666e31db")

def who_am_i():
    return rehive_client.user.get()