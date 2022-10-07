#=====IMPORT RELEVANT LIBRARIES===========
from datetime import date

#====LOGIN SECTION====

# The usernames and passwords in the file are separated by a comma, so to validate usernames, commas are removed
# The usernames and passwords are then stored in a dictionary
users_dic = {}
tasks = [] # Empty list to store all tasks 
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
    task_num = 0
    task_dic = {} # Dictionary to store each part of an individual task

    recepient = input("Enter the username of the person to whom the task is assigned: ").lower()
    task_title = input("Enter the title of the task: ")
    task = input("Enter a brief description of the task below, do not punctuate with commas:\n")
    due_date = input("Enter the task due date in the format DD MMM YYYY (e.g. 12 Mar 2020): ")
    completion = "No" # Capitalize first letter

    today = date.today()
    today = today.strftime("%d %b %Y") # Formats date to specified format

    task_dic["recepient"] = recepient
    task_dic["title"] = task_title
    task_dic["descr"] = task
    task_dic["d_date"] = due_date
    task_dic["completion"] = completion
    task_dic["a_date"] = today

    fhand = open("tasks.txt", "a")
    for line in fhand:
        task_num += 1
    task_dic["task_id"] = task_num
    tasks.append(task_dic) # Append each task dictionary in the list of tasks

    fhand.write(task_num + ": " + recepient + ", " + task_title + ", " + task + ", " + today + ", " + due_date + ", " + completion + "\n")
    fhand.close()


def view_all():
    """This function reads tasks from the task file and displays it in a user-friendly format"""
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.split(", ")
            print("Task:" + line[0] + "\t\t" + line[2] + "\nAssigned to:\t" + line[1] + "\nDate assigned:\t" + line[4] +\
            "\nDue date:\t" + line[5] + "\nTask complete:\t" + line[6] + "Task description: " + line[3] + "\n")


def view_mine():
    """Function to read tasks assigned to the user who is logged in"""
    # The task's line is splitted into list. The first item (username) is compared to current username and the users tasks displayed
    task_map = {} # Dictionary to hold tasks assigned to the user and a task number
    task_list = [] # Empty list to store user's tasks'

    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.split(", ")
            if line[1].lower() == user_name:
                task_message = "Task:" + line[0] + "\t\t" + line[2] + "\nAssigned to:\t" + line[1] + "\nDate assigned:\t" + line[4] +\
                "\nDue date:\t" + line[5] + "\nTask complete:\t" + line[6] + "Task description: " + line[3] + "\n"
                
                print(task_message)


    # Code to allow a user select a specific task or return to the main menu
    while True:
        task_num = input("\nEnter the number of a task to view the task, or enter -1 to return to the main menu:\n")
        if task_num in task_map.keys():
            message = f"Task{task_num}: {task_map[task_num]}"
            print("You have selected the following task:\n", message)


            break
        elif task_num == "-1":
            pass # Code to return to main menu
        else:
            print("Invalid option")


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

