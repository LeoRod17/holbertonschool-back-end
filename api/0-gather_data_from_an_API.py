#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID, returns information about his/her todo
list progress."""
import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    title = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)).json()
    usu = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(id)).json()
    truecount = 0
    count = 0
    for key, value in usu[0].items():
        if key == "name":
            name = value
    for x in range(len(title)):
        for y, z in title[x].items():
            if y == "completed" and z:
                truecount = truecount + 1
        count = count + 1
    print("Employee {} is done with tasks({}/{}):".format(
        name, truecount, count))
    for x in title:
        if x["completed"]:
                print("\t {}".format(x["title"]))
