#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the JSON format.."""
import json
from sys import argv
import requests


if __name__ == '__main__':
    id = argv[1]
    lista = []
    title = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)).json()
    usu = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(id)).json()

    with open("{}.json".format(id), mode="w") as f:
        for x in title:
            if x['userId'] == id:
                lista.append({
                    "task:": x["title"], "completed": x["completed"],
                    "username": usu["username"]})
        json.dump({'{}'.format(id): lista}, f)
