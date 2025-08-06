def add_task():
    task = input("enter task:")
    with open("tasks.txt","a") as file:
        file.write(task + "\n")
        print("task added")
        
def view_task():
    try:
        with open ("tasks.txt","r") as file:
            tasks = file.readlines()
            if tasks:
                print("Your Tasks")
                for idx, task in enumerate(tasks,1):
                    print(f"{idx}.{task.strip()}")
            else:
                print("No Task found")
    except FileNotFoundError:
        print("No file found, Start by adding task")
                
def delete_task():
    try:
        with open("tasks.txt","r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks to delete")
            return
        view_task()
        num= int(input("enter the task no to delete task:"))
        if 1<=num<=len(tasks):
            delete = tasks.pop(num-1)
            with open("tasks.txt","w") as file:
                file.writelines(tasks)
                print(f"Deleted task:{delete.strip()}")
        else:
            print("Invalid task number")
        
    except FileNotFoundError:
        print("No file Found")
    except ValueError:
        print("Please enter a valid number")
            
def edit_task():
    try:
        with open ("tasks.txt","r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No Task to edit")
            return
        view_task()
        num =int(input("enter the task to edit:"))
        if 1<=num<=len(tasks):
            new_task = (input("enter the new task:"))
            tasks[num-1] = new_task+ "\n"
            with open("tasks.txt","w") as file:
                file.writelines(tasks)
                print("task updated")
        else:
            print("Enter valid number")
    except FileNotFoundError:
        print("No file found")
    except ValueError:
        print("Enter a valid number")
            
while True:
    print("--To Do List Menu--")
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Edit Task")
    print("5.Exit")
    
    choice = (input("Enter the choice:"))
    
    if choice=='1':
        add_task()
    elif choice=='2':
        view_task()
    elif choice=='3':
        delete_task()
    elif choice=='4':
        edit_task()
    elif choice=='5':
        print("Exiting To Do List App. Goodbye!")
        break    
    else:
        print("Invalid choice please enter a number from 1 to 5 ")        
        
    
    
    
    
    
    

    
    
        
    
        
        
        
        
    
    
        
        
            
        
    
    