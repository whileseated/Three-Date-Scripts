import sys
from datetime import datetime

def calculate_days_from_date(date_str):
    try:
        given_date = datetime.strptime(date_str, "%Y%m%d")
        current_date = datetime.now()
        difference = current_date - given_date
        return difference.days
    except ValueError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 date_calculator.py YYYYMMDD")
    else:
        date_str = sys.argv[1]
        result = calculate_days_from_date(date_str)
        print(f"Days from {date_str}: {result}")

