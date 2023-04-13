from typing import Tuple
from Frontend.frontend_api import format_output
from Backend.backend_api import change_account, view_account
from Utils.constants import DEPOSIT, WITHDRAW

# Abstract command
class Command:
    def execute(self) -> None:
        # Do nothing
        pass

# Concrete commands
class Deposit_Command(Command):
    def __init__(self, amount) -> None:
        self.amount = amount

    def execute(self) -> Tuple[bool, list]:
        status, amount = change_account(self.amount, DEPOSIT)
        return (status, amount)

class Withdraw_Command(Command):
    def __init__(self, amount) -> None:
        self.amount = amount

    def execute(self) -> Tuple[bool, list]:
        status, amount = change_account(self.amount, WITHDRAW)
        return (status, amount)

class Print_Command(Command):
    def __init__(self) -> None:
        pass

    def execute(self) -> Tuple[bool, list]:
        status, transactions = view_account()
        return (status, transactions)






    
