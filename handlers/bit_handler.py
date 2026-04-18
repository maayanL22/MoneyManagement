import json
import csv

from datetime import datetime

from managers.consts import BIT_FILE



class BitHandler:
    def __init__(self):
        self.header = {'id_column': 'id', 'date_column': 'date', 'amount_column': 'amount',
                       'method_column': 'method', 'description_column': 'description'} # method: transfer/acceptance/withdraw
        self.bit_file = BIT_FILE
        self.current_id = 0
        self.balance = 0

        try:
            with open(self.bit_file, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.header.keys())  # Write the header if the file is newly created
                print(f"Created new file: {self.bit_file}")
        except IOError as e:
            print(f"Could not open bit file")

    def add_transfer(self, amount: int, date: datetime, description: str):
        try:
            self._update_balance(amount, method)
        except ValueError as e:
            print(f"Error updating balance: {e}") # Change to log instead of print
        with open(self.bit_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.current_id, date, amount, 'transfer', description])

    def _update_balance(self, amount: int, method: str):
        if method in ['transfer-balance', 'withdraw']:
            if self.balance < amount:
                raise ValueError("Cannot transfer more than balance")
            self.balance += amount
        elif method == 'acceptance':
            if amount <= 0:
                raise ValueError("Accept non positive amount")
            self.balance += amount