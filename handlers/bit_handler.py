import json
import csv

from datetime import datetime

from managers.consts import BIT_FILE



class BitHandler:
    def __init__(self):
        self.header = {'id_column': 'id', 'date_column': 'date', 'amount_column': 'amount',
                       'method_column': 'method', 'description_column': 'description'}
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
        with open(self.bit_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.current_id, date, amount, 'transfer', description])

