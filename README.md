# Random-Task-planner
Random task planner using the pomodoro technique

Each task is designed to take a number of pomodoros of 25 minutes each. Add tasks and set the number of alloted pomodoros for each one in the csv file.
The csv file, tasks.csv, template is included.

Usage:
1. Execute w/ this to avoid irrelevant warnings:

    ```bash
    python -W ignore task_picker.py
    ```
    
2. Use the Task template.csv to fill in your tasks and then rename it in this format: "xxYyy", where "xx" is the day's date in numbers and "Yyy" are first three
letters of the *month's literal name. Note that the first letter in "Yyy" is capitalized.

*December is currently hardcoded into the planner.
