import json
import time
from typing import Tuple
from constants import DATABASE, DEPOSIT, WITHDRAW

def change_account(amount, change_type) -> bool:
    change_amount = 0
    if change_type is DEPOSIT:
        change_amount = amount
    elif change_type is WITHDRAW:
        change_amount = amount * -1

    # Get db instance
    with open(DATABASE, 'r') as db_reader:
        payload = json.load(db_reader) 

    # Guard clause
    if payload['balance'] + change_amount < 0:
        return False
    
    status, modified_payload = modify_payload(payload, change_amount)

    if status:
        # Write new payload to db
        with open(DATABASE, 'w') as db_writer:
            json.dump(modified_payload, db_writer, indent=4)
        return True
    
    # Withdraw greater than balance
    else:
        return False

def view_account()->Tuple[bool, list]:
    print("Accessing View Account")
    # Get db instance
    transactions = None
    with open(DATABASE, 'r') as db_reader:
        payload = json.load(db_reader) 
        transactions = payload['transactions']
    
    if transactions:
        return (True, transactions)
    else:
        return (False, None)

def modify_payload(payload, amount) -> Tuple[bool, dict]:
    new_balance = payload['balance'] + amount
    if new_balance < 0:
        return (False, None)

    payload['balance'] = new_balance
    payload['number_of_transactions'] += 1
    payload['transactions'].append({
        'time': time.ctime(time.time()),
        'amount': f"${amount}",
        'balance': f"${new_balance}"
    })

    return (True, payload)