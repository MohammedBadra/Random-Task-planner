#Choosing and initializing the daily csv
from datetime import datetime, timezone, date
import sys
import pandas as pd
import random
import time
import pytz

#timezone = "America/Los_Angeles"
timezone = "Asia/Seoul"

utc_now = pytz.utc.localize(datetime.utcnow())
my_timezone_now = utc_now.astimezone(pytz.timezone(timezone))

raw_today = my_timezone_now.strftime("%d/%m/%Y/%H")
today = raw_today.split("/")
###########################################################################################################################################

#parsing the monthly database csv file
months_dict = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

year = str(int(today[2]) - 2000)
month = months_dict[int(today[1])]

csvname = month + year + ".csv"

try:
    tasks = pd.read_csv(csvname)
except FileNotFoundError:
    temp = pd.read_csv("month_template.csv")
    temp.to_csv(csvname)
    print("The file didn't exist. We created it for you! Please fill it and rerun!")
    sys.exit()

tasks = pd.read_csv(csvname)
#tasks
###########################################################################################################################################

###########################################################################################################################################
#Initializing the planner

#retreiving today's date to parse for it in the csv. format: DD/MM/YYYY
today_check = raw_today[:10]

available_tasks = [tasks.Task[index] for index in tasks.index if (tasks.Done[index] == False) and (tasks.Date[index] == today_check)]
availables_sum = 0
final_break = 0
running_time_total = 0
task_count = 0

for index in tasks.index:
    if (tasks.Done[index] == False) and (tasks.Date[index] == today_check):
        availables_sum += (tasks.alotted_pomodoros[index] - tasks.finished_pomodoros[index])
print("Overall, you can do", availables_sum, "pomodoros!\n")

pomodoro_slots = int(input("How many pomodoros do you want to do now?\n"))
if pomodoro_slots > availables_sum:
    print("Please rerun after adding more tasks!")
    sys.exit()
###########################################################################################################################################

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
        print("Your total runtime:", running_time_total)
        print("Yay! You're done :) \nTake a ", round(final_break), "minutes break at least. You earned it!\n")

    for taskie_index in range(len(tasks.Task)):
        if current_task == tasks.Task[taskie_index]:
            tasks.finished_pomodoros[taskie_index] += 1
            if tasks.finished_pomodoros[taskie_index] == tasks.alotted_pomodoros[taskie_index]:
                tasks.Done[taskie_index] = "True"

    available_tasks = [tasks.Task[index] for index in tasks.index if (tasks.Done[index] == False) and (tasks.Date[index] == today_check)]
    #print(tasks)
    print("Tasks left:", available_tasks, "\n")
    task_count += 1

    tasks.to_csv(csvname)