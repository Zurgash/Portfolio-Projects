#=====importing libraries===========
import datetime

#====Login Section====
# Read users from user.txt and store them in a dictionary
users = {}
with open("user.txt", "r") as file:
    for line in file:
        # Check if the line is not empty and correctly formatted
        if line.strip():
            try:
                username, password = line.strip().split(", ")
                users[username] = password
            except ValueError:
                print(f"Error reading line: {line.strip()}")

# Validate user login using a while loop
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful.")
        break
    else:
        print("Invalid username or password. Try again.")

while True:
    # Present the menu to the user and make sure that the user input is converted to lower case.
    # If username != admin we will use the else statement
    if username == "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # Checks if input "r" is used by the admin
    # If true the admin is allowed to register a new user
    # We also check to see if usernames exist and ensure passwords match
    # With responses

    if menu == 'r' and username == "admin":
        new_username = input("Enter new username: ")
        if new_username in users:
            print("Username already exists. Try again.")
        else:
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm password: ")
            if new_password == confirm_password:
                users[new_username] = new_password
                with open("user.txt", "w") as file:
                    for uname, pwd in users.items():
                        file.write(f"{uname}, {pwd}\n")
                print("User registered successfully.")
            else:
                print("Passwords do not match. Try again.")
                
    # If menu selected "a" we allow the user to add tasks to specific users
    # Validate that the user exists in our database
    # We prompt the user to enter task details such as title, description, due date and date assigned_date
    # As well as give feedback whether or not the task was added successfully

    elif menu == 'a':
        task_username = input("Enter the username of the person the task is assigned to: ")
        if task_username not in users:
            print("User does not exist. Please enter a valid username.")
            continue
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
        assigned_date = datetime.date.today().strftime("%Y-%m-%d")
        with open("tasks.txt", "a") as file:
            file.write(f"{task_username}; {title}; {description}; {assigned_date}; {due_date}; No\n")
        print("Task added successfully.")

    # We print out all the tasks added to our system with va command
    # printing out all relevant task information

    elif menu == 'va':
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split("; ")
                if len(task_data) == 6:
                    print("-----------------------------------------------------------------------------")
                    print(f"Task: \t\t\t{task_data[1]}\nAssigned to:\t\t{task_data[0]}\nAssigned Date:\t\t{task_data[3]}\nDue Date:\t\t{task_data[4]}\nTask Complete?:\t\t{task_data[5]}\nTask description:\n{task_data[2]}")
                    print("-----------------------------------------------------------------------------")
                else:
                    print(f"Error reading line: {line.strip()}")

    elif menu == 'vm':
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split("; ")
                if len(task_data) == 6 and task_data[0] == username:
                    print("-----------------------------------------------------------------------------")
                    print(f"Task: \t\t\t{task_data[1]}\nAssigned to:\t\t{task_data[0]}\nAssigned Date:\t\t{task_data[3]}\nDue Date:\t\t{task_data[4]}\nTask Complete?:\t\t{task_data[5]}\nTask description:\n{task_data[2]}")
                    print("-----------------------------------------------------------------------------")
    elif menu == 'ds' and username == "admin":

        # Display the total number of tasks as well as the total number of users

        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        print("------------------------------------")
        print(f"Total number of tasks: {len(tasks)}")
        print(f"Total number of users: {len(users)}")
        print("------------------------------------")

    # Command "e" to exit the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Printing error response
    else:
        print("You have entered an invalid input. Please try again")
