import json
import os
import re

def add_task(tasko):
    # taskos = {}
    # taskos.update(tasko)
    with open("To_Do_List_App.json", "w") as ft:
        json.dump(tasko, ft, indent=4)


def mark_done(task_num):
    with open("To_Do_List_App.json", "r") as fi:
        dat = json.load(fi)
        o = 1
        for ky in dat:
            if o == int(task_num):
                dat[ky] = "Done"
            o += 1
    with open("To_Do_List_App.json", "w") as fo:
        json.dump(dat, fo, indent=4)


tasks = {}
taskos = {}
print("Welcome to To-Do List App")
# print("1. Add Task")
# print("2. Mark as done")
while True:
    print("-------------------")
    print("1. Add Task")
    print("2. Mark as done")
    print("3. View Task")
    ans = input("enter the number(or e to exit):")
    status = "Pending"
    if ans == "1":
        while True:
            task = input("Enter your Task(or e to exit):")
            try:
                with open("To_Do_List_App.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                print("file is missing")
            if task in data:
                print("Task already exists")
                continue
            if task == "e":
                break
            tasks[task] = status
            if os.path.getsize("To_Do_List_App.json") > 0:
                with open("To_Do_List_App.json", "r") as f:
                    data = json.load(f)
                    tasks.update(data)
            else:
                data = {}
                # tasks.update(data)
            # taskos.update(tasks)
        add_task(tasks)
    elif ans == "2":
        with open("To_Do_List_App.json", "r") as f:
            data = json.load(f)
            i = 1
            for key, value in data.items():
                print(f"{i}--> {key} : {value}")
                i += 1
        while True:
            try:
                tsk_num = int(input("Enter number(or 108 to exit), to mark as done:"))
            except ValueError:
                print("Invalid input")
                continue
            if tsk_num == 108:
                break
            mark_done(tsk_num)
    elif ans == "3":
        x = 0
        search_task = input("Filter the tasks by:")
        with open("To_Do_List_App.json", "r") as fr:
            datr = json.load(fr)
            i = 1
            for k, v in datr.items():
                if matches := re.search(f"{search_task} .*", k):
                    print(f"{i}--> {k} : {v}")
                    x = 1
                i += 1
            if x == 0:
                print("Not Found")
    elif ans == "e":
        break

# print(tasks)

