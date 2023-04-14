import os
import pickle
import json
from Utils.constants import INPUT_AMOUNT, INPUT_COMMAND, VALID_COMMANDS, QUEUE, DATABASE
from Frontend.frontend_api import initialize_bank, verify_input, add_to_queue

# Test cases for initialize_bank
def test_initialize_bank():
    # Call initialize_bank
    initialize_bank()

    # Check if the test database and queue files exist and have the correct content
    assert os.path.exists(DATABASE)
    assert os.path.exists(QUEUE)

    with open(DATABASE, 'r') as db_reader:
        payload = json.load(db_reader)
        assert payload == {"balance": 0, "number_of_transactions": 0, "transactions": []}

    with open(QUEUE, 'rb') as q_reader:
        queue = pickle.load(q_reader)
        assert queue == []

# Test cases for verify_input
def test_verify_input_command():
    result, value = verify_input("q", INPUT_COMMAND)
    assert result and value == "q"

    result, value = verify_input("w", INPUT_COMMAND)
    assert result and value == "w"

    result, value = verify_input("d", INPUT_COMMAND)
    assert result and value == "d"

    result, value = verify_input("p", INPUT_COMMAND)
    assert result and value == "p"

    result, value = verify_input("unknown", INPUT_COMMAND)
    assert not result and value is None

    result, value = verify_input("AJSJDJASDJSJSDJSADJ", INPUT_COMMAND)
    assert not result and value is None

    result, value = verify_input("-100000000000000.129318239", INPUT_COMMAND)
    assert not result and value is None

    result, value = verify_input("qq", INPUT_COMMAND)
    assert not result and value is None

def test_verify_input_amount():
    result, value = verify_input("100", INPUT_AMOUNT)
    assert result and value == 100.0

    result, value = verify_input("12312031023012031023.012341234123413241", INPUT_AMOUNT)
    assert result and value == 12312031023012031023.012341234123413241

    result, value = verify_input("0.01244", INPUT_AMOUNT)
    assert result and value == 0.01244

    result, value = verify_input("123.4123", INPUT_AMOUNT)
    assert result and value == 123.4123

    result, value = verify_input("-0.0000001", INPUT_AMOUNT)
    assert not result and value is None

    result, value = verify_input("-50.123", INPUT_AMOUNT)
    assert not result and value is None

    result, value = verify_input("-1.5", INPUT_AMOUNT)
    assert not result and value is None

    result, value = verify_input("JAJAJAJAJA", INPUT_AMOUNT)
    assert not result and value is None

    result, value = verify_input("123412398ads80fa0df8", INPUT_AMOUNT)
    assert not result and value is None

    result, value = verify_input("invalid", INPUT_AMOUNT)
    assert not result and value is None

# Test cases for add_to_queue
def test_add_to_queue():

    # Initialize the test queue
    with open(QUEUE, 'wb') as q_writer:
        pickle.dump([], q_writer)

    command = {"command_type": "deposit", "amount": 100}
    add_to_queue(command)

    with open(QUEUE, 'rb') as q_reader:
        queue = pickle.load(q_reader)
        assert len(queue) == 1
        assert queue[0] == command