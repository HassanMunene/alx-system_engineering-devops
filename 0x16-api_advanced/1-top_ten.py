#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    # defining the limit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    # setting user-agent
    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        # Making request
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        # check if data containing posts
        if 'data' in data and 'children' in data['data']:
            # Extract and print the titles of the first 10 posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None")
    except requests.exceptions.RequestException:

        print("None")
    except KeyError:

        print("None")


if __name__ == '__main__':

    subreddit = "cybersecurity"
    top_ten(subreddit)
