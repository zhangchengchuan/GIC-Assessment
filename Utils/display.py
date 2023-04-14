from Utils.constants import WITHDRAW, DEPOSIT, PRINT, HEADERS

def display_welcome() -> None:
    print("Welcome to AwesomeGIC Bank! What would you like to do?")
    print("[D]eposit\n[W]ithdraw\n[P]rint Statement\n[Q]uit")

def display_transactions(return_values) -> None:
    for transactions in return_values:
        print(transactions)

def display_invalid_amount() -> None:
    print("Please enter a NUMERICAL value GREATER THAN 0.")

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
        # Calculate the column widths because different transaction different length.
        col_widths = [max(len(str(row[col])) for row in return_values) for col in HEADERS]
        header_widths = [len(header) for header in HEADERS]
        col_widths = [max(width, header_width) for width, header_width in zip(col_widths, header_widths)]

        # Print header and the rows
        print("| " + " | ".join(f"{header:<{width}}" for header, width in zip(HEADERS, col_widths)) + " |")
        for row in return_values:
            print("| " + " | ".join(f"{row[col]:<{width}}" for col, width in zip(HEADERS, col_widths)) + " |")

