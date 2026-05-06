from managers.income_manager import IncomeManager
from managers.io_manager import IOManager
from managers.money_manager import MoneyManager
from managers.outcome_manager import OutcomeManager


def main():
    io_manager = IOManager()
    income_manager = IncomeManager()
    outcome_manager = OutcomeManager()
    money_manager = MoneyManager(io_manager, income_manager, outcome_manager)

if __name__ == "__main__":
    main()
