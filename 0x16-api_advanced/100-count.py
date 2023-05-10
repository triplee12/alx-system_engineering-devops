#!/usr/bin/python3
""" Count keywords """
import requests

def count_words(subreddit, word_list, hot_list=[], after=None, word_counts={}):
    """ Count keywords """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data['data']['after']
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if (f' {word.lower()} ' in f' {title} ') or (f' {word.lower()}. ' in f' {title} ') or (f' {word.lower()}! ' in f' {title} ') or (f' {word.lower()}-' in f' {title} ') or (f' {word.lower()}?' in f' {title} ') or (title.startswith(f'{word.lower()} ')) or (title.endswith(f' {word.lower()}')):
                    if word.lower() in word_counts:
                        word_counts[word.lower()] += 1
                    else:
                        word_counts[word.lower()] = 1
        if after:
            return count_words(subreddit, word_list, hot_list, after, word_counts)
        else:
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word_count in sorted_word_counts:
                print(f'{word_count[0]}: {word_count[1]}')
    else:
        print(None)
