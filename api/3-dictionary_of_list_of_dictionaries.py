#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the JSON format."""
import json
import requests


if __name__ == '__main__':
    lista = []
    dic = {}
    title = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    usu = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    with open("todo_all_employees.json", mode="w") as f:
        for y in usu:
            user = int(y["id"])
            for x in title:
                if x["id"] == user:
                    lista.append({
                        "task": x['title'],
                        "completed": x["completed"],
                        "username": y["username"]
                    })
            dic[str(user)] = lista
            lista = []
        json.dump(dic, f)
