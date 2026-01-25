import csv

from datetime import datetime

from consts import *

"""
Income Manager Module - manages and handles all income actions
"""


class OutcomeManager:
    def __init__(self):
        self.header = {'id_column': 'id', 'date_column': 'date', 'outcome_column': 'outcome amount',
                       'method_column': 'method', 'description_column': 'description'}
        self.outcome_file = OUTCOME_FILE
        self.current_id = 0

        try:
            with open(self.income_file, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.header.keys())  # Write the header if the file is newly created
                print(f"Created new file: {self.outcome_file}")
        except Exception:
            print(f"Could not open outcome file")

