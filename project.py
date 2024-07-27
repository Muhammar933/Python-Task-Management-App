def task():
    task = [] #empty list
    print('-------WELCOME TO THE TASKE MANAGEMENT APP------')
    

    total_task = int(input('Enter how many tasks you want to add ='))
    for i in range(1, total_task+1):
        task_name = input('Enter task {i} = ')
        task.append(task_name)
    
    print(f"Todays's task are\n{task}")

    while True:
        operation = int(input('Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/'))
        if operation == 1:
            add = input('Enter your taske you want to add =')
            task.append(add)
            print(f'Task {add} has been added successfully')

        elif operation ==2:
            update_val = input('enter the task name you want to update =')
            if update_val in task:
                up = input('Enter Your task')
                ind = task.index(update_val)
                task[ind] = up
                print(f'Updated task {up}')

        elif operation == 3:
            del_val = input('WHich task You Want to delete =')
            if del_val in task:
                ind = task.index(del_val)
                del task[ind]
                print(f'Task {del_val} has been deleted successfully')
        elif operation == 4:
            print(f'Total tasks = {task} ')
        
        elif operation == 5:
            print('CLosing the program....')
            break

        else:
            print('Invalid Input!!')

task()