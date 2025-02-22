"""
Hacking The Fender
The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret 
passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access 
to The Fender‘s systems, you must update his "passwords.csv" file to scramble the secret data. The last thing you 
need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very 
conveniently halted by The Fender if they viewed Slash Null as a threat.

Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest 
for justice. Work with CSV files and other text files in this exploration of the strength of Python file 
programming.

If you get stuck during this project, check out the project walkthrough video which can be found in the help menu.
"""

# Reading In The Passwords

# First import the CSV module, since we’ll be needing it to parse the data.
import csv

# We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users.
compromised_users = []

# We need to create a list of users whose passwords have been compromised, create a new list and save it to 
# the variable compromised_users.
password_path = 'python_3_basics/hacking_the_fender/passwords.csv'

# Next we’ll need you to open up the file itself. Store it in a file object called password_file.
with open(password_path) as password_file:

    # Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
    password_csv = csv.DictReader(password_file)
    
    # Now we’ll want to iterate through each of the lines in the CSV. Create a for loop and save each row of the CSV into the 
    # temporary variable password_row.
    for password_row in password_csv:
        # We want to add each username to the list of compromised_users. Use the list’s .append() method to add the username to 
        # compromised_users instead of printing them.
        compromised_users.append(password_row['Username'])

print(compromised_users)

# Inside the new context-managed block opened by the with statement start a new for loop. Iterate over each of your compromised_users.
compromised_users_path = 'python_3_basics/hacking_the_fender/compromised_users.txt'

# Write the username of each compromised_user in compromised_users to compromised_user_file.
with open(compromised_users_path, 'w') as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)