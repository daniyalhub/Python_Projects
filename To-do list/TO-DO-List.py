# Simple TO DO list

tasks = []

def load_tasks():
    try:
        with open("tasks.txt") as file:
            return file.read().splitlines()
    except:
        return {}    

def save_tasks(tasks):
    with open("Tasks.txt" , 'w') as file:
        for task in tasks:
            file.write(task + "\n")

task = load_tasks 

while True:
    print("==============================")
    print("----------To do list----------")
    print("==============================")
    print("\n1. Add task", flush=True)
    print("2. Show tasks", flush=True)
    print("3. Delete task", flush=True)
    print("4. Exit", flush=True)

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("\nEnter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task successfully added😎.", flush=True)

    elif choice == "2":
        if len(tasks) == 0:
            print("\nThere is no task added.",flush=True)
        else:
            print("Your tasks")
            for i in range(len(tasks)):
                print(f"{i+1} .{tasks[i]} ", flush=True)

    elif choice == "3":            
        if len(tasks) == 0:
            print("\nThere is no task added.",flush=True)
        else:
            print("Your tasks")
            for i in range(len(tasks)):
                print(f"{i+1} .{tasks[i]} ", flush=True)

            num = int(input("Enter your choice: "))    
            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)
                print("\nloading..........", flush=True)
                print("\nTask deleted!", flush=True)
                print(tasks)
            else:
                print("Invalid choice!",flush=True)

    elif choice == "4":
        print("Good bye👋", flush=True)
        break        

    else:
        print("Invalid choice")    