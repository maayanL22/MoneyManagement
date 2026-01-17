import csv

from consts import *

"""
Income Manager Module - manages and handles all income actions
"""
class IncomeManager():
    def __init__(self):
        header = ['date', 'amount', 'description']

        try:
            with open(INCOME_FILE, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)  # Write the header if the file is newly created
                print(f"Created new file: {INCOME_FILE}")
