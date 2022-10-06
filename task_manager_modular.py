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
    # For login, the new username is compared to keys in the username dictionary
    # If there is a match, the password must correspond to the corresponding value of the key 
    user_name = input("Enter username: ").lower()
    password = input("Enter password: ")
    if user_name in users_dic.keys() and password == users_dic[user_name]:
        print("\nLogin Successful!")
        break
    else:
        print("\nUsername or password don't match. Please enter a valid username and password") # As security feature, they must not know which one (username or password) is wrong

# Define functions for each feature

def reg_user():
    """This function creates a new user and adds it to the registry (user.txt)"""
        # The new username is checked for singularity. If passed, the new username and password is written to the user file
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


def add_task():
    """This function adds new tasks to tasks file"""

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


def view_all():
    """This function reads tasks from the task file and displays it in a user-friendly format"""
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.split(", ")
            print("Task:\t\t" + line[1] + "\nAssigned to:\t" + line[0] + "\nDate assigned:\t" + line[3] +\
            "\nDue date:\t" + line[4] + "\nTask complete:\t" + line[5] + "Task description: " + line[2] + "\n")


def view_mine():
    """Function to read tasks assigned to the user who is logged in"""
    # The task's line is splitted into list. The first item (username) is compared to current username and the users tasks displayed
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.split(", ")
            if line[0].lower() == user_name:
                print("Task:\t\t" + line[1] + "\nAssigned to:\t" + line[0] + "\nDate assigned:\t" + line[3] +\
                "\nDue date:\t" + line[4] + "\nTask complete:\t" + line[5] + "Task description: " + line[2] + "\n")


def display_stats():
    """Function to count and display the number of users and tasks on the app"""

    # Code to count and display the total number of users to admin
    with open("user.txt", "r") as f:
        count_users = 0
        for line in f:
            count_users += 1
        print(f"\nThe total number of users is {count_users}")
        
    # Code to count and display the number of assigned tasks to admin
    with open("tasks.txt", "r") as f:
        count_task = 0
        for line in f:
            count_task += 1
        print(f"The total number of tasks is {count_task}")


#====INSIDE APP (after login)====

while True:
    # Code to ensure that only admin can register new users and view stats
    # The additional features are only made available if the current user is admin
    if user_name == "admin":
        menu = input('''\nSelect one of the following Options below:
    # r - Registering a user
    # a - Adding a task
    # va - View all tasks
    # vm - view my task
    # ds - display statistics
    # e - Exit
    # : ''').lower()
    else:
        menu = input('''\nSelect one of the following Options below:
    # a - Adding a task
    # va - View all tasks
    # vm - view my task
    # e - Exit
    # : ''').lower()

    if menu == "r" and user_name == "admin":
        reg_user()   
                
    elif menu == "a":
        add_task()
        
    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "ds" and user_name == "admin":
        display_stats()

    elif menu == "e":
        print('\nGoodbye!!!')
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again")

