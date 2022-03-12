This is a solution for the [TEALS 3.05 lab](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/units/3_unit/05_lesson/project.md.html).

I have also broken down the original task into smaller milestones to help the students focus their efforts on smaller goals.

# Project 3: Oregon Trail

Using variables, functions, and conditionals in Python, students will create an Oregon Trail game.

## Overview
We will be recreating Oregon Trail! The goal is to travel from Independence, Missouri to Oregon City, Oregon (2000 miles) by Dec 31st. However, the trail is arduous. Each day costs you food. You can hunt and rest, but you have to get there before winter!

## Details
  
### Phases

#### Traveling, Status, and Help
- Ask for the player's name
- Player starts in Independence, Missouri on 03/01 with 2,000 miles to go.
- Each turn, the player is asked what action they choose, where the player can type in the following: **travel**, **status**, **help**, **quit**
- travel: moves you randomly between 30-60 miles and takes 3-7 days (random).
- status: lists **distance traveled**, and **day**.
- help: lists all the commands.
- quit: will end the game.
- The player must get to Oregon by 12/31. Let the player know if they have won or lost.

#### Eating and Hunting
- Player has 500lbs of food.
- The player eats 5lbs of food a day.
- Each turn, the player is asked what action they choose, where the player can type in the following: "travel", and **"hunt"**
- hunt: adds 100lbs of food and takes 2-5 days (random).
- If the player runs out of food, they die.
- status: lists **food**, distance traveled, and day.
- help: lists **hunt**.

#### Resting
- The Player has 5 health.
- The player's health will decrease twice each month.
- status: lists food, **health**, distance traveled, and day.
- rest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
- help: lists **rest**.

### Implementation details
- Create functions for all options a player can take
- Use global variables to keep track of player health, food pounds, miles to go, current day, current month
- Create a function add_day which updates the day
- Use a list to keep track of which months have 31 days and use this in the add_day function (i.e.: - MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]) **OR** use the date functions provided in the starter code.
- Create a select_action function that uses a while loop to call the add_day function
- Game ends if days run out, health runs out, the player reaches Oregon, or the player quits.

## Bonus
1. Make the rate of food consumption be a function of activity. If a player hunts for a turn they take up more food, but if they rest they take up less food.
2. Create a random event that occurs randomly once a month, like a river crossing or a dysentery, that will take up a range of 1-10 food, 1-10 days and 0-1 health.
3. Create a range of miles corresponding to high altitudes in the Rocky Mountains, where there is an increased chance of slow travel due to snow after November 1st.