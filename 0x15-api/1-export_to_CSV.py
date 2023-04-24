#!/usr/bin/python3
"""DataAPI module"""
import csv
import requests
import sys


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    resp1 = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_username = resp1.json().get('username')
    resp2 = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    responses = resp2.json()
    with open('{}.csv'.format(employee_id), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in responses:
            writer.writerow([
                employee_id,
                employee_username,
                task.get('completed'),
                task.get('title')
            ])
