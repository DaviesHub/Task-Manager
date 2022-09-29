#=====IMPORT RELEVANT LIBRARIES===========
from datetime import date

#====LOGIN SECTION====

# The usernames and passwords in the file are separated by a comma, so to validate usernames, commas are removed
# The usernames and passwords are then stored in a dictionary
users_dic = {} 
fhand = open("user.txt", "r")
users = fhand.read()
users = users.split()
fhand.close() 
for i in range(0, len(users), 2):
    users[i] = users[i].lower()
    users_dic[users[i].replace(",", "")] = users[i+1]

# Prompt user input
while True:
    user_name = input("Enter username: ").lower()
    password = input("Enter password: ")
    if user_name in users_dic.keys() and password == users_dic[user_name]:
        print("\nLogin Successful!")
        break
    else:
        print("\nUsername or password don't match. Please enter a valid username and password") # As security feature, they must not know which one (username or password) is wrong
        
#====INSIDE APP (after login)====

while True:
    menu = input('''\nSelect one of the following Options below:
# r - Registering a user
# a - Adding a task
# va - View all tasks
# vm - view my task
# e - Exit
# : ''').lower()

    if menu == 'r':
        # Code to register new users
        while True:
            new_username = input("Enter new username: ").lower()
            if new_username in users_dic.keys():
                print("Username already exists...")
            else:
                break

        while True:
            new_password = input("Enter password: ")
            new_password2 = input("Confirm password: ")
            if new_password != new_password2:
                print("Incorrect password.")
            else:
                break
        
        fhand = open("user.txt", "a")
        fhand.write(new_username + ", " + new_password + "\n")
        fhand.close()   
                
    elif menu == 'a':
        # Code to add tasks
        recepient = input("Enter the username of the person to whom the task is assigned: ").lower()
        task_title = input("Enter the title of the task: ")
        task = input("Enter a brief description of the task below, do not punctuate with commas:\n")
        due_date = input("Enter the task due date in the format DD MMM YYYY (e.g. 12 Mar 2020): ")
        completion = "No" # Capitalize first letter

        today = date.today()
        today = today.strftime("%d %b %Y") # Formats date to specified format

        fhand = open("tasks.txt", "a")
        fhand.write(recepient + ", " + task_title + ", " + task + ", " + today + ", " + due_date + ", " + completion + "\n")
        fhand.close()

    elif menu == 'va':
        # Code to read tasks from task file
        with open("tasks.txt", "r") as f:
            for line in f:
                line = line.split(", ")
                print("Task:\t\t" + line[1] + "\nAssigned to:\t" + line[0] + "\nDate assigned:\t" + line[3] +\
                "\nDue date:\t" + line[4] + "\nTask complete:\t" + line[5] + "Task description: " + line[2] + "\n")

    elif menu == 'vm':
        # Code to read tasks assigned to the user who is logged in
        with open("tasks.txt", "r") as f:
            for line in f:
                line = line.split(", ")
                if line[0].lower() == user_name:
                    print("Task:\t\t" + line[1] + "\nAssigned to:\t" + line[0] + "\nDate assigned:\t" + line[3] +\
                    "\nDue date:\t" + line[4] + "\nTask complete:\t" + line[5] + "Task description: " + line[2] + "\n")

    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again")