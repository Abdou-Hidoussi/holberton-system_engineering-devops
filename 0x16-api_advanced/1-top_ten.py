#!/usr/bin/python3
""" Task 1 """
import json
import requests


def top_ten(subreddit):
    user = {"User-Agent": "Abdou-Hidoussi"}
    request = requests.get("https://www.reddit.com/r/{}/hot/.json?limit=10"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        nb = 0
        for posts in request.json().get("data").get("children"):
            if nb < 10:
                print("#"+posts.get("data").get("title")+"#")
                nb += 1
            else:
                break
    else:
        print("None")
