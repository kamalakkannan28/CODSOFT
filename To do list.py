todo_list = []

while True:
    print("\nTo-Do List Menu:\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
    elif choice == '2':
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(todo_list):
            todo_list.pop(task_num - 1)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
