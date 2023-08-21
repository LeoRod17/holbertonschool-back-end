#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO
list progress."""
import requests
from sys import argv


id = argv[1]
req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                   .format(id)).json()
for x in req:
    print(x)
