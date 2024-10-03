
while 1:
    def add():
        print("** Add Task **")
        headline = input("Task Headline: ")
        description = input("Description: ")
        try:
            tasks = open(".tasks.txt", "r")
            tasks.close()
            tasks = open(".tasks.txt", "a")
            tasks.write(f"\n{headline}: {description}")
        except FileNotFoundError:
            tasks = open(".tasks.txt", "a+")
            tasks.write(f"{headline}: {description}")
        tasks.close()
        print("Task Added..")

    def remove():
        print("** Remove Task **")
        headline = input("Task Headline: ")
        tasks = open(".tasks.txt", "r")
        task = list()
        for line in tasks:
            if not headline in line:
                task.append(line)
        tasks.close()
        
        tasks = open(".tasks.txt", "w")
        for i in task:
            tasks.write(i)

        tasks.close()
        print("Task Removed..")


    def show():
        print("** Show Task **")
        tasks = open(".tasks.txt", "r+")
        file = tasks.read()

        # Print tasks from file
        count = 1
        for i in file:
            if i == ':':
                print("\n  Description: ", end="")
            else:
                if (i == '\n') or (count == 1):
                    print(f"\n\n{count}. Headline: ", end="")

                    if count == 1:
                        print(i, end="")

                    count += 1
                else:
                    print(i, end="")
        tasks.close()

        print("\n\nThat's all for today..\n")



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
            remove()
        case "3":
            show()
        case "4":
            print("Thank You..")
            exit(0)


