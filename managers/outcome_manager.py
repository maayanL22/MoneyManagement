import csv

from datetime import datetime

from managers.consts import *

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
            with open(self.outcome_file, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.header.keys())  # Write the header if the file is newly created
                print(f"Created new file: {self.outcome_file}")
        except Exception:
            print(f"Could not open outcome file")

    def write_outcome(self, outcome: int, date: datetime, description: str):
        with open(self.outcome_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.current_id, date, outcome, description])

    def sum_income_of_month(self, month: int):
        total = 0
        outcome_column_name = self.header['outcome_column']
        date_column_name = self.header['date_column']
        with open(self.outcome_file, newline='', encoding='utf-8') as outcome_file:
            # Use DictReader to access columns by name (string)
            reader = csv.DictReader(outcome_file)
            if outcome_column_name not in reader.fieldnames:
                print(f"Error: Column '{outcome_column_name}' not found.")
                return None

            for row in reader:
                try:
                    if row[date_column_name].month == month:
                        # Convert the value to a float (or int if you only have integers) and add to the total
                        value = row[outcome_column_name].replace(',', '')  # Handle potential thousand separators
                        total += float(value)
                except ValueError:
                    # Handle cases where a value might be missing or non-numeric (e.g., 'N/A', empty string)
                    print(f"Warning: Skipping non-numeric value in row: {row[outcome_column_name]}")
                    continue
        return total

