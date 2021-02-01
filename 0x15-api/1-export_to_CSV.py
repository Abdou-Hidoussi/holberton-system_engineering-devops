#!/usr/bin/python3
""" Task 1 """

import requests
from sys import argv
import csv


if __name__ == "__main__":
    data = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
    name = data.json().get('name')
    username = data.json().get('username')

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

    with open("{}.csv".format(argv[1]), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in data.json():
            writer.writerow([argv[1], username,
                            task.get("completed"), task.get("title")])
