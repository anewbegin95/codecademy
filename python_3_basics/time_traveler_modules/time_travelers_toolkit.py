# At the beginning of your script, import the necessary modules. 
# This includes importing the datetime module with an alias of dt, Decimal from the decimal module, and the randint and choice functions from 
# the random module. Also, import the custom_module.py you created earlier, making sure it is in the same directory as time_travelers_toolkit.py.

import datetime as dt
from random import randint, choice
from decimal import Decimal
from custom_module import generate_time_travel_message

# Use the datetime module to retrieve the current date and time. You’ll need to obtain both the date and the exact time at the moment the script is run.
current_date = dt.datetime.now()

# Once you’ve retrieved the current date and time, print them out to the console in a clear and readable format. This will give you a reference point for when the time travel message is generated.
print(current_date)

# To calculate the cost of time travel, use the decimal module, which provides a way to perform precise financial calculations. 
# First, create a base cost as a Decimal object. Then, determine a cost multiplier based on the difference between the current year and the 
# target year. Combine these values to calculate the final cost.
def time_travel_cost(target_year):
    base_cost = Decimal("4.99")
    current_year = current_date.year
    total_cost = Decimal(abs(current_year - target_year)) * base_cost
    return total_cost

# Use the randint() function to generate a random year within a specified range. This random year will be the target year for the time travel.
target_year = randint(1, 2024)

# Create a list of possible destinations for the time travel. Then, use the choice() function to randomly select one destination from the list.
destinations = ["Ur", "Babylon", "Xi'an", "Tenochtitlan", "Atlantis", "Memphis", "Troy", "Pompeii", "El Dorado", "Camelot", "The Somme", "Hiroshima", "Woodstock"]
chosen_destination = choice(destinations)

# After generating a random year, selecting a destination, and calculating the cost, use these values as arguments for the generate_time_travel_message() 
# function you imported from custom_module.py earlier. Print the generated message to describe the user’s time travel experience, and congratulations on a
#  project completed!
cost = time_travel_cost(target_year)

my_trip = generate_time_travel_message(target_year, chosen_destination, cost)
print(my_trip)