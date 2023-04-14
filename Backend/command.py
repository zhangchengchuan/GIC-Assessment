from typing import Tuple
from Backend.backend import change_account, view_account
from Utils.constants import DEPOSIT, WITHDRAW, PRINT

class Command:
    """
    An abstract base class representing a command.
    """
    def execute(self) -> None:
        """
        Execute the command. Override this method in concrete commands.
        """
        pass

class Deposit_Command(Command):
    """
    A concrete command to deposit a specified amount into the account.
    """
    def __init__(self, amount) -> None:
        self.amount = amount
        self.command_type = DEPOSIT

    def execute(self) -> Tuple[bool, list]:
        """
        Execute the deposit command by calling the change_account function.

        Returns:
            Tuple containing status (True/False) and amount, if successful.
        """
        status, amount = change_account(self.amount, DEPOSIT)
        return (status, amount)

class Withdraw_Command(Command):
    """
    A concrete command to withdraw a specified amount from the account.
    """
    def __init__(self, amount) -> None:
        self.amount = amount
        self.command_type = WITHDRAW

    def execute(self) -> Tuple[bool, list]:
        """
        Execute the withdraw command by calling the change_account function.

        Returns:
            Tuple containing status (True/False) and amount, if successful.
        """
        status, amount = change_account(self.amount, WITHDRAW)
        return (status, amount)

class Print_Command(Command):
    """
    A concrete command to print the account transaction history.
    """
    def __init__(self) -> None:
        self.command_type = PRINT
        self.amount = 0

    def execute(self) -> Tuple[bool, list]:
        """
        Execute the print command by calling the view_account function.

        Returns:
            Tuple containing status (True/False) and a list of transactions, if any.
        """
        status, transactions = view_account()
        return (status, transactions)
