#!/usr/bin/python3
"""DataAPI module"""
import requests
import sys


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    resp1 = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_name = resp1.json().get('name')
    resp2 = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    responses = resp2.json()
    done_tasks = [resp for resp in responses if resp.get('completed')]
    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, len(done_tasks), len(responses)))
    for done in done_tasks:
        print('\t {}'.format(done.get('title')))
