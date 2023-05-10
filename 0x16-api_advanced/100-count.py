#!/usr/bin/python3
""" Count keywords """
import requests

def count_words(subreddit, word_list, word_count=[], page_after=None):
    """ Count keywords """
    headers = {'User-Agent': 'Mozilla/5.0'}
    word_list = [word.lower() for word in word_list]

    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is None:
        Apiurl = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        resp = requests.get(Apiurl, headers=headers, allow_redirects=False)
        if resp.status_code == 200:
            for child in resp.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1

            if resp.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, resp.json()['data']['after'])
    else:
        Apiurl = ('https://www.reddit.com/r/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))
        resp = requests.get(Apiurl, headers=headers, allow_redirects=False)

        if resp.status_code == 200:
            for child in resp.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1
            if resp.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, resp.json()['data']['after'])
            else:
                dicto = {}
                for key_word in list(set(word_list)):
                    i = word_list.index(key_word)
                    if word_count[i] != 0:
                        dicto[word_list[i]] = (word_count[i] *
                                               word_list.count(word_list[i]))

                for key, value in sorted(dicto.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(key, value))
