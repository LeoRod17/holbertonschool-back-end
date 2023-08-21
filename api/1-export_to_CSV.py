#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID, returns information about his/her todo
list progress."""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    title = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)).json()
    usu = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(id)).json()
    for key, value in usu[0].items():
        if key == "username":
            name = value

    with open("{}.CSV".format(id), mode="w+") as f:
        w = csv.writer(f)
        for x in title:
            w.writerow([id, name, x["completed"], x["title"]])
