##########  DATE STUFF  ##########

# the first item is set to None intentionally so the array index will be the month number.
DAYS_IN_EACH_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# starts 3/1 and ends 12/31
def make_month_calendar(): 
    month_calendar = []
    for m in range(3, len(DAYS_IN_EACH_MONTH)):
        for d in range(1, DAYS_IN_EACH_MONTH[m] + 1):
            month_calendar.append(m)
    return month_calendar

# starts 3/1 and ends 12/31
def make_day_calendar():
    day_calendar = []
    for m in range(3, len(DAYS_IN_EACH_MONTH)):
        for d in range(1, DAYS_IN_EACH_MONTH[m] + 1):
            day_calendar.append(d)
    return day_calendar

def get_current_date_str():    
    return str(month_cal[days_from_start]) + "/" + str(day_cal[days_from_start])

##########  TEXT STYLING  ##########

def bold(text):
    return '\N{ESC}[1m' + text + '\N{ESC}[0m'

def green(text):
    return '\N{ESC}[32m' + text + '\N{ESC}[0m'

def red(text):
    return '\N{ESC}[31m' + text + '\N{ESC}[0m'

def yellow(text):
    return '\N{ESC}[33m' + text + '\N{ESC}[0m'

##########  MAIN FUNCTION  ##########

month_cal = make_month_calendar()
day_cal = make_day_calendar()

days_total = len(day_cal) - 1
days_from_start = 0