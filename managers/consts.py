from enum import Enum

# File paths
INCOME_FILE = "./db/income.csv"
OUTCOME_FILE = "./db/outcome.csv"


# Enums
class PaymentMethod(Enum):
    CREDIT_CARD = 0
    CASH = 1
    BIT = 2

