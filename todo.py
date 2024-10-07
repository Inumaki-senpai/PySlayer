from os import remove


def add():
    print("** Add Task **")
    headline = input("Task Headline: ")
    description = input("Description: ")

    try:
        with open(".tasks.txt", "x") as tasks:
            tasks.write(f"{headline}: {description}")

    except FileExistsError:
        with open(".tasks.txt", "a") as tasks:
            tasks.write(f"\n{headline}: {description}")

    print("Task Added..")


def rem():
    print("** Remove Task **")
    headline = input("Task Headline: ")
    with open(".tasks.txt", "r") as tasks:
        task_lines = tasks.readlines()

    with open(".tasks.txt", "w") as tasks:
        for line in task_lines:
            if not headline in line:
                tasks.write(line)

    if len(open(".tasks.txt", "r").readlines()) == 0:
        remove(".tasks.txt")

    print("Task no longer exists..")


def show():
    print("** Show Task **")
    try:
        with open(".tasks.txt", "r") as tasks:
            task_lines =  tasks.readlines()
    except FileNotFoundError:
        print("No tasks found.. \nEnjoy your day.. ( ^ _ ^ ) \n")
        return None

    # Print tasks from task_lines
    count = 1
    for i in task_lines:
        i = i.replace(":", "\n  Description: ")
        print(f"\n{count}. Headline: {i}", end="")
        count += 1

    print("\n\nThat's all for today..\n")


while True:
    print("** To Do Manager **")
    print(" 1. Add task")
    print(" 2. Remove task")
    print(" 3. Show tasks")
    print(" 4. Exit")

    choice = input("Enter your choice: ")
    print()
    match choice:
        case "1":
            add()
        case "2":
            rem()
        case "3":
            show()
        case "4":
            print("Thank You..")
            exit(0)


