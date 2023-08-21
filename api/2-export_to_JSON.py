#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the JSON format.."""
import requests
from sys import argv
import json

if __name__ == '__main__':
    id = int(argv[1])
    lista =[]
    title = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)).json()
    usu = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(id)).json()
    for key, value in usu[0].items():
        if key == "username":
            name = value

    with open("{}.json".format(id), mode="w") as f:
        for x in title:
            lista.append({
                "task:": x["title"], "completed": x["completed"], "username": name})
        json.dump(lista,f)
