import json
import time
import logging
from typing import Tuple
from Utils.constants import DATABASE, DEPOSIT, WITHDRAW

def change_account(amount, change_type) -> Tuple[bool, list]:
    """
    Change the account balance based on the specified change_type (DEPOSIT/WITHDRAW).

    Args:
        amount: The amount to deposit or withdraw.
        change_type: The type of change (DEPOSIT/WITHDRAW).

    Returns:
        Tuple containing status (True/False) and amount, if successful.
    """
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

def view_account() -> Tuple[bool, list]:
    """
    Retrieve and return account transaction history.

    Returns:
        Tuple containing status (True/False) and a list of transactions, if any.
    """
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
    """
    Modify the payload based on the given amount and update the transaction history.

    Args:
        payload: The current payload.
        amount: The amount to be added or subtracted from the balance.

    Returns:
        Tuple containing status (True/False) and modified payload.
    """
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
