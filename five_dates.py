from datetime import datetime, timedelta

def date_days_ago(days):
    past_date = datetime.today() - timedelta(days=days)
    return past_date.strftime('%Y%m%d')

intervals = [500, 1000, 5000, 10000, 20000]

for interval in intervals:
    result = date_days_ago(interval)
    print(f"{result} - {interval}")

