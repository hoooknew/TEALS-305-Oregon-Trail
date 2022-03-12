import datetime # https://docs.python.org/3/library/datetime.html#date-objects
import random # https://docs.python.org/3/library/random.html

##########  DATE STUFF  ##########

START_DATE = datetime.date(2022, 3, 1)
END_DATE = datetime.date(2022, 12, 31)

def days_between(start_date : datetime.date, end_date: datetime.date):
    return (end_date - start_date).days

def get_current_date():
    return START_DATE + datetime.timedelta(days=days_from_start)

def get_current_date_str():
    curr_date = get_current_date()
    return curr_date.strftime("%m/%d")

def get_current_day_of_month():
    return get_current_date().day

##########  TEXT STYLING  ##########

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

    # add between 30 and 60 miles
    miles_this_trip = (30 + random.randrange(0, 31))
    miles_traveled = miles_traveled + miles_this_trip
    
    days_this_trip = take_time(3, 7)

    print ("You traveled " + str(miles_this_trip) + " miles over " + str(days_this_trip) +" days.")

def hunt():
    global lbs_of_food

    lbs_of_food = lbs_of_food + 100
    days_this_hunt = take_time(2, 5)

    print ("You hunted 100 pounds of food over " + str(days_this_hunt) +" days.")

def rest():
    global player_health

    days_this_rest = take_time(2, 5)

    if player_health == 5:        
        print("Your health stayed at " + bold(str(player_health)) + " health while resting for " + bold(str(days_this_rest)) + " days.")
    else:
        player_health = player_health + 1        
        print("Your health increased by one to " + bold(str(player_health)) + " health while resting for " + bold(str(days_this_rest)) + " days.")

def take_time(min_days : int, max_days: int):
    global days_from_start
    global lbs_of_food
    global player_health

    starting_day_of_month = get_current_day_of_month()

    days_passed = (min_days + random.randrange(0, (max_days - min_days) + 1))
    days_from_start = days_from_start + days_passed

    if 15 > starting_day_of_month and 15 <= starting_day_of_month + days_passed:
        player_health = player_health - 1
        print(red("Your health decreased by 1"))

    if 30 > starting_day_of_month and 30 <= starting_day_of_month + days_passed:
        player_health = player_health - 1
        print(red("Your health decreased by 1"))

    food_eaten = days_passed * 5
    lbs_of_food = lbs_of_food - food_eaten
    print ("You ate "+str(food_eaten)+" pounds of food over " + str(days_passed) +" days.")
    if lbs_of_food < 100:
        print (red("You have " + str(lbs_of_food) + " pounds of food left."))
    else:
        print ("You have " + str(lbs_of_food) + " pounds of food left.")

    return days_passed

def take_action(action):
    if action == "travel":
        travel()
    elif action == "hunt":
        hunt()
    elif action == "rest":
        rest()
    elif action == "status":
        print ("You have traveled " + bold(str(miles_traveled)) + " miles for " + bold(str(days_from_start)) + " days.")
        print ("You have " + bold(str(lbs_of_food)) + " pounds of food left.")
        print ("You have " + bold(str(player_health)) + " health left.")
        print ("It is " + bold(get_current_date_str()) + ".")
    elif action == "quit":
        print ("quitter!")
        quit()
    else:
        print('You can type "travel", "hunt", "rest", "status", "help", or "quit".')

##########  MAIN FUNCTION  ##########

player_name = input("What is the player's name? ")

days_total = days_between(START_DATE, END_DATE)
days_from_start = 0

miles_total = 2000
miles_traveled = 0

lbs_of_food = 500

player_health = 5

while (
        (miles_total > miles_traveled) and 
        (days_total > days_from_start) and
        lbs_of_food >= 0 and
        player_health > 0
    ):
    action = input(bold("\n" + player_name + ", what would you like to do? "))
    take_action(action)

if (miles_total < miles_traveled):
    print(bold(green("You made it on " + get_current_date_str() + "!")))
elif(days_total < days_from_start):
    print(bold(red("You didn't make it by 12/31 and froze to death in the cold winter...")))
elif(player_health <= 0):
    print(bold(red("You died from overexertion...")))
elif(lbs_of_food < 0):
    print(bold(red("You starved...")))
