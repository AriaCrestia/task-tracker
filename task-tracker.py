import os
# Code for showing tasks in list
def ShowTasks():
    if (len(taskList) == 0):
        os.system("clear")
        print("----")
        print("no tasks active.")
    elif (len(taskList) > 0):
        taskList.sort()
        taskPos = 0
        taskNum = 1
        os.system("clear")
        print("----")
        while (taskPos != len(taskList)):
            print(str(taskNum) + ". " + str(taskList[taskPos]))
            taskPos += 1
            taskNum += 1
        taskPos = 0
        print("----")
# Code for adding tasks to list
def AddTask():
    os.system("clear")
    print("----")
    add_task = str(input("Task name: "))
    taskList.append(add_task)
    ShowTasks()
# Code for removing tasks from list
def RemoveTask():
    os.system("clear")
    print("----")
    if (len(taskList) == 0):
        print("no tasks to remove.")
    elif (len(taskList) > 0):
        user_input = int(input("Task number: "))
        if (user_input < 1) or (user_input > len(taskList)):
            print("task does not exist.")
        else:
            remove_task = user_input
            remove_task -= 1
            taskList.remove(taskList[remove_task])
            print("task removed.")
            ShowTasks()

print("ready to go.")
taskList = []
ShowTasks()
run = 0
# Code for user input
while (run == 0):
    user_input = str(input(" -> "))
    user_input = user_input.lower()
    if (user_input == "show"):
        ShowTasks()
    elif (user_input == "add"):
        AddTask()
    elif (user_input == "remove"):
        RemoveTask()
    elif (user_input == "end"):
        run = 1
    else:
        os.system("clear")
        ShowTasks()
        print("unavailable command")
