from datetime import datetime

def get_days_from_today(date):
    try:
        data = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - data
        return delta.days
    except ValueError:
        print("Введіть дату у форматі 'YYYY-MM-DD'")

print(get_days_from_today('2021-05-05'))