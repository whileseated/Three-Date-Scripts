import sys
from datetime import datetime, timedelta

def date_days_ago(days):
    past_date = datetime.today() - timedelta(days=days)
    return past_date.strftime('%Y%m%d')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 date-script.py <days>")
    else:
        try:
            days_ago = int(sys.argv[1])
            result = date_days_ago(abs(days_ago))
            print(result)
        except ValueError:
            print("Please enter a valid number of days.")
