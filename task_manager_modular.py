#=====IMPORT RELEVANT LIBRARIES===========
from datetime import date
from datetime import datetime

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

# When program is run, all tasks in the tasks file are stored in a list
task_count = 0
fhand = open("tasks.txt", "r")
for line in fhand:
    task_dic = {}
    if len(line) > 1:
        task_count += 1

    line = line.split(", ")
    task_dic["task_id"] = task_count
    task_dic["recepient"] = line[0]
    task_dic["title"] = line[1]
    task_dic["descr"] = line[2]
    task_dic["d_date"] = line[4]
    task_dic["completion"] = "No"
    task_dic["a_date"] = line[3]

    tasks.append(task_dic)
fhand.close()

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

    # Store new user in users dictionary
    users_dic[new_username] = new_password2


def add_task():
    """This function adds new tasks to tasks file"""

    task_num = 1

    recepient = input("Enter the username of the person to whom the task is assigned: ").lower()
    task_title = input("Enter the title of the task: ")
    task = input("Enter a brief description of the task below, do not punctuate with commas:\n")
    due_date = input("Enter the task due date in the format DD MMM YYYY (e.g. 12 Mar 2020): ").title()
    completion = "No" # Capitalize first letter

    today = date.today()
    today = today.strftime("%d %b %Y") # Formats date to specified format

    task_dic["recepient"] = recepient
    task_dic["title"] = task_title
    task_dic["descr"] = task
    task_dic["d_date"] = due_date
    task_dic["completion"] = completion
    task_dic["a_date"] = today

    fhand = open("tasks.txt", "r+")
    for line in fhand:
        if len(line) > 1:
            task_num += 1
    task_dic["task_id"] = task_num
    tasks.append(task_dic) # Append each task dictionary in the list of tasks

    fhand.write(recepient + ", " + task_title + ", " + task + ", " + today + ", " + due_date + ", " + completion + "\n")
    fhand.close()


def view_all():
    """This function reads tasks from the task file and displays it in a user-friendly format"""
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.split(", ")
            print("Task:" + "\t\t" + line[1] + "\nAssigned to:\t" + line[0] + "\nDate assigned:\t" + line[3] +\
            "\nDue date:\t" + line[4] + "\nTask complete:\t" + line[5] + "Task description: " + line[2] + "\n")


def view_mine():
    """Function to read tasks assigned to the user who is logged in"""
    # The task's line is splitted into list. The first item (username) is compared to current username and the users tasks displayed
    task_id = 0

    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.split(", ")
            if line[1].lower() == user_name:
                task_message = "Task:" + line[0] + "\t\t" + line[2] + "\nAssigned to:\t" + line[1] + "\nDate assigned:\t" + line[4] +\
                "\nDue date:\t" + line[5] + "\nTask complete:\t" + line[6] + "Task description: " + line[3] + "\n"
                
                print(task_message)

    # Code to allow a user select a specific task or return to the main menu
    while True:
        task_id = input("\nEnter the number of a task to view the task, or enter -1 to return to the main menu:\n")
        
        for i in range(len(tasks)):
            if task_id == str(tasks[i]["task_id"]) and user_name == tasks[i]["recepient"]:
                message = "Task:" + tasks[i]["task_id"] + "\t\t" + tasks[i]["title"] + "\nAssigned to:\t" + tasks[i]["recepient"] + "\nDate assigned:\t" + tasks[i]["a_date"] +\
                "\nDue date:\t" + tasks[i]["d_date"] + "\nTask complete:\t" + tasks[i]["completion"] + "Task description: " + tasks[i]["descr"] + "\n"
                print("You have selected the following task:\n", message)
                edit_task()
                break

            elif task_id == "-1": # Code to return to main menu
                break

            else:
                print("Invalid option")



def edit_task():
    """Function to allow a user edit a task"""

    while True:
        action = input('''\nSelect one of the options below:
        # m - Mark a task as complete
        # e - edit a task
        # : ''').lower()

        if action == "m":
            if tasks[i]["completion"].lower() != "yes":
                tasks[i]["completion"] = "Yes"
                print("Successful! Task is complete.")
            else:
                print("The task is already complete.")

        elif action == "e":
            if tasks[i]["completion"] != "Yes":
                print("A completed task cannot be edited. Edit an uncompleted task.")
            else:
                while True:
                    edit_key = input("To edit task recepient, enter 1. To edit due date, enter 2: ")
                    if edit_key == 1:
                        while True:
                            new_recepient = input("Enter the username of the new recepient: ").lower()
                            if new_recepient not in users_dic.keys():
                                print("The user does not exist")
                            else:
                                tasks[i]["recepient"] = new_recepient
                                break
                        break

                    elif edit_key == 2:
                        due_date = input("Enter the task due date in the format DD MMM YYYY (e.g. 12 Mar 2020): ")
                        tasks[i]["d_date"] = due_date
        break


