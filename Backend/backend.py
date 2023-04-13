import pickle
from typing import Tuple
from Utils.constants import *
from Backend.command import Withdraw_Command, Deposit_Command, Print_Command

def run_backend() -> Tuple[bool, list]:
    # Get the current queue.
    queue = None
    with open(QUEUE, 'rb') as q_reader:
        queue = pickle.load(q_reader)
        if not queue:
            print("Error fetching queue")

    # Execute commands in the queue
    # However, in this case only one command in "queue" due to system constraints.
    command = queue[0]
    queue.pop(0)
    status, return_val = command.execute()
        
    # Truncate the queue file.
    with open(QUEUE, 'wb') as q_writer:
        pickle.dump([], q_writer)

    if status:
        return (True, return_val)
    else:
        return (False, None)
    



