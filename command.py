from typing import Tuple
from utils import format_output
from backend_api import change_account, view_account
from constants import DEPOSIT, WITHDRAW

# @abstractmethod
class Command:
    def execute(self) -> None:
        # Do nothing
        pass

# Concrete commands
class Deposit_Command(Command):
    def __init__(self, amount) -> None:
        self.amount = amount

    def execute(self) -> Tuple[bool, list]:
        status = change_account(self.amount, DEPOSIT)
        return (status, None)

class Withdraw_Command(Command):
    def __init__(self, amount) -> None:
        self.amount = amount

    def execute(self) -> Tuple[bool, list]:
        status = change_account(self.amount, WITHDRAW)
        return (status, None)

class Print_Command(Command):
    def __init__(self) -> None:
        pass

    def execute(self) -> Tuple[bool, list]:
        status, transactions = view_account()
        return (status, transactions)






    
