import pickle
import logging
import json
from Utils.constants import INPUT_AMOUNT, INPUT_COMMAND, VALID_COMMANDS, QUEUE, DATABASE
from typing import Tuple

def initialize_bank():
    """
    Initialize the bank's database and queue.
    
    This function creates and initializes the database with an initial payload
    and an empty queue.
    """
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

    # Initialize Queue
    q_writer = open(QUEUE, 'wb')
    q_writer.truncate(0)
    pickle.dump([], q_writer)

    logging.info("Successful Initialization of Database and Queue")

def verify_input(input, input_type) -> Tuple[bool, str]:
    """
    Verify the input based on the specified input type.
    
    Args:
        input (str): The input to be verified.
        input_type (str): The type of input to be verified (INPUT_COMMAND or INPUT_AMOUNT).
    
    Returns:
        Tuple containing a boolean indicating if the input is valid and the formatted input value.
    """
    input = input.strip()
    if input_type == INPUT_COMMAND:
        return (True, input.lower()) if input.lower() in VALID_COMMANDS else (False, None)
    elif input_type == INPUT_AMOUNT:
        try:
            amount = float(input)
            return (False, None) if amount < 0 else (True, amount)
        except ValueError:
            return (False, None)
    else:
        return (False, None)

def add_to_queue(command):
    """
    Add a command to the queue.
    
    Args:
        command: The command object to be added to the queue.
    """
    q_reader = open(QUEUE, 'rb')
    current_queue = pickle.load(q_reader)
    q_reader.close()

    q_writer = open(QUEUE, 'wb')
    current_queue.append(command)
    pickle.dump(current_queue, q_writer)
    q_writer.close()
    logging.info(f"Successfully added {command} to queue.")

def format_output(message) -> None:
    """
    Format and print the output message.
    
    Args:
        message (str): The message to be formatted and printed.
    """
    print(f"{message}\n")
