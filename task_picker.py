import sys
import pandas as pd
import random
import time

tasks = pd.read_csv("Tasks.csv")

pomodoro_slots = int(input("How many pomodoros do you want to do now?\n"))
available_tasks = [tasks.Task[index] for index in tasks.index if tasks.Done[index] == False]

availables_sum = 0
for index in tasks.index:
    if tasks.Done[index] == False:
        availables_sum += (tasks.alotted_pomodoros[index] - tasks.finished_pomodoros[index])
print("Overall, you can do", availables_sum, "pomodoros!")

if pomodoro_slots > availables_sum:
    print("Please rerun after adding more tasks!")
    sys.exit()


for pomodoro in range(pomodoro_slots):
    current_task = random.choice(available_tasks)
    print("The task you have now is", current_task, "and you have 25 mins to finish it!")

    tic = time.perf_counter()
    done = "placeholder"
    while done == "placeholder":
        done = input("Write anything when you're done!\n")
    toc = time.perf_counter()
    minutes_elapsed = round((toc - tic) / 60, 2)
    print("This task took you", minutes_elapsed, "minutes")

    wait = "placeholder"
    while wait == "placeholder":
        wait = input("Write anything when you're ready to continue!\n")

    for taskie_index in range(len(tasks.Task)):
        if current_task == tasks.Task[taskie_index]:
            tasks.finished_pomodoros[taskie_index] += 1
            if tasks.finished_pomodoros[taskie_index] == tasks.alotted_pomodoros[taskie_index]:
                tasks.Done[taskie_index] = "True"
            
    available_tasks = [tasks.Task[index] for index in tasks.index if tasks.Done[index] == False]
    print("Tasks left:", available_tasks)
    
    tasks.to_csv('Tasks.csv')