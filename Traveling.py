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

def travel():
    global miles_traveled 
    global days_passed

    # add between 30 and 60 miles
    miles_this_trip = (30 + random.randrange(0, 31))
    miles_traveled = miles_traveled + miles_this_trip
    # add between 3 and 7 days
    days_this_trip = (3 + random.randrange(0, 5))
    days_passed = days_passed + days_this_trip

    print ("You traveled " + str(miles_this_trip) + " over " + str(days_this_trip) +" days.")

def take_action(action):
    if action == "travel":
        travel()
    elif action == "status":
        print ("You have traveled " + str(miles_traveled) + "miles for " + str(days_passed) + " days.")
        print ("It is " + get_current_date_str() + ".")    
    elif action == "quit":
        print ("quitter!")
        quit()
    else:
        print('You can type "travel", "status", "help", or "quit".')


player_name = input("What is the player's name? ")

days_total = days_between(START_DATE, END_DATE)
days_passed = 0

miles_total = 2000
miles_traveled = 0

while (
        (miles_total > miles_traveled) and 
        (days_total > days_passed)
    ):
    action = input(player_name + ", what would you like to do? ")
    take_action(action)

if (miles_total < miles_traveled):
    print("You made it on " + get_current_date_str() + "!")
elif(days_total < days_passed):
    print("You didn't make it by 12/31 and froze to death in the cold winter")
