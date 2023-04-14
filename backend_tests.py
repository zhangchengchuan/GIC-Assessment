import json
from Backend.backend import change_account, view_account, modify_payload
from Utils.constants import DEPOSIT, WITHDRAW, PRINT, DATABASE

def read_db():
    with open(DATABASE, "r") as db_reader:
        return json.load(db_reader)

def write_db(data):
    with open(DATABASE, "w") as db_writer:
        json.dump(data, db_writer, indent=4)

# Set up the database
def setup_module(module):
    write_db({
        "balance": 0,
        "number_of_transactions": 0,
        "transactions": []
    })

# Test cases for change_account
def test_change_account_deposit_no_initial_balance():
    initial_db = read_db()
    amount = 100
    status, transaction = change_account(amount, DEPOSIT)
    updated_db = read_db()
    print(updated_db['balance'])

    assert status
    assert updated_db["balance"] == initial_db["balance"] + amount
    assert updated_db["number_of_transactions"] == initial_db["number_of_transactions"] + 1

def test_change_account_deposit_with_initial_balance():
    initial_db = read_db()
    print(initial_db)
    amount_a = 100
    status, transaction = change_account(amount_a, DEPOSIT)
    initial_db_with_balance = read_db()
    initial_txn = initial_db_with_balance['number_of_transactions']
    initial_balance = initial_db_with_balance['balance']

    # Second deposit
    amount_b = 200
    status, transaction = change_account(amount_b, DEPOSIT)
    updated_db = read_db()

    assert status
    assert updated_db["balance"] == initial_balance + amount_b
    assert updated_db["number_of_transactions"] == initial_txn + 1

def test_change_account_withdraw_with_no_initial_balance():
    initial_db = read_db()
    amount = 50
    status, transaction = change_account(amount, WITHDRAW)
    updated_db = read_db()

    assert status
    assert updated_db["balance"] == initial_db["balance"] - amount
    assert updated_db["number_of_transactions"] == initial_db["number_of_transactions"] + 1

def test_change_account_withdraw_with_initial_balance():
    initial_db = read_db()
    amount_a = 200
    status, transaction = change_account(amount_a, DEPOSIT)
    initial_db_with_balance = read_db()
    initial_balance = initial_db_with_balance['balance']
    initial_txn = initial_db_with_balance['number_of_transactions']

    amount_b = 100
    status, transaction = change_account(amount_b, WITHDRAW)
    updated_db = read_db()

    assert status
    assert updated_db["balance"] == initial_balance - amount_b
    assert updated_db["number_of_transactions"] == initial_txn + 1

def test_change_account_withdraw_fail():
    initial_db = read_db()
    amount = 1000
    status, transaction = change_account(amount, WITHDRAW)

    assert not status
    assert transaction is None

# Test cases for view_account
def test_view_account():
    initial_db = read_db()
    status, transactions = view_account()

    assert status
    assert transactions == initial_db["transactions"]

def test_view_account_no_transactions():
    write_db({"balance": 0, "number_of_transactions": 0, "transactions": []})
    status, transactions = view_account()

    assert not status
    assert transactions is None

# Test cases for modify_payload
def test_modify_payload():
    initial_db = read_db()
    initial_balance = initial_db['balance']
    initial_txn = initial_db['number_of_transactions']
    amount = 100
    status, modified_payload = modify_payload(initial_db, amount)

    assert status
    assert modified_payload["balance"] == initial_balance + amount
    assert modified_payload["number_of_transactions"] == initial_txn + 1

def test_modify_payload_fail():
    initial_db = read_db()
    amount = -1000
    status, modified_payload = modify_payload(initial_db, amount)

    assert not status
    assert modified_payload is None