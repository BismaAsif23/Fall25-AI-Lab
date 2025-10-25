def task(): 
    tasks = []
    print("this is a task management app")
    total_tasks = int(input("tasks to be added:"))

    for i in range (1, total_tasks+1):
        task_name = input(f"enter task {i}:")
        tasks.append(task_name)
    print("tasks are :",tasks)
    
    while True :
        opt = int(input("enter 1 to Add task: \n enter 2 to update task: \n enter 3 to Delete tasks:\n enter 4 to View task:\n enter 5 to count task:\n enter 6 to exit task:\nEnter your number for operation:"))


        if opt == 1 :
            add = input("enter task to be added:")
            tasks.append(add)
            print(f" Task {add} has been added")
        elif opt == 2 :
            update = input("enter task to be updated:")
            if update in tasks :
                up = input("enter new task:")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f" updated task {up}")
        elif opt == 3 :
            delete = input("enter task to be deleted:")
            if delete in tasks :
                ind = tasks.index(delete)
                del tasks[ind]
                print(f" task {delete} has been deleted")
        elif opt == 4 :
            print(f"total tasks are {tasks}")

        elif opt == 5 :
            count = len(tasks)
            print(f"there are {count} tasks in list")



        elif opt ==6 :
            print("exiting the program")
            break
        else :
            print("invalid input")
task()