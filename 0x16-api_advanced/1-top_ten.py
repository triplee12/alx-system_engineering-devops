#!/usr/bin/python3
""" Top ten posts """
import requests


def top_ten(subreddit):
    """ Return top 10 posts """
    headers = {'User-Agent': 'Mozilla/5.0'}
    Apiurl = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    resp = requests.get(Apiurl, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
