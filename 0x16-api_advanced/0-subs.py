#!/usr/bin/python3
""" Api advanced """
import requests


def number_of_subscribers(subreddit):
    """ Return number of subscribers """
    headers = {'User-Agent': 'Mozilla/5.0'}
    Apiurl = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    resp = requests.get(Apiurl, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        return data['data']['subscribers']
    else:
        return 0
