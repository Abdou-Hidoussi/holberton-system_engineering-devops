#!/usr/bin/python3
""" Task 1 """
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    user = {"User-Agent": "Abdou-Hidoussi"}

    if after is None:
        request = requests.get("https://www.reddit.com/r/{}/hot.json?"
                               .format(subreddit), headers=user)
    else:
        request = requests.get("https://www.reddit.com/r/{}/hot.json?after={}"
                               .format(subreddit, after), headers=user)

    children = request.json().get('data').get('children')
    after = request.json().get('data').get('after')

    if request.status_code == 200:
        for x in range(len(children)):
            hot_list.append(children[x].get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
