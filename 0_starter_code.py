import datetime # https://docs.python.org/3/library/datetime.html#date-objects
import random # https://docs.python.org/3/library/random.html

START_DATE = datetime.date(2022, 3, 1)
END_DATE = datetime.date(2022, 12, 31)

def days_between(start_date : datetime.date, end_date: datetime.date):
    return (end_date - start_date).days

def get_current_date():
    return START_DATE + datetime.timedelta(days=days_passed)

def get_current_date_str():
    curr_date = get_current_date()
    return curr_date.strftime("%m/%d")


days_total = days_between(START_DATE, END_DATE)
days_passed = 0