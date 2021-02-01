#!/usr/bin/python3
""" Task 0 """

import requests
from sys import argv


if __name__ == "__main__":
    data = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    name = data.json().get('name')

    data = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1] + '/todos')
    done = 0
    done_task = []
    for task in data.json():
        if task['completed']:
            done_task.append(task['title'])
            done += 1
    total = len(data.json())
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in done_task:
        print("\t {}".format(task))