def generate_report():
    """This function generates task and user reports to the admin"""

    #---Generate task overview file---
    # count the number of tasks in task list
    num_tasks = len(tasks)

    # count the number of completed tasks
    num_completed_tasks = 0
    for task in tasks:
        if task["completion"] == "Yes":
            num_completed_tasks += 1

    # count the number of uncompleted tasks
    num_uncompleted_tasks = 0
    for task in tasks:
        if task["completion"] == "No":
            num_uncompleted_tasks += 1

    # count the number of overdue tasks
    # We convert and parse accordingly the due date and current date strings to datatime objects
    num_overdue_tasks = 0
    for task in tasks:     
        due_date = datetime.strptime(task["d_date"], "%d %b %Y")
        current_date = datetime.strptime(task["a_date"], "%d %b %Y")
        if task["completion"] == "No" and due_date < current_date:
            num_overdue_tasks += 1

    # Calculate the percentage of incomplete tasks
    percent_incomplete = (num_uncompleted_tasks / num_tasks) * 100

    # Calculate the percentage of overdue tasks
    percent_overdue = (num_overdue_tasks / num_tasks) * 100

    summary = "Total number of tasks: {}\nNumber of completed tasks: {}\n"\
    "Number of uncompleted tasks: {}\nNumber of overdue tasks: {}\n"\
    "Percentage of incomplete tasks: {:.2f}%\nPercentage of overdue tasks: {:.2f}%\n\n".format(num_tasks,\
    num_completed_tasks, num_uncompleted_tasks, num_overdue_tasks, percent_incomplete, percent_overdue)

    with open("task_overview.txt", "a") as fhand:
        fhand.write(summary)

    #---Generate user overview file---
    # count the number of users
    with open("user.txt", "r") as f1:
        num_users = 0
        for line in f1:
            num_users += 1
    
    num_tasks = len(tasks)

    with open("user_overview.txt", "a") as f:
        f.write("Total number of users: {num_users}\nTotal number of tasks assigned: {num_tasks}\n")

    fhand =  open("tasks.txt", "r")
    for user in users_dic.keys():
        # Count the total number of tasks assigned to each user
        count_user_task = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        count_overdue_tasks = 0
        for line in fhand:
            line = line.split(", ")
            due_date2 = datetime.strptime(line[5], "%d %b %Y")
            current_date2 = datetime.strptime(line[4], "%d %b %Y")
            if line[1].lower() == user:
                count_user_task += 1
                if line[6].lower() == "yes":
                    completed_tasks += 1 # Count the tasks completed
                else:
                    uncompleted_tasks += 1 # Count the uncompleted tasks
                    if due_date2 < current_date2:
                        count_overdue_tasks += 1

        percent_user_task = (count_user_task / num_tasks) * 100
        percent_completed_task = (completed_tasks / num_tasks) * 100
        percent_uncompleted_task = (uncompleted_tasks / num_tasks) * 100
        percent_overdue_task = (count_overdue_tasks / num_tasks) * 100

        user_summary = "033[1m====={}=====\033[0m\nTotal number of tasks: {}\n\
        Percentage of tasks that are assigned to {}: {:.2f}%\n\
        Percentage of tasks that have been completed: {:.2f}%\nPercentage of incomplete tasks: {:.2f}%\n\
        Percentage of overdue tasks: {:.2f}%\n\n".format(user, count_user_task, user,\
        percent_user_task, percent_completed_task, percent_uncompleted_task, percent_overdue_task)

        with open("user_overview.txt", "a") as f:
            f.write(user_summary)
    fhand.close()


def display_stats():
    """Function to display the number of users and tasks on the app"""

    # Code to count and display the total number of users to admin
    with open("user_overview.txt", "r") as f:
        firstline = f.readline()
        firstline = firstline.split(" ")
        print(f"\nThe total number of users is {firstline[-1]}")
        
    # Code to count and display the number of assigned tasks to admin
    with open("task_overview.txt", "r") as f:
        firstline = f.readline()
        firstline = firstline.split(" ")
        print(f"The total number of tasks is {firstline[-1]}")


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
    # gr - generate reports
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

    elif menu == "gr" and user_name == "admin":
        generate_report()

    elif menu == "ds" and user_name == "admin":
        display_stats()

    elif menu == "e":
        print('\nGoodbye!!!')
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again")