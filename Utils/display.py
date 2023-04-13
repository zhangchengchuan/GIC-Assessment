from Utils.constants import WITHDRAW, DEPOSIT, PRINT

def display_welcome() -> None:
    print("Welcome to AwesomeGIC Bank! What would you like to do?")
    print("[D]eposit\n[W]ithdraw\n[P]rint Statement\n[Q]uit")

def display_transactions(return_values) -> None:
    for transactions in return_values:
        print(transactions)

def display_invalid_amount() -> None:
    print("Please enter a value greater than 0.")

def display_continuation() -> None:
    print("\nIs there anything else you'd like to do?")
    print("[D]eposit\n[W]ithdraw\n[P]rint Statement\n[Q]uit")

def display_termination() -> None:
    print("Thank you for banking with AwesomeGIC Bank.\nHave a nice day!")

def display_failure(command_type) -> None:
    if command_type == WITHDRAW:
        print(f"Failed to withdraw.")
    elif command_type == DEPOSIT:
        print(f"Failed to deposit.")
    elif command_type == PRINT:
        print("Failed to display previous transactions")

def display_success(command_type, return_values) -> None:
    if command_type == WITHDRAW:
        print(f"Successfully withdrawn ${return_values[0]}")
    elif command_type == DEPOSIT:
        print(f"Successfully deposited ${return_values[0]}")
    elif command_type == PRINT:
        for transaction in return_values:
            # print(f"Date:{" "*20}| Amount |")
            print(transaction)

