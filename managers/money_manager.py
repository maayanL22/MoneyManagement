from datetime import datetime

from io_manager import IOManager
from income_manager import IncomeManager
from outcome_manager import OutcomeManager


class MoneyManager(IOManager):
    def __init__(self, io_manager, income_manager, outcome_manager):
        self.io_manager = io_manager
        self.income_manager = income_manager
        self.outcome_manager = outcome_manager

    def get_balance(self):
        return self.io_manager.get_balance()

    def write_income(self, income: int, date: datetime, description: str):
        return self.income_manager.write_income(income, date, description)

    def get_monthly_income(self, month: int):
        return self.income_manager.get_monthly_income(month)

