#!/usr/bin/python3
""" Task 3 """

import json
import requests
import sys


if __name__ == '__main__':

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users/')

    to_json = {}
    with open("todo_all_employees.json", "w") as file:
        for user in users.json():
            all_tasks = []
            for task in tasks.json():
                the_dict = {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                all_tasks.append(the_dict)
            to_json.update({str(user["id"]): all_tasks})
        json.dump(to_json, file)
