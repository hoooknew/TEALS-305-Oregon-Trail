import random # https://docs.python.org/3/library/random.html
import time

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

RIVER_CROSSING = 'river crossing'
DYSENTERY = 'dysentery'
RICK_ROLL = 'rick roll'

# starts 3/1 and ends 12/31
def make_stuff_happens_calendar():
    stuff_calendar = []
    for m in range(3, len(DAYS_IN_EACH_MONTH)):
        day_for_stuff = random.randrange(1, DAYS_IN_EACH_MONTH[m] + 1)
        for d in range(1, DAYS_IN_EACH_MONTH[m] + 1):
            if d == day_for_stuff:                
                stuff_calendar.append(random.choice([RIVER_CROSSING, DYSENTERY, RICK_ROLL]))
            else:
                stuff_calendar.append(None)
    return stuff_calendar

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

def blue(text):
    return '\N{ESC}[34m' + text + '\N{ESC}[0m'

def yellow(text):
    return '\N{ESC}[33m' + text + '\N{ESC}[0m'

##########  ACTIONS  ##########

def travel():
    global miles_traveled     

    if (
        month_cal[days_from_start] >= 11 and 
        miles_traveled >= 1500 and 
        random.randrange(1, 11) <= 2
    ):
        print(blue("You got caught in a blizzard in the Sierra Nevadas... 🥶 The distance you traveled is halfed."))
        # add between 15 and 30 miles
        miles_this_trip = random.randrange(15, 31)
        miles_traveled = miles_traveled + miles_this_trip
    else:
        # add between 30 and 60 miles
        miles_this_trip = random.randrange(30, 61)
        miles_traveled = miles_traveled + miles_this_trip
    
    print ("You traveled " + bold(str(miles_this_trip)) + " miles over " + bold(str(days_this_trip)) +" days.")

    days_this_trip = take_time(3, 7)
    eat_food(days_this_trip, 5)    

def hunt():
    global lbs_of_food

    lbs_of_food = lbs_of_food + 100

    days_this_hunt = take_time(2, 5)
    eat_food(days_this_hunt, 6)

    print ("You hunted 100 pounds of food over " + str(days_this_hunt) +" days.")

def rest():
    global player_health

    days_this_rest = take_time(2, 5)
    eat_food(days_this_rest, 3)

    if player_health == 5:        
        print("Your health stayed at " + bold(str(player_health)) + " health while resting for " + bold(str(days_this_rest)) + " days.")
    else:
        player_health = player_health + 1        
        print("Your health increased by one to " + bold(str(player_health)) + " health while resting for " + bold(str(days_this_rest)) + " days.")

def cross_river():
    days_to_cross = random.randrange(1, 10 + 1)
    print(yellow("You found a river! 😃 You now have to ford it. 😑 It will take " + bold(str(days_to_cross)) + yellow(" days to cross... 😭")))
    return days_to_cross

def literal_stuff_happening():
    global player_health

    days_to_heal = random.randrange(1, 10 + 1)
    print(yellow("You got dysentery! 💩🥳 It will take " + bold(str(days_to_heal)) + yellow(" days to heal... 😭")))
    player_health = player_health - 1
    print(red("Your health decreased by 1 because of the dysentery."))

    return days_to_heal

def rick_rolling():
    global player_health
    important_text = '''We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it

And if you ask me how I'm feeling
Don't tell me you're too blind to see

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

(Ooh, give you up)
(Ooh, give you up)
Never gonna give, never gonna give
(Give you up)
Never gonna give, never gonna give
(Give you up)

We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you'''.splitlines()

    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀''')
    print()
    print(bold("You've encountered a traveling minstrel! What great luck! 🍀"))    
    time.sleep(3)    
    print()
    for line in important_text:
        if line != '':
            print('🎶 ' + line + ' 🎶')
        else:
            print()
        time.sleep(.75)
    print()

    print(bold("WOW! Wasn't that refreshing! Your health is fully restored to " + blue("5") + bold(". 😎")))
    player_health = 5

    return 0

def stuff_happens(stuff_happening):
    if stuff_happening == RIVER_CROSSING:
        return cross_river()
    elif stuff_happening == DYSENTERY:
        return literal_stuff_happening()
    elif stuff_happening == RICK_ROLL:
        return rick_rolling()
    else:
        return 0

def take_time(min_days : int, max_days: int):
    global days_from_start
    global lbs_of_food
    global player_health
    
    days_passed =0
    days_to_pass = random.randrange(min_days, max_days + 1)
    while days_passed < days_to_pass:
        days_from_start = days_from_start + 1
        days_passed = days_passed + 1
        
        if day_cal[days_from_start] == 15 or day_cal[days_from_start] == 30:
            player_health = player_health - 1
            print(red("Your health decreased by 1 because of exertion. 😱"))            
        
        if stuff_cal[days_from_start] is not None:
            days_to_pass = days_to_pass + stuff_happens(stuff_cal[days_from_start])

    return days_passed

def eat_food(days_passed, food_per_day):
    global lbs_of_food
    if lbs_of_food > 0:
        food_eaten = days_passed * 5
        lbs_of_food = lbs_of_food - food_eaten
        print ("You ate "+str(food_eaten)+" pounds of food over " + str(days_passed) +" days.")
        if lbs_of_food < 100:
            print (red("You have " + str(lbs_of_food) + " pounds of food left."))
        else:
            print ("You have " + str(lbs_of_food) + " pounds of food left.")

    if lbs_of_food < 0:
        player_health = player_health - 1
        print(red("You're starving and your health decreased by 1"))

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

month_cal = make_month_calendar()
day_cal = make_day_calendar()
stuff_cal = make_stuff_happens_calendar()

days_total = len(day_cal) - 1
days_from_start = 0

miles_total = 2000
miles_traveled = 0

lbs_of_food = 500

player_health = 5


while (
        (miles_total > miles_traveled) and 
        (days_total > days_from_start) and        
        player_health > 0
    ):
    action = input(bold("\n" + player_name + ", what would you like to do? "))
    take_action(action)

if (miles_total < miles_traveled):
    print(bold(green("You made it on " + get_current_date_str() + "!")))
elif(days_total < days_from_start):
    print(bold(red("You didn't make it by 12/31 and froze to death in the cold winter...")))
elif(player_health <= 0):
    print(bold(red("You died... 💀")))