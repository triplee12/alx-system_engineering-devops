#!/usr/bin/python3
""" Recursive endpoint calling """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Recursively call endpoint """
    headers = {'User-Agent': 'Mozilla/5.0'}
    Apiurl = 'https://www.reddit.com/r/{subreddit}/hot.json'.format(subreddit)
    params = {'limit': 100}
    if after:
        params['after'] = after
    resp = requests.get(Apiurl, headers=headers, params=params, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        after = data['data']['after']
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
