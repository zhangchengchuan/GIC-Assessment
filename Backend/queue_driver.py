import pickle
from typing import Tuple
from Utils.constants import QUEUE

def run_queue_driver() -> Tuple[bool, list]:
    """
    Run the queue driver to process commands in the queue.
    
    The queue driver fetches the commands from the queue, executes them, and then
    updates the queue. Due to system constraints, only one command is processed
    in the queue.

    Returns:
        Tuple containing status (True/False) and a list of return values from the executed command.
    """
    # Get the current queue.
    queue = None
    with open(QUEUE, 'rb') as q_reader:
        queue = pickle.load(q_reader)
        if not queue:
            print("Error fetching queue")

    # Get the command
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
