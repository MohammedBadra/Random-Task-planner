#Choosing and initializing the daily csv5
from datetime import datetime
import sys
import pandas as pd
import random
import time

#This part is just to offset cloud nine's (UTC) 8 hour difference
from datetime import datetime
from datetime import date

today = datetime.now().strftime("%d/%m/%Y/%H")
splitted_today = today.split("/")

csvname = ""
if int(splitted_today[-1]) in range(0, 8):
    if splitted_today[1] == "12":
        csvname = "0" + str(int(splitted_today[0]) - 1) + "Dec.csv"
else:
    if splitted_today[1] == "12":
        csvname = splitted_today[0] + "Dec.csv"

print(csvname)
tasks = pd.read_csv(csvname)

###########################################################################################################################################
#Initializing the planner

available_tasks = [tasks.Task[index] for index in tasks.index if tasks.Done[index] == False]
availables_sum = 0
final_break = 0
running_time_total = 0
task_count = 0

for index in tasks.index:
    if tasks.Done[index] == False:
        availables_sum += (tasks.alotted_pomodoros[index] - tasks.finished_pomodoros[index])
print("Overall, you can do", availables_sum, "pomodoros!\n")

pomodoro_slots = int(input("How many pomodoros do you want to do now?\n"))
if pomodoro_slots > availables_sum:
    print("Please rerun after adding more tasks!")
    sys.exit()
###########################################################################################################################################
for pomodoro in range(pomodoro_slots):
    current_task = random.choice(available_tasks)
    print(task_count, "pomodoros done, and", pomodoro_slots - task_count, "to go!")
    print("The task you have now is", current_task, "and you have 25 mins to finish it!")

    tic = time.perf_counter()
    done = "something"
    while done == "something":
        done = input("Write anything when you're done!\n")
    toc = time.perf_counter()
    minutes_elapsed = round((toc - tic) / 60, 2)
    running_time_total += minutes_elapsed
    print(running_time_total)
    print("This task took you", minutes_elapsed, "minutes\n")

    wait = "something"
    if pomodoro_slots - task_count != 1:
        while wait == "something":
            wait = input("Take a 5 minutes break and write anything when you're back!\n")
    else:
        final_break = (running_time_total / 25) * 5
        print("Yay! You're done :) \nTake a ", round(final_break), "minutes break at least. You earned it!\n")

    for taskie_index in range(len(tasks.Task)):
        if current_task == tasks.Task[taskie_index]:
            tasks.finished_pomodoros[taskie_index] += 1
            if tasks.finished_pomodoros[taskie_index] == tasks.alotted_pomodoros[taskie_index]:
                tasks.Done[taskie_index] = "True"

    available_tasks = [tasks.Task[index] for index in tasks.index if tasks.Done[index] == False]
    #print(tasks)
    print("Tasks left:", available_tasks, "\n")
    task_count += 1
    
    tasks.to_csv(csvname)