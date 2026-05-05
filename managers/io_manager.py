import json
import csv

from consts import *

class IOManager:
    def __init__(self):
        self.money_file_path = MAIN_FILE_PATH
        self.income_file_path = INCOME_FILE_PATH
        self.expenses_file_path = EXPENSES_FILE_PATH

    def get_balance(self):
        """
        Receive money balance from the money file
        :return: Money balance
        """
        with open(self.money_file_path, "r") as main_file:
            data = json.load(main_file)

        return data["balance"]

    def change_balance(self, amount_to_change):
        with open(self.money_file_path, "r") as money_file:
            current_data = json.load(money_file)

        current_data["balance"] += amount_to_change

        with open(self.money_file_path, "w") as money_file:
            json.dump(current_data, money_file)