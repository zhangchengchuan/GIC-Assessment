from command import Deposit_Command, Withdraw_Command, Print_Command
from utils import verify_input, format_output, display, add_to_queue, initialize_bank 
from constants import INPUT_COMMAND, INPUT_AMOUNT # Change this
from backend import run_backend
from logger import getLogger

def main():
    print("Hello World")
    print("Welcome to GIC Bank")
    initialize_bank()
    looping = True
    while looping:
        format_output("What would you like to do?")
        status, user_input = verify_input(input(), INPUT_COMMAND)
        # Guard clause
        if not status:
            format_output("Invalid Input. Please try again.")
            continue

        if user_input == 'q':
            break


        command = None
        if user_input == 'w':
            format_output("Please enter amount:")
            status, amount = verify_input(input(), INPUT_AMOUNT)
            command = Withdraw_Command(amount)
        elif user_input == 'd':
            format_output("Please enter amount:")
            status, amount = verify_input(input(), INPUT_AMOUNT)
            command = Deposit_Command(amount)
        elif user_input == 'p':
            command = Print_Command()
        else:
            format_output("Unexpected error")

        if command: 
            add_to_queue(command)
            status, return_values = run_backend()

            if not status:
                # Show command has failed
                print("failed command")
            else:
                print("successful command")
                if return_values:
                    display(return_values)
            # format_output("Successfully Executed Command")

        # TODO: format output for each successful command of adding to queue.

    
    print("Thank you for banking with us.")

if __name__ == "__main__":
    main()