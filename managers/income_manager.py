import csv

from datetime import datetime

from managers.consts import *

"""
Income Manager Module - manages and handles all income actions
"""


class IncomeManager:
    def __init__(self):
        self.header = {'id_column': 'id', 'date_column' :'date', 'income_column': 'income amount',
                  'description_column' : 'description'}
        self.income_file = INCOME_FILE
        self.current_id = 0

        try:
            with open(self.income_file, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.header.keys())  # Write the header if the file is newly created
                print(f"Created new file: {self.income_file}")
        except Exception:
            print(f"Could not open income file")

    def write_income(self, income: int, date: datetime, description: str):
        with open(self.income_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.current_id, date, income, description])

    def sum_income_of_month(self, month: int):
        total = 0
        income_column_name = self.header['income_column']
        date_column_name = self.header['date_column']
        with open(self.income_file, newline='', encoding='utf-8') as income_file:
            # Use DictReader to access columns by name (string)
            reader = csv.DictReader(income_file)
            if income_column_name not in reader.fieldnames:
                print(f"Error: Column '{income_column_name}' not found.")
                return None

            for row in reader:
                try:
                    if row[date_column_name].month == month:
                        # Convert the value to a float (or int if you only have integers) and add to the total
                        value = row[income_column_name].replace(',', '')  # Handle potential thousand separators
                        total += float(value)
                except ValueError:
                    # Handle cases where a value might be missing or non-numeric (e.g., 'N/A', empty string)
                    print(f"Warning: Skipping non-numeric value in row: {row[income_column_name]}")
                    continue
        return total
