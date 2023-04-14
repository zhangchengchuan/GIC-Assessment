from Backend.command import Deposit_Command, Withdraw_Command, Print_Command
from Frontend.frontend_api import verify_input, format_output, add_to_queue, initialize_bank
from Utils.constants import INPUT_COMMAND, INPUT_AMOUNT, WITHDRAW, DEPOSIT, PRINT
from Backend.queue_driver import run_queue_driver
from Utils.display import display_welcome, display_continuation, display_termination, display_success, display_failure, display_invalid_amount
import logging

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s : %(levelname)s :%(message)s',
                        filename='bank.log',
                        filemode='w')

def main():
    display_welcome()
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
            if status:
                command = Withdraw_Command(amount)
            else:
                display_invalid_amount()
        elif user_input == 'd':
            format_output("Please enter amount:")
            status, amount = verify_input(input(), INPUT_AMOUNT)
            if status:
                command = Deposit_Command(amount)
            else:
                display_invalid_amount()
        elif user_input == 'p':
            command = Print_Command()
        else:
            format_output("Unexpected error")

        if command: 
            add_to_queue(command)
            status, return_values = run_queue_driver()

            if not status:
                # Show command has failed
                display_failure(command.command_type)
            else:
                display_success(command.command_type, return_values)
                    
        display_continuation()
    
    display_termination()

if __name__ == "__main__":
    main()