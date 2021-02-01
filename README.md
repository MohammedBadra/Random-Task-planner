# Random-Task-planner
Random task planner using the pomodoro technique

Each task is designed to take a number of pomodoros of 25 minutes each. If the taks take longer, the program will adjust the break duration accordingly.
The seed csv template, month_template.csv, is included.

Usage:
1. Execute w/ this to avoid irrelevant warnings:

    ```bash
    python -W ignore task_picker.py
    ```
    
2. If the monthly csv file doesn't already exist, the program generates it for you in this form: "MmmYY.csv" in the first run. Then, go ahead and fill the "Task" column in the respective month csv file, and add the date to the corresponding "Date" in this format: "DD/MM/YYYY".

Notes:
1. Only use this planner with tasks of equivalent priorities. Updates on prioritization preferences will be rolled out soon


Glossary:
1. Mmm: first three letters of the *month's literal name
2. YY: last two digits of the year
3. DD: day in numbers
4. MM: month in numbers
5. YYYY" year in numbers
