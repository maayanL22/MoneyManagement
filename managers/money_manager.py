from datetime import datetime

from managers.io_manager import IOManager
from managers.income_manager import IncomeManager
from managers.outcome_manager import OutcomeManager


class MoneyManager():
    def __init__(self, io_manager, income_manager, outcome_manager):
        print("Initializing MoneyManager")
        self.io_manager = io_manager
        self.income_manager = income_manager
        self.outcome_manager = outcome_manager
        print("MoneyManager initialized")

    def get_balance(self):
        return self.io_manager.get_balance()

    def write_income(self, income: int, date: datetime, description: str):
        return self.income_manager.write_income(income, date, description)

    def get_monthly_income(self, month: int):
        return self.income_manager.get_monthly_income(month)

    def write_outcome(self, outcome: int, date: datetime, description: str):
        return self.outcome_manager.write_outcome(outcome, date, description)

    def get_monthly_outcome(self, month: int):
        return self.outcome_manager.get_monthly_outcome(month)

    def get_monthly_balance(self, month: int):
        return self.get_monthly_income(month) - self.get_monthly_outcome(month)

    def get_current_month_balance(self):
        return self.get_monthly_balance(datetime.now().month)