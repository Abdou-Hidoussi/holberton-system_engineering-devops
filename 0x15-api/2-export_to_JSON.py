#!/usr/bin/python3
""" Task 2 """

import json
import requests
from sys import argv


if __name__ == "__main__":
    data = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])

    name = data.json().get('name')
    username = data.json().get('username')

    data = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1] + '/todos')
    done = 0
    done_task = []
    all_task = []
    for task in data.json():
        all_task.append(task)
        if task['completed']:
            done_task.append(task['title'])
            done += 1
    total = len(data.json())
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))

    for task in done_task:
        print("\t {}".format(task))

    with open("{}.json".format(argv[1]), mode='w') as file:
            json.dump({argv[1]: [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            } for task in data.json()]}, file)
