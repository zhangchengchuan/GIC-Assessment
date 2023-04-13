import pickle
import json
from constants import INPUT_AMOUNT, INPUT_COMMAND, VALID_COMMANDS, QUEUE, DATABASE
from typing import Tuple

def initialize_bank():
    # Initialize Backend


    # Initialize DB
    db_writer = open(DATABASE, 'w')
    db_writer.truncate(0)
    payload = {
        "balance": 0,
        "number_of_transactions": 0,
        "transactions": []
    }
    json.dump(payload, db_writer)
    db_writer.close()
    # TODO: Log status

    # Initialize Queue
    q_writer = open(QUEUE, 'wb')
    q_writer.truncate(0)
    pickle.dump([], q_writer)
    # TODO: Log status

def verify_input(input, input_type) -> Tuple[bool, str]:
    if input_type == INPUT_COMMAND:
        if input.lower() in VALID_COMMANDS:
            return (True, input.lower())
    elif input_type == INPUT_AMOUNT:
        try:
            amount = float(input)
            return (False, None) if amount < 0 else (True, amount)
        except ValueError:
            return (False, None)

    return (False, None)

def add_to_queue(command):
    q_reader = open(QUEUE, 'rb')
    current_queue = pickle.load(q_reader)
    q_reader.close()

    q_writer = open(QUEUE, 'wb')
    current_queue.append(command)
    pickle.dump(current_queue, q_writer)
    q_writer.close()

    # TODO: Log to logger file

def format_output(message) -> None:
    # print("*******************************")
    print(f"** {message}\n")
    # print("*******************************\n")

def display(return_values) -> None:
    for transactions in return_values:
        print(transactions)