import requests

url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)

if response.status_code == 200:
    todos = response.json()
else:
    print("Не удалось получить данные")


import os
import json

if not os.path.exists('temp'):
    os.mkdir('temp')

for todo in todos:
    with open(f'temp/{todo["id"]}.json', 'w') as file:
        json.dump(todo, file)





import pandas as pd
from openpyxl import Workbook

workbook = Workbook()
worksheet = workbook.active

for root, dirs, files in os.walk('temp'):
    for file in files:
        if file.endswith('.json'):
            with open(os.path.join(root, file), 'r') as json_file:
                data = json.load(json_file)
                worksheet.append(data.values())

workbook.save('todos.xlsx')




