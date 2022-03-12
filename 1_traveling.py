import random # https://docs.python.org/3/library/random.html

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

# https://chrisyeh96.github.io/2020/03/28/terminal-colors.html

def bold(text):
    return '\N{ESC}[1m' + text + '\N{ESC}[0m'

def green(text):
    return '\N{ESC}[32m' + text + '\N{ESC}[0m'

def red(text):
    return '\N{ESC}[31m' + text + '\N{ESC}[0m'

def yellow(text):
    return '\N{ESC}[33m' + text + '\N{ESC}[0m'

##########  ACTIONS  ##########

def travel():
    global miles_traveled 
    global days_from_start

    # add between 30 and 60 miles
    miles_this_trip = random.randrange(30, 61)
    miles_traveled = miles_traveled + miles_this_trip
    # add between 3 and 7 days
    days_passed = random.randrange(3, 8)
    days_from_start = days_from_start + days_passed

    print ("You traveled " + str(miles_this_trip) + " miles over " + str(days_passed) +" days.")

def take_action(action):
    if action == "travel":
        travel()
    elif action == "status":
        print ("You have traveled " + str(miles_traveled) + " miles for " + str(days_from_start) + " days.")
        print ("It is " + get_current_date_str() + ".")    
    elif action == "quit":
        print ("quitter!")
        quit()
    else:
        print('You can type "travel", "status", "help", or "quit".')

##########  MAIN FUNCTION  ##########

player_name = input("What is the player's name? ")

month_cal = make_month_calendar()
day_cal = make_day_calendar()

days_total = len(day_cal) - 1
days_from_start = 0

miles_total = 2000
miles_traveled = 0

while (
        (miles_total > miles_traveled) and 
        (days_total > days_from_start)
    ):
    action = input(player_name + ", what would you like to do? ")
    take_action(action)

if (miles_total < miles_traveled):
    print(bold(green("You made it on " + get_current_date_str() + "!")))
elif(days_total < days_from_start):
    print(bold(red("You didn't make it by 12/31 and froze to death in the cold winter...")))
