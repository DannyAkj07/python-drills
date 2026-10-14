def to_do():
    tasks = []
    while True:
        print("======= TO-DO LIST =======")
        print('-' * 26)
        print ("[A] Add Task")
        print ("[V] View Tasks")
        print ("[R] Remove Task")
        print ("[Q] Quit")
        prompt = input("Enter your choice between (A/V/R/Q): ").lower().strip()
        print("-" * 26)

        if prompt == "a":
            add = input("Enter new task: ").strip()
            if add:
                tasks.append(add)
                print(f"Task '{add}' added!")
            else:
                print("Task cannot be empty")

        elif prompt == 'v':
            if not tasks:
                print("No tasks found.")
            else:
                print("YOUR TASKS:")
                for index, item in enumerate(tasks,start=1):
                    print(f" {index}. {item}")

        elif prompt == "r":
            if not tasks:
                print("No tasks to remove.")
            else:
                print("YOUR TASKS")
                for index, item in enumerate(tasks,start=1):
                    print(f" {index}. {item}")

                try:
                    num = int(input("Enter task number to delete: "))
                    index = num - 1
                    if index >= 0 and index < len(tasks):
                        removed = tasks.pop(index)
                        print(f"Removed task: '{removed}'")
                    else:
                        print("Error: Task number does not exist.")
                except ValueError:
                    print("Error: Please enter a valid number.")
        elif prompt == "q":
            print("Thanks for using To-Do List. Goodbye")
            break

        else:
            print("Invalid choice, please select A, V, R, or Q.")

to_do()