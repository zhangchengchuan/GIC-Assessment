import json
import time
import logging
from typing import Tuple
from Utils.constants import DATABASE, DEPOSIT, WITHDRAW

def change_account(amount, change_type) -> Tuple[bool, list]:
    change_amount = 0
    if change_type is DEPOSIT:
        change_amount = amount
    elif change_type is WITHDRAW:
        change_amount = amount * -1

    # Get db instance
    with open(DATABASE, 'r') as db_reader:
        payload = json.load(db_reader) 
    
    status, modified_payload = modify_payload(payload, change_amount)

    if status:
        # Write new payload to db
        with open(DATABASE, 'w') as db_writer:
            json.dump(modified_payload, db_writer, indent=4)
        logging.info("Successfully written new payload to database")
        return True, [amount]
    
    # Withdraw greater than balance
    else:
        return False, None

def view_account()->Tuple[bool, list]:
    # Get db instance
    transactions = None
    with open(DATABASE, 'r') as db_reader:
        payload = json.load(db_reader) 
        transactions = payload['transactions']
    
    if transactions:
        logging.info("Successfully fetched previous transactions.")
        return (True, transactions)
    else:
        logging.warning("There is no previous transactions.")
        return (False, None)

def modify_payload(payload, amount) -> Tuple[bool, dict]:
    new_balance = payload['balance'] + amount
    if new_balance < 0:
        logging.warning("Withdrawal amount greater than balance.")
        return (False, None)

    payload['balance'] = new_balance
    payload['number_of_transactions'] += 1
    payload['transactions'].append({
        'time': time.ctime(time.time()),
        'amount': f"{amount}",
        'balance': f"{new_balance}"
    })

    logging.info("Payload has been modified.")
    return (True, payload)