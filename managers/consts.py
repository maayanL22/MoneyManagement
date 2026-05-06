from enum import Enum

# File paths
INCOME_FILE_PATH = "./db/income.csv"
OUTCOME_FILE_PATH = "./db/outcome.csv"
MAIN_FILE_PATH = "./db/main.csv"

# Enums
class PaymentMethod(Enum):
    CREDIT_CARD = 0
    CASH = 1
    BIT = 2

