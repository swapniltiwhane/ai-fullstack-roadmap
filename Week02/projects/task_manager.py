#Need to show menu options to the user
#1. Add Task
#2. Remove Task
#3. View Tasks
#4. Exit

print("Welcome to Task Manager")

task_list = []
def add_task():
    task = input("Enter the task you want to add: ")
    task_list.append(task)

def remove_task():
    task = input("Enter the task you want to remove: ")
    if task in task_list:
        task_list.remove(task)
    else:
        print("Task not found.")

def view_tasks():
    if not task_list:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")

def display_menu():
    print("\nChoose an option from the menu below:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def main():
    display_menu()
        
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Thank you for using Task Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

main()